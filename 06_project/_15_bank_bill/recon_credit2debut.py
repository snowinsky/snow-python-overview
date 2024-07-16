# 业务操作分如下步骤
# 1.客户发起扣款，通过vendor还钱
# 2.local收到还钱的信息流，去homer对账
# 3.t+1之后，财务从收款账号收钱
# 因此，对账分四方，
# 第一，vendor的还钱流水==》local的还钱流水（reconcile-v3功能完成）
# 第二，local的还钱流水==》homer的配账流水（由监控完成，确保客户还款都配账，有gap，22点后停止配账，转天配账）
# 第三，homer的配账流水==》收款账号的收款流水（暂时缺失，现有收款账号的收款流水信息，但没有对账匹配）
# 第四，财务的资金流水==》收款账号的收款流水（依赖homer的配账流水，因为有线下还款）

###########################################
# 尝试实现 local还钱流水与收款账号的收款流水的配账
###########################################

# 首先对直联渠道，直联渠道都是实时到账，tradeTime=settleTime，所以对账时间是一致的，不用t+1
# 第一，先从oracle的paydb中获取收款账号对账单的信息，汇总后备用
# 第二，从mysql的ssdd router中获取直联代扣渠道的信息，然后汇总备用
# 第三，将两者的信息进行汇总，并对账，找出差异点

# 第一，先从oracle的paydb中获取收款账号对账单的信息，汇总后备用

import datetime as dt
from datetime import *

from db_access import oracle_paydb_recon


def get_credit_bank_bill_summary_from_oracle(recon_date):
    start_date = dt.datetime.strptime(recon_date, '%Y%m%d')
    end_date = start_date + dt.timedelta(days=1)
    get_credit_bank_summary = '''
    SELECT
        b.CHANNEL_CODE AS vendor_group,
        b.HCC_ACCOUNT AS deduct_to_acct,
        sum(b.AMOUNT)*100 AS deduct_to_amt_sum
    FROM
        T_RECON_S_DETAIL_B b
    WHERE
        b.trade_time >= :start_date
        AND b.trade_time < :end_date
    GROUP BY
        b.CHANNEL_CODE ,
        b.HCC_ACCOUNT
    ORDER BY
        b.CHANNEL_CODE ,
        b.HCC_ACCOUNT 
    '''
    sql_parameter_map = {'start_date': start_date, 'end_date': end_date}
    return oracle_paydb_recon.execute_query_sql(get_credit_bank_summary, sql_parameter_map)


# 第二，从mysql的ssdd router中获取直联代扣渠道的信息，然后汇总备用

from db_access import mysql_ssdd


def get_debit_trade_summary_from_mysql(recon_date) -> list:
    sql = '''
    with temp_vendor_group as (
    select
        1 as id_vendor,
        'ABCDD-CFC' as vendor_group
    union
    select
        2 as id_vendor,
        'CCB-OL' as vendor_group
    union
    select
        12 as id_vendor,
        'CCB-OL' as vendor_group
    union
    select
        3 as id_vendor,
        'BAOFUDD-CFC' as vendor_group
    union
    select
        16 as id_vendor,
        'BAOFUDD-CFC' as vendor_group
    union
    select
        4 as id_vendor,
        'JDPAY' as vendor_group
    union
    select
        5 as id_vendor,
        'BOCDD-CFC' as vendor_group
    union
    select
        6 as id_vendor,
        'ICBCDD-CFC' as vendor_group
    union
    select
        7 as id_vendor,
        'YINYIN-OL' as vendor_group
    union
    select
        8 as id_vendor,
        'EBUDD-CFC' as vendor_group
    union
    select
        10 as id_vendor,
        'PSBC-OL' as vendor_group
    union
    select
        11 as id_vendor,
        'CAPP-WECHAT' as vendor_group
    union
    select
        13 as id_vendor,
        'PSBC-OL' as vendor_group
    union
    select
        15 as id_vendor,
        'ALIPAY' as vendor_group
    union
    select
        22 as id_vendor,
        'ICBC-SZ' as vendor_group
    union
    select
        17 as id_vendor,
        'CHINAPAY-SingleDD' as vendor_group
    ),
    temp_vendor_acct as (
    select
        va.id as id_vendor_account,
        case
            vg.vendor_group 
            when 'ABCDD-CFC' then left(va.account_number, 15)
            when 'CCB-OL' then va.account_number
            when 'BAOFUDD-CFC' then va.cmb_number
            when 'JDPAY' then left(va.account_number,15)
            when 'BOCDD-CFC' then va.account_number
            when 'ICBCDD-CFC' then va.account_number
            when 'YINYIN-OL' then va.account_number
            when 'PSBC-OL' then va.account_number
            when 'ICBC-SZ' then va.account_number
            when 'CHINAPAY-SingleDD' then va.account_number
            else va.cmb_number
        end as deduct_to,
        vg.vendor_group
    from
        t_vendor_account va
    join temp_vendor_group vg
      on
        va.id_vendor = vg.id_vendor
    )
    select
        vg.vendor_group as vendor_group,
        va.deduct_to as deduct_to_acct,
        CAST(sum(res.debited_amount) AS UNSIGNED) as deduct_to_amt_sum
    from
        t_dd_response res
    left join temp_vendor_group vg on
        res.id_vendor = vg.id_vendor
    left join t_deduct_response dres on
        res.id_deduct_response = dres.id
    left join t_deduct_request dreq on
        dres.id_deduct_request = dreq.id
    left join temp_vendor_acct va on
        dreq.id_vendor_account = va.id_vendor_account
    where
        res.cdate >= %(start_date)s
        and res.cdate < %(end_date)s
        and res.return_code = '0000'
    group by
        vg.vendor_group,
        va.deduct_to
    order by vg.vendor_group,
        va.deduct_to;
    '''
    start_date = dt.datetime.strptime(recon_date, '%Y%m%d')
    end_date = start_date + dt.timedelta(days=1)
    sql_param_dict = {'start_date': start_date, 'end_date': end_date}
    return mysql_ssdd.execute_query_sql(sql, sql_param_dict)


###############################################
# 对账渠道分三部分 ###############################
# 第一部分，直联渠道direct linkage vendor
# 这种渠道都是直联银行，直接同行转账，所以结算日和交易日是同一天
# 因此，对账是T+0对账
# ABCDD-CFC
# CCB-OL
# BOCDD-CFC
# ICBCDD-CFC
# ICBC-SZ
###############################################
# 第二部分，银行的三方渠道，例如宝付，京东等 non-direct dd vendor
# 这种渠道都是t+1对账，结算日是交易日的第二天
# BAOFUDD-CFC
# JDPAY
# YINYIN-OL
# EBUDD-CFC
# PSBC-OL
# CHINAPAY-SingleDD
###############################################
# 第三部分，微信支付宝渠道，clientddvendor
# 这种渠道也是t+1对账，结算日是交易日的第二天
# 和三方渠道不同之处在于，它没有结算账号的概念，都是统一收账，因此没有结算账号明细
# CAPP-WECHAT
# ALIPAY
###############################################

###############################################
# 对账方向是 local==> bank 属于资金流对账，以某一天的local的数据做基准
# 确保local扣款数据都已经资金流到账
###############################################
###############################################

sql_mysql_ssdd_template = '''
        with temp_vendor_group as (
        select
            1 as id_vendor,
            'ABCDD-CFC' as vendor_group
        union
        select
            2 as id_vendor,
            'CCB-OL' as vendor_group
        union
        select
            12 as id_vendor,
            'CCB-OL' as vendor_group
        union
        select
            3 as id_vendor,
            'BAOFUDD-CFC' as vendor_group
        union
        select
            16 as id_vendor,
            'BAOFUDD-CFC' as vendor_group
        union
        select
            4 as id_vendor,
            'JDPAY' as vendor_group
        union
        select
            5 as id_vendor,
            'BOCDD-CFC' as vendor_group
        union
        select
            6 as id_vendor,
            'ICBCDD-CFC' as vendor_group
        union
        select
            7 as id_vendor,
            'YINYIN-OL' as vendor_group
        union
        select
            8 as id_vendor,
            'EBUDD-CFC' as vendor_group
        union
        select
            10 as id_vendor,
            'PSBC-OL' as vendor_group
        union
        select
            11 as id_vendor,
            'CAPP-WECHAT' as vendor_group
        union
        select
            13 as id_vendor,
            'PSBC-OL' as vendor_group
        union
        select
            15 as id_vendor,
            'ALIPAY' as vendor_group
        union
        select
            22 as id_vendor,
            'ICBC-SZ' as vendor_group
        union
        select
            17 as id_vendor,
            'CHINAPAY-SingleDD' as vendor_group
        ),
        temp_vendor_acct as (
        select
            va.id as id_vendor_account,
            case
                vg.vendor_group 
                when 'ABCDD-CFC' then left(va.account_number, 15)
                when 'CCB-OL' then va.account_number
                when 'BOCDD-CFC' then va.account_number
                when 'ICBCDD-CFC' then va.account_number
                when 'ICBC-SZ' then va.account_number
                when 'BAOFUDD-CFC' then va.cmb_number
                when 'JDPAY' then left(va.account_number,15)
                when 'YINYIN-OL' then va.account_number
                when 'EBUDD-CFC' then va.account_number
                when 'PSBC-OL' then va.account_number
                when 'CHINAPAY-SingleDD' then va.account_number
                else va.cmb_number
            end as deduct_to,
            vg.vendor_group
        from
            t_vendor_account va
        join temp_vendor_group vg
          on
            va.id_vendor = vg.id_vendor
        )
        select
            vg.vendor_group as vendor_group,
            va.deduct_to as deduct_to_acct,
            CAST(sum(res.debited_amount) AS UNSIGNED) as deduct_to_amt_sum
        from
            t_dd_response res
        left join temp_vendor_group vg on
            res.id_vendor = vg.id_vendor
        left join t_deduct_response dres on
            res.id_deduct_response = dres.id
        left join t_deduct_request dreq on
            dres.id_deduct_request = dreq.id
        left join temp_vendor_acct va on
            dreq.id_vendor_account = va.id_vendor_account
        where
            res.cdate >= %(start_date)s
            and res.cdate < %(end_date)s
            and res.return_code = '0000'
            and vg.vendor_group in ({channel_list_join_by_comma})
        group by
            vg.vendor_group,
            va.deduct_to
        order by vg.vendor_group,
            va.deduct_to;
        '''

sql_oracle_recon_template = '''
        SELECT
            b.CHANNEL_CODE AS vendor_group,
            b.HCC_ACCOUNT AS deduct_to_acct,
            sum(b.AMOUNT)*100 AS deduct_to_amt_sum
        FROM
            T_RECON_S_DETAIL_B b
        WHERE
            b.trade_time >= :start_date
            AND b.trade_time < :end_date
            AND b.CHANNEL_CODE in ({channel_list_join_by_comma})
        GROUP BY
            b.CHANNEL_CODE ,
            b.HCC_ACCOUNT
        ORDER BY
            b.CHANNEL_CODE ,
            b.HCC_ACCOUNT
        '''

sql_pg_recon_template = '''
        select
            case l.channel_group when 'WECHAT' then 'CAPP-WECHAT'
            else l.channel_group end as vendor_group,
            '12050183510000001896' as deduct_to_acct,
            sum(l.amount::integer) as deduct_to_amt_sum
        from
            app_recon.t_recon_src_detail_l l
        where
            l.trade_date_int = %(start_date)s
            and l.channel_group in ('WECHAT', 'ALIPAY')
        group by
            l.channel_group
        '''

channel_direct_linkage_vendor = "'ABCDD-CFC','CCB-OL','BOCDD-CFC','ICBCDD-CFC','ICBC-SZ'"
channel_non_direct_linkage_vendor = "'BAOFUDD-CFC','JDPAY','YINYIN-OL','EBUDD-CFC','PSBC-OL','CHINAPAY-SingleDD'"
channel_client_dd_vendor = "'CAPP-WECHAT','ALIPAY'"


def get_local_direct_linkage_vendor_sum(recon_date):
    channel_list_join_by_comma = channel_direct_linkage_vendor
    sql = sql_mysql_ssdd_template.replace('{channel_list_join_by_comma}', channel_list_join_by_comma)
    start_date = dt.datetime.strptime(recon_date, '%Y%m%d')
    end_date = start_date + dt.timedelta(days=1)
    sql_param_dict = {'start_date': start_date, 'end_date': end_date}
    return mysql_ssdd.execute_query_sql(sql, sql_param_dict)


def get_local_non_direct_linkage_vendor_sum(recon_date):
    channel_list_join_by_comma = channel_non_direct_linkage_vendor
    sql = sql_mysql_ssdd_template.replace('{channel_list_join_by_comma}', channel_list_join_by_comma)
    start_date = dt.datetime.strptime(recon_date, '%Y%m%d')
    end_date = start_date + dt.timedelta(days=1)
    sql_param_dict = {'start_date': start_date, 'end_date': end_date}
    return mysql_ssdd.execute_query_sql(sql, sql_param_dict)


from db_access import postgresql_paydb_recon


def get_local_client_dd_vendor_sum(recon_date):
    return postgresql_paydb_recon.execute_query_sql(sql_pg_recon_template, {'start_date': int(recon_date)})


def get_bank_direct_linkage_vendor_sum(recon_date):
    start_date = dt.datetime.strptime(recon_date, '%Y%m%d')
    end_date = start_date + dt.timedelta(days=1)
    channel_list_join_by_comma = channel_direct_linkage_vendor
    get_credit_bank_summary = sql_oracle_recon_template.replace('{channel_list_join_by_comma}',
                                                                channel_list_join_by_comma)
    sql_parameter_map = {'start_date': start_date, 'end_date': end_date}
    return oracle_paydb_recon.execute_query_sql(get_credit_bank_summary, sql_parameter_map)


def get_bank_non_direct_linkage_vendor_sum(recon_date):
    start_date = dt.datetime.strptime(recon_date, '%Y%m%d')
    end_date = start_date + dt.timedelta(days=1)
    channel_list_join_by_comma = channel_non_direct_linkage_vendor
    get_credit_bank_summary = sql_oracle_recon_template.replace('{channel_list_join_by_comma}',
                                                                channel_list_join_by_comma)
    sql_parameter_map = {'start_date': start_date, 'end_date': end_date}
    return oracle_paydb_recon.execute_query_sql(get_credit_bank_summary, sql_parameter_map)


def get_bank_client_dd_vendor_sum(recon_date):
    start_date = dt.datetime.strptime(recon_date, '%Y%m%d')
    end_date = start_date + dt.timedelta(days=1)
    channel_list_join_by_comma = channel_client_dd_vendor
    get_credit_bank_summary = sql_oracle_recon_template.replace('{channel_list_join_by_comma}',
                                                                channel_list_join_by_comma)
    sql_parameter_map = {'start_date': start_date, 'end_date': end_date}
    return oracle_paydb_recon.execute_query_sql(get_credit_bank_summary, sql_parameter_map)


def reconcile_local2bank_direct_linkage_vendor(recon_date):
    local_trade_sum_list = set(get_local_direct_linkage_vendor_sum(recon_date))
    bank_credit_sum_list = set(get_bank_direct_linkage_vendor_sum(recon_date))
    matched = local_trade_sum_list.intersection(bank_credit_sum_list)
    for a in sorted(matched):
        print("dl matched:", a, recon_date)
    unmatch_local = local_trade_sum_list.difference(bank_credit_sum_list)
    for b in sorted(unmatch_local):
        print("dl unmatch local:", b, recon_date)
    unmatch_bank = bank_credit_sum_list.difference(local_trade_sum_list)
    for c in sorted(unmatch_bank):
        print("dl unmatch  bank:", c, recon_date)
    return list(sorted(matched)), list(sorted(unmatch_local)), list(sorted(unmatch_bank))


def reconcile_local2bank_non_direct_linkage_vendor(recon_date):
    recon_date_obj = dt.datetime.strptime(recon_date, '%Y%m%d')
    t1_recon_date = recon_date_obj + dt.timedelta(days=1)
    t1_recon_date_str = t1_recon_date.strftime('%Y%m%d')
    local_trade_sum_list = set(get_local_non_direct_linkage_vendor_sum(recon_date))
    bank_credit_sum_list = set(get_bank_non_direct_linkage_vendor_sum(t1_recon_date_str))
    matched = local_trade_sum_list.intersection(bank_credit_sum_list)
    for a in sorted(matched):
        print("3th matched:", a, recon_date)
    unmatch_local = local_trade_sum_list.difference(bank_credit_sum_list)
    for b in sorted(unmatch_local):
        print("3th unmatch local:", b, recon_date)
    unmatch_bank = bank_credit_sum_list.difference(local_trade_sum_list)
    for c in sorted(unmatch_bank):
        print("3th unmatch  bank:", c, t1_recon_date_str)
    return list(sorted(matched)), list(sorted(unmatch_local)), list(sorted(unmatch_bank))


def reconcile_local2bank_client_dd_vendor(recon_date):
    recon_date_obj = dt.datetime.strptime(recon_date, '%Y%m%d')
    t1_recon_date = recon_date_obj + dt.timedelta(days=1)
    t1_recon_date_str = t1_recon_date.strftime('%Y%m%d')
    local_trade_sum_list = set(get_local_client_dd_vendor_sum(recon_date))
    bank_credit_sum_list = set(get_bank_client_dd_vendor_sum(t1_recon_date_str))
    matched = local_trade_sum_list.intersection(bank_credit_sum_list)
    for a in sorted(matched):
        print("client_dd matched:", a, recon_date)
    unmatch_local = local_trade_sum_list.difference(bank_credit_sum_list)
    for b in sorted(unmatch_local):
        print("client_dd unmatch local:", b, recon_date)
    unmatch_bank = bank_credit_sum_list.difference(local_trade_sum_list)
    for c in sorted(unmatch_bank):
        print("client_dd unmatch  bank:", c, t1_recon_date_str)
    return list(sorted(matched)), list(sorted(unmatch_local)), list(sorted(unmatch_bank))

def write_recon_local2bank_report(recon_date):
    with open(f"D:/data/channel-proxy/recon/bank/recon_local2bank_{recon_date}.txt", 'w', encoding='utf-8') as f:
        f.write("#########################################################################################\n")
        f.write("#### Direct Linkage Vendor Reconciliation  (T+0)          ###############################\n")
        f.write("#########################################################################################\n")
        dl_m, dl_um_local, dl_um_bank = reconcile_local2bank_direct_linkage_vendor(recon_date)
        f.write(f"---matched on {recon_date}-------------------------------------------------------------------\n")
        for a in dl_m:
            f.write(f"dl-matched:{recon_date},{a}\n")
        f.write(f"---matched on {recon_date}-------------------------------------------------------------------\n\n")
        f.write(f"---unmatched local on {recon_date}-----------------------------------------------------------\n")
        for b in dl_um_local:
            f.write(f"dl-unmatched local:{recon_date},{b}\n")
        f.write(f"---unmatched local on {recon_date}-----------------------------------------------------------\n\n")
        f.write(f"---unmatched bank on {recon_date}------------------------------------------------------------\n")
        for c in dl_um_bank:
            f.write(f"dl-unmatched bank:{recon_date},{c}\n")
        f.write(f"---unmatched bank on {recon_date}------------------------------------------------------------\n\n")
        f.write("#########################################################################################\n")
        f.write("#### 3th-part Vendor Reconciliation    (T+1..n)           ###############################\n")
        f.write("#########################################################################################\n")
        th3_m, th3_um_local, th3_um_bank = reconcile_local2bank_non_direct_linkage_vendor(recon_date)
        f.write(f"---matched on {recon_date}-------------------------------------------------------------------\n")
        for a in th3_m:
            f.write(f"3th-matched:{recon_date},{a}\n")
        f.write(f"---matched on {recon_date}-------------------------------------------------------------------\n\n")
        f.write(f"---unmatched local on {recon_date}-----------------------------------------------------------\n")
        for b in th3_um_local:
            f.write(f"3th-unmatched local:{recon_date},{b}\n")
        f.write(f"---unmatched local on {recon_date}-----------------------------------------------------------\n\n")
        f.write(f"---unmatched bank on {recon_date} + 1--------------------------------------------------------\n")
        for c in th3_um_bank:
            f.write(f"3th-unmatched bank:{recon_date} + 1,{c}\n")
        f.write(f"---unmatched bank on {recon_date} + 1--------------------------------------------------------\n\n")
        f.write("#########################################################################################\n")
        f.write("#### Client DD Vendor Reconciliation      (T+1)           ###############################\n")
        f.write("#########################################################################################\n")
        cd_m, cd_um_local, cd_um_bank = reconcile_local2bank_client_dd_vendor(recon_date)
        f.write(f"---matched on {recon_date}-------------------------------------------------------------------\n")
        for a in cd_m:
            f.write(f"cd-matched:{recon_date},{a}\n")
        f.write(f"---matched on {recon_date}-------------------------------------------------------------------\n\n")
        f.write(f"---unmatched local on {recon_date}------------------------------------------------------------\n")
        for b in cd_um_local:
            f.write(f"cd-unmatched local:{recon_date},{b}\n")
        f.write(f"---unmatched local on {recon_date}------------------------------------------------------------\n\n")
        f.write(f"---unmatched bank on {recon_date} + 1---------------------------------------------------------\n")
        for c in cd_um_bank:
            f.write(f"cd-unmatched bank:{recon_date} + 1,{c}\n")
        f.write(f"---unmatched bank on {recon_date} + 1---------------------------------------------------------\n\n")

if __name__ == '__main__':
    write_recon_local2bank_report('20240713')
    # for a in get_local_client_dd_vendor_sum('20240713'):
    #     print(a)
    # for lts in local_trade_sum_list:
    #     channel = lts[0]
    #     hcc_acct = lts[1]
    #     amt = int(lts[2])
    #     if(recon_match(lts, bank_credit_sum_list)):
    #         local_trade_sum_list.remove(lts)
    #
    # for a in local_trade_sum_list:
    #     print(f'unmatched local={a}')
    #
    # for b in bank_credit_sum_list:
    #     print(f'unmatched bank={b}')

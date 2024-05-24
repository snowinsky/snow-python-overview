from download_batch_file import downloadBatchResFile
from mark_batch_file import markBatchFile
from select_from_pg import selectFromPg
from select_from_mysql import selectFromMySql


def main():
    '''
    为了应对内审检查，一般需要根据内审人员提供的合同号和日期，查找当日的扣款记录
    然后下载对应扣款的回盘文件，并从回盘文件中挑选出对应的数据，然后对其他的敏感数据信息进行打星处理
    :return:
    '''
    print('请输入合同号：')
    contract_nbr = input()
    print('请输入审查日期(yyyyMMdd)：')
    audit_date = input()
    print('请输入审查金额:')
    audit_amt = input()

    print(f"您的输入是：合同={contract_nbr}, 日期={audit_date} 金额={audit_amt}")

    hasData, data = selectFromMySql(contract_nbr, audit_date)
    if not hasData:
        hasData, data = selectFromPg(contract_nbr, audit_date)

    if not hasData:
        print("没有找到数据，请手动处理。。。。")
        exit()

    data_dic_list = [{
        "contract_nbr": rec[0],
        "request_time": rec[1],
        "debit_amt": rec[2],
        "vendor_id": rec[3],
        "vendor_code": rec[4],
        "batch_name": rec[5],
        "batch_file_record_id": rec[6],
    } for rec in data]
    print("共找到 %s 条数据" % len(data_dic_list))

    print("分别针对每一条数据进行处理。。。。")
    for rec in data_dic_list:
        res_batch_file_path = downloadBatchResFile(rec['vendor_code'], rec['batch_name'])
        if not res_batch_file_path:
            print("下载回盘文件失败，请手动处理")
            exit()
        marked_res_batch_file_path = markBatchFile(res_batch_file_path, rec['batch_file_record_id'])
        if marked_res_batch_file_path:
            print("回盘文件下载并对敏感数据处理完毕", marked_res_batch_file_path)


if __name__ == '__main__':
    '''
    请输入合同号：
    3622868198006
    请输入审查日期(yyyyMMdd)：
    20240507
    请输入审查金额:
    0.82
    您的输入是：合同=3622868198006, 日期=20240507 金额=0.82
    找到数据如下 [('3622868198006', datetime.datetime(2024, 5, 7, 7, 30, 1), Decimal('82.00'), 6, 'ICBC', 'JX20240507500009', '109683695609', None)]
    
    Process finished with exit code 0
    '''
    main()

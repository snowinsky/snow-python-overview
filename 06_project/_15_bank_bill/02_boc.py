import requests
import xml.etree.ElementTree as ET

bank_acct_list = (
"320767651502", "320767666007", "325967635633", "327267633910", "327267638341", "332467663452", "333767648131",
"335067650536", "336367656155", "337667652776", "338967638037", "341567650156", "342867654823", "344167645195",
"345467660374", "336368244185", "341568240933", "335068239535", "346768240963", "349368242589", "332467032471")

custid = '28582807'
cusopr = '169111635'
trncod = 'b2e0035'

url = 'http://10.31.2.201:8080/B2EC/E2BServlet'


def get_bill(start_date, end_date, credit_acct):
    req_xml = f'''
        <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <bocb2e version="120" locale="zh_CN">
            <head>
                <custid>
                    {custid}
                </custid>
                <cusopr>
                    {cusopr}
                </cusopr>
                <trncod>
                    {trncod}
                </trncod>
            </head>
            <trans>
                <trn-b2e0035-rq>
                    <b2e0035-rq>
                        <actacn>
                            {credit_acct}
                        </actacn>
                        <type>
                            2002
                        </type>
                        <begnum>
                            1
                        </begnum>
                        <recnum>
                            50
                        </recnum>
                        <datescope>
                            <from>
                                {start_date}
                            </from>
                            <to>
                                {end_date}
                            </to>
                        </datescope>
                        <amountscope />
                        <direction>
                            1
                        </direction>
                    </b2e0035-rq>
                </trn-b2e0035-rq>
            </trans>
        </bocb2e>
    '''
    req_data = ''.join([a.strip() for a in req_xml.split('\n')])
    print('request=',req_data)
    res = requests.post(url, data=req_data)
    print('response=',res.text)


if __name__ == '__main__':
    for credit_acct in bank_acct_list:
        get_bill('20240511','20240511', credit_acct)


demo_res = '''
<?xml version="1.0" encoding="UTF-8"?>
<bocb2e version="120" locale="zh_CN">
	<head>
		<termid>
			E010031002201
		</termid>
		<custid>
			28582807
		</custid>
		<cusopr>
			169111635
		</cusopr>
		<trncod>
			b2e0035
		</trncod>
	</head>
	<trans>
		<trn-b2e0035-rs>
			<status>
				<rspcod>
					B001
				</rspcod>
				<rspmsg>
					ok
				</rspmsg>
			</status>
			<totalnum>
				14
			</totalnum>
			<notenum>
				14
			</notenum>
			<b2e0035-rs>
				<status>
					<rspcod>
						B001
					</rspcod>
					<rspmsg>
						ok
					</rspmsg>
				</status>
				<fractn>
					<ibknum>
					</ibknum>
					<actacn>
					</actacn>
					<acntname>
					</acntname>
					<ibkname>
					</ibkname>
					<outref>
					</outref>
				</fractn>
				<toactn>
					<toibkn>
						20142
					</toibkn>
					<actacn>
						342867654823
					</actacn>
					<toname>
						捷信消费金融有限公司
					</toname>
					<tobank>
						中国银行北京工体北路支行
					</tobank>
					<tobref>
						A1041805D12024051100001008
					</tobref>
				</toactn>
				<mactibkn>
				</mactibkn>
				<mactacn>
				</mactacn>
				<mactname>
				</mactname>
				<mactbank>
				</mactbank>
				<vchnum>
					32763554574
				</vchnum>
				<transid>
					032763554999851574999851574
				</transid>
				<insid>
					20240511_A00
				</insid>
				<txndate>
					20240511
				</txndate>
				<txntime>
					074245
				</txntime>
				<txnamt>
					150.00
				</txnamt>
				<acctbal>
					1055900.23
				</acctbal>
				<avlbal>
					1055900.23
				</avlbal>
				<frzamt>
					0.00
				</frzamt>
				<overdramt>
					0.00
				</overdramt>
				<avloverdramt>
					0.00
				</avloverdramt>
				<useinfo>
				</useinfo>
				<furinfo>
					OBSS050621393136GIRO20240511_A00
				</furinfo>
				<transtype>
					99
				</transtype>
				<bustype>
					8313
				</bustype>
				<trncur>
					CNY
				</trncur>
				<direction>
					1
				</direction>
				<feeact>
				</feeact>
				<feeamt>
				</feeamt>
				<feecur>
				</feecur>
				<valdat>
					20240511
				</valdat>
				<vouchtp>
				</vouchtp>
				<vouchnum>
				</vouchnum>
				<fxrate>
					1.000000
				</fxrate>
				<interinfo>
					F://A:OBSS050621393136GIRO20240511_A00//U://R:
				</interinfo>
				<channelflg>
					银企对接
				</channelflg>
				<commnum>
				</commnum>
				<reserve1>
					银企对接
				</reserve1>
				<reserve2>
					CTIS0000000034286765482320240511000032763554999851574999851574
				</reserve2>
				<reserve3>
				</reserve3>
				<reserve4>
				</reserve4>
			</b2e0035-rs>
			<b2e0035-rs>
				<status>
					<rspcod>
						B001
					</rspcod>
					<rspmsg>
						ok
					</rspmsg>
				</status>
				<fractn>
					<ibknum>
					</ibknum>
					<actacn>
					</actacn>
					<acntname>
					</acntname>
					<ibkname>
					</ibkname>
					<outref>
					</outref>
				</fractn>
				<toactn>
					<toibkn>
						20142
					</toibkn>
					<actacn>
						342867654823
					</actacn>
					<toname>
						捷信消费金融有限公司
					</toname>
					<tobank>
						中国银行北京工体北路支行
					</tobank>
					<tobref>
						A1041805D12024051100001029
					</tobref>
				</toactn>
				<mactibkn>
				</mactibkn>
				<mactacn>
				</mactacn>
				<mactname>
				</mactname>
				<mactbank>
				</mactbank>
				<vchnum>
					34710196572
				</vchnum>
				<transid>
					034710196999851572999851572
				</transid>
				<insid>
					20240511_A00
				</insid>
				<txndate>
					20240511
				</txndate>
				<txntime>
					075647
				</txntime>
				<txnamt>
					50.00
				</txnamt>
				<acctbal>
					1055950.23
				</acctbal>
				<avlbal>
					1055950.23
				</avlbal>
				<frzamt>
					0.00
				</frzamt>
				<overdramt>
					0.00
				</overdramt>
				<avloverdramt>
					0.00
				</avloverdramt>
				<useinfo>
				</useinfo>
				<furinfo>
					OBSS050621391431GIRO20240511_A00
				</furinfo>
				<transtype>
					99
				</transtype>
				<bustype>
					8313
				</bustype>
				<trncur>
					CNY
				</trncur>
				<direction>
					1
				</direction>
				<feeact>
				</feeact>
				<feeamt>
				</feeamt>
				<feecur>
				</feecur>
				<valdat>
					20240511
				</valdat>
				<vouchtp>
				</vouchtp>
				<vouchnum>
				</vouchnum>
				<fxrate>
					1.000000
				</fxrate>
				<interinfo>
					F://A:OBSS050621391431GIRO20240511_A00//U://R:
				</interinfo>
				<channelflg>
					银企对接
				</channelflg>
				<commnum>
				</commnum>
				<reserve1>
					银企对接
				</reserve1>
				<reserve2>
					CTIS0000000034286765482320240511000034710196999851572999851572
				</reserve2>
				<reserve3>
				</reserve3>
				<reserve4>
				</reserve4>
			</b2e0035-rs>
			<b2e0035-rs>
				<status>
					<rspcod>
						B001
					</rspcod>
					<rspmsg>
						ok
					</rspmsg>
				</status>
				<fractn>
					<ibknum>
					</ibknum>
					<actacn>
					</actacn>
					<acntname>
					</acntname>
					<ibkname>
					</ibkname>
					<outref>
					</outref>
				</fractn>
				<toactn>
					<toibkn>
						20142
					</toibkn>
					<actacn>
						342867654823
					</actacn>
					<toname>
						捷信消费金融有限公司
					</toname>
					<tobank>
						中国银行北京工体北路支行
					</tobank>
					<tobref>
						A1041805D12024051100001050
					</tobref>
				</toactn>
				<mactibkn>
				</mactibkn>
				<mactacn>
				</mactacn>
				<mactname>
				</mactname>
				<mactbank>
				</mactbank>
				<vchnum>
					36462873570
				</vchnum>
				<transid>
					036462873999851570999851570
				</transid>
				<insid>
					20240511_A00
				</insid>
				<txndate>
					20240511
				</txndate>
				<txntime>
					080649
				</txntime>
				<txnamt>
					100.00
				</txnamt>
				<acctbal>
					1056050.23
				</acctbal>
				<avlbal>
					1056050.23
				</avlbal>
				<frzamt>
					0.00
				</frzamt>
				<overdramt>
					0.00
				</overdramt>
				<avloverdramt>
					0.00
				</avloverdramt>
				<useinfo>
				</useinfo>
				<furinfo>
					OBSS050621391505GIRO20240511_A00
				</furinfo>
				<transtype>
					99
				</transtype>
				<bustype>
					8313
				</bustype>
				<trncur>
					CNY
				</trncur>
				<direction>
					1
				</direction>
				<feeact>
				</feeact>
				<feeamt>
				</feeamt>
				<feecur>
				</feecur>
				<valdat>
					20240511
				</valdat>
				<vouchtp>
				</vouchtp>
				<vouchnum>
				</vouchnum>
				<fxrate>
					1.000000
				</fxrate>
				<interinfo>
					F://A:OBSS050621391505GIRO20240511_A00//U://R:
				</interinfo>
				<channelflg>
					银企对接
				</channelflg>
				<commnum>
				</commnum>
				<reserve1>
					银企对接
				</reserve1>
				<reserve2>
					CTIS0000000034286765482320240511000036462873999851570999851570
				</reserve2>
				<reserve3>
				</reserve3>
				<reserve4>
				</reserve4>
			</b2e0035-rs>
			<b2e0035-rs>
				<status>
					<rspcod>
						B001
					</rspcod>
					<rspmsg>
						ok
					</rspmsg>
				</status>
				<fractn>
					<ibknum>
					</ibknum>
					<actacn>
					</actacn>
					<acntname>
					</acntname>
					<ibkname>
					</ibkname>
					<outref>
					</outref>
				</fractn>
				<toactn>
					<toibkn>
						20142
					</toibkn>
					<actacn>
						342867654823
					</actacn>
					<toname>
						捷信消费金融有限公司
					</toname>
					<tobank>
						中国银行北京工体北路支行
					</tobank>
					<tobref>
						A1041805D12024051100001159
					</tobref>
				</toactn>
				<mactibkn>
				</mactibkn>
				<mactacn>
				</mactacn>
				<mactname>
				</mactname>
				<mactbank>
				</mactbank>
				<vchnum>
					47095687568
				</vchnum>
				<transid>
					047095687999851568999851568
				</transid>
				<insid>
					20240511_A00
				</insid>
				<txndate>
					20240511
				</txndate>
				<txntime>
					085733
				</txntime>
				<txnamt>
					50.00
				</txnamt>
				<acctbal>
					1056100.23
				</acctbal>
				<avlbal>
					1056100.23
				</avlbal>
				<frzamt>
					0.00
				</frzamt>
				<overdramt>
					0.00
				</overdramt>
				<avloverdramt>
					0.00
				</avloverdramt>
				<useinfo>
				</useinfo>
				<furinfo>
					OBSS050621400339GIRO20240511_A00
				</furinfo>
				<transtype>
					99
				</transtype>
				<bustype>
					8313
				</bustype>
				<trncur>
					CNY
				</trncur>
				<direction>
					1
				</direction>
				<feeact>
				</feeact>
				<feeamt>
				</feeamt>
				<feecur>
				</feecur>
				<valdat>
					20240511
				</valdat>
				<vouchtp>
				</vouchtp>
				<vouchnum>
				</vouchnum>
				<fxrate>
					1.000000
				</fxrate>
				<interinfo>
					F://A:OBSS050621400339GIRO20240511_A00//U://R:
				</interinfo>
				<channelflg>
					银企对接
				</channelflg>
				<commnum>
				</commnum>
				<reserve1>
					银企对接
				</reserve1>
				<reserve2>
					CTIS0000000034286765482320240511000047095687999851568999851568
				</reserve2>
				<reserve3>
				</reserve3>
				<reserve4>
				</reserve4>
			</b2e0035-rs>
			<b2e0035-rs>
				<status>
					<rspcod>
						B001
					</rspcod>
					<rspmsg>
						ok
					</rspmsg>
				</status>
				<fractn>
					<ibknum>
					</ibknum>
					<actacn>
					</actacn>
					<acntname>
					</acntname>
					<ibkname>
					</ibkname>
					<outref>
					</outref>
				</fractn>
				<toactn>
					<toibkn>
						20142
					</toibkn>
					<actacn>
						342867654823
					</actacn>
					<toname>
						捷信消费金融有限公司
					</toname>
					<tobank>
						中国银行北京工体北路支行
					</tobank>
					<tobref>
						A1041805D12024051100001165
					</tobref>
				</toactn>
				<mactibkn>
				</mactibkn>
				<mactacn>
				</mactacn>
				<mactname>
				</mactname>
				<mactbank>
				</mactbank>
				<vchnum>
					48530096566
				</vchnum>
				<transid>
					048530096999851566999851566
				</transid>
				<insid>
					20240511_A00
				</insid>
				<txndate>
					20240511
				</txndate>
				<txntime>
					090335
				</txntime>
				<txnamt>
					299.75
				</txnamt>
				<acctbal>
					1056399.98
				</acctbal>
				<avlbal>
					1056399.98
				</avlbal>
				<frzamt>
					0.00
				</frzamt>
				<overdramt>
					0.00
				</overdramt>
				<avloverdramt>
					0.00
				</avloverdramt>
				<useinfo>
				</useinfo>
				<furinfo>
					OBSS050621400875GIRO20240511_A00
				</furinfo>
				<transtype>
					99
				</transtype>
				<bustype>
					8313
				</bustype>
				<trncur>
					CNY
				</trncur>
				<direction>
					1
				</direction>
				<feeact>
				</feeact>
				<feeamt>
				</feeamt>
				<feecur>
				</feecur>
				<valdat>
					20240511
				</valdat>
				<vouchtp>
				</vouchtp>
				<vouchnum>
				</vouchnum>
				<fxrate>
					1.000000
				</fxrate>
				<interinfo>
					F://A:OBSS050621400875GIRO20240511_A00//U://R:
				</interinfo>
				<channelflg>
					银企对接
				</channelflg>
				<commnum>
				</commnum>
				<reserve1>
					银企对接
				</reserve1>
				<reserve2>
					CTIS0000000034286765482320240511000048530096999851566999851566
				</reserve2>
				<reserve3>
				</reserve3>
				<reserve4>
				</reserve4>
			</b2e0035-rs>
			<b2e0035-rs>
				<status>
					<rspcod>
						B001
					</rspcod>
					<rspmsg>
						ok
					</rspmsg>
				</status>
				<fractn>
					<ibknum>
					</ibknum>
					<actacn>
					</actacn>
					<acntname>
					</acntname>
					<ibkname>
					</ibkname>
					<outref>
					</outref>
				</fractn>
				<toactn>
					<toibkn>
						20142
					</toibkn>
					<actacn>
						342867654823
					</actacn>
					<toname>
						捷信消费金融有限公司
					</toname>
					<tobank>
						中国银行北京工体北路支行
					</tobank>
					<tobref>
						A1041805D12024051100001170
					</tobref>
				</toactn>
				<mactibkn>
				</mactibkn>
				<mactacn>
				</mactacn>
				<mactname>
				</mactname>
				<mactbank>
				</mactbank>
				<vchnum>
					49808250564
				</vchnum>
				<transid>
					049808250999851564999851564
				</transid>
				<insid>
					20240511_A00
				</insid>
				<txndate>
					20240511
				</txndate>
				<txntime>
					090838
				</txntime>
				<txnamt>
					150.00
				</txnamt>
				<acctbal>
					1056549.98
				</acctbal>
				<avlbal>
					1056549.98
				</avlbal>
				<frzamt>
					0.00
				</frzamt>
				<overdramt>
					0.00
				</overdramt>
				<avloverdramt>
					0.00
				</avloverdramt>
				<useinfo>
				</useinfo>
				<furinfo>
					OBSS050621401508GIRO20240511_A00
				</furinfo>
				<transtype>
					99
				</transtype>
				<bustype>
					8313
				</bustype>
				<trncur>
					CNY
				</trncur>
				<direction>
					1
				</direction>
				<feeact>
				</feeact>
				<feeamt>
				</feeamt>
				<feecur>
				</feecur>
				<valdat>
					20240511
				</valdat>
				<vouchtp>
				</vouchtp>
				<vouchnum>
				</vouchnum>
				<fxrate>
					1.000000
				</fxrate>
				<interinfo>
					F://A:OBSS050621401508GIRO20240511_A00//U://R:
				</interinfo>
				<channelflg>
					银企对接
				</channelflg>
				<commnum>
				</commnum>
				<reserve1>
					银企对接
				</reserve1>
				<reserve2>
					CTIS0000000034286765482320240511000049808250999851564999851564
				</reserve2>
				<reserve3>
				</reserve3>
				<reserve4>
				</reserve4>
			</b2e0035-rs>
			<b2e0035-rs>
				<status>
					<rspcod>
						B001
					</rspcod>
					<rspmsg>
						ok
					</rspmsg>
				</status>
				<fractn>
					<ibknum>
					</ibknum>
					<actacn>
					</actacn>
					<acntname>
					</acntname>
					<ibkname>
					</ibkname>
					<outref>
					</outref>
				</fractn>
				<toactn>
					<toibkn>
						20142
					</toibkn>
					<actacn>
						342867654823
					</actacn>
					<toname>
						捷信消费金融有限公司
					</toname>
					<tobank>
						中国银行北京工体北路支行
					</tobank>
					<tobref>
						A1041805D12024051100001177
					</tobref>
				</toactn>
				<mactibkn>
				</mactibkn>
				<mactacn>
				</mactacn>
				<mactname>
				</mactname>
				<mactbank>
				</mactbank>
				<vchnum>
					50828525562
				</vchnum>
				<transid>
					050828525999851562999851562
				</transid>
				<insid>
					20240511_A00
				</insid>
				<txndate>
					20240511
				</txndate>
				<txntime>
					091240
				</txntime>
				<txnamt>
					100.00
				</txnamt>
				<acctbal>
					1056649.98
				</acctbal>
				<avlbal>
					1056649.98
				</avlbal>
				<frzamt>
					0.00
				</frzamt>
				<overdramt>
					0.00
				</overdramt>
				<avloverdramt>
					0.00
				</avloverdramt>
				<useinfo>
				</useinfo>
				<furinfo>
					OBSS050621404431GIRO20240511_A00
				</furinfo>
				<transtype>
					99
				</transtype>
				<bustype>
					8313
				</bustype>
				<trncur>
					CNY
				</trncur>
				<direction>
					1
				</direction>
				<feeact>
				</feeact>
				<feeamt>
				</feeamt>
				<feecur>
				</feecur>
				<valdat>
					20240511
				</valdat>
				<vouchtp>
				</vouchtp>
				<vouchnum>
				</vouchnum>
				<fxrate>
					1.000000
				</fxrate>
				<interinfo>
					F://A:OBSS050621404431GIRO20240511_A00//U://R:
				</interinfo>
				<channelflg>
					银企对接
				</channelflg>
				<commnum>
				</commnum>
				<reserve1>
					银企对接
				</reserve1>
				<reserve2>
					CTIS0000000034286765482320240511000050828525999851562999851562
				</reserve2>
				<reserve3>
				</reserve3>
				<reserve4>
				</reserve4>
			</b2e0035-rs>
			<b2e0035-rs>
				<status>
					<rspcod>
						B001
					</rspcod>
					<rspmsg>
						ok
					</rspmsg>
				</status>
				<fractn>
					<ibknum>
					</ibknum>
					<actacn>
					</actacn>
					<acntname>
					</acntname>
					<ibkname>
					</ibkname>
					<outref>
					</outref>
				</fractn>
				<toactn>
					<toibkn>
						20142
					</toibkn>
					<actacn>
						342867654823
					</actacn>
					<toname>
						捷信消费金融有限公司
					</toname>
					<tobank>
						中国银行北京工体北路支行
					</tobank>
					<tobref>
						A1041805D12024051100001181
					</tobref>
				</toactn>
				<mactibkn>
				</mactibkn>
				<mactacn>
				</mactacn>
				<mactname>
				</mactname>
				<mactbank>
				</mactbank>
				<vchnum>
					51451926560
				</vchnum>
				<transid>
					051451926999851560999851560
				</transid>
				<insid>
					20240511_A00
				</insid>
				<txndate>
					20240511
				</txndate>
				<txntime>
					091511
				</txntime>
				<txnamt>
					1024.06
				</txnamt>
				<acctbal>
					1057674.04
				</acctbal>
				<avlbal>
					1057674.04
				</avlbal>
				<frzamt>
					0.00
				</frzamt>
				<overdramt>
					0.00
				</overdramt>
				<avloverdramt>
					0.00
				</avloverdramt>
				<useinfo>
				</useinfo>
				<furinfo>
					OBSS050621403337GIRO20240511_A00
				</furinfo>
				<transtype>
					99
				</transtype>
				<bustype>
					8313
				</bustype>
				<trncur>
					CNY
				</trncur>
				<direction>
					1
				</direction>
				<feeact>
				</feeact>
				<feeamt>
				</feeamt>
				<feecur>
				</feecur>
				<valdat>
					20240511
				</valdat>
				<vouchtp>
				</vouchtp>
				<vouchnum>
				</vouchnum>
				<fxrate>
					1.000000
				</fxrate>
				<interinfo>
					F://A:OBSS050621403337GIRO20240511_A00//U://R:
				</interinfo>
				<channelflg>
					银企对接
				</channelflg>
				<commnum>
				</commnum>
				<reserve1>
					银企对接
				</reserve1>
				<reserve2>
					CTIS0000000034286765482320240511000051451926999851560999851560
				</reserve2>
				<reserve3>
				</reserve3>
				<reserve4>
				</reserve4>
			</b2e0035-rs>
			<b2e0035-rs>
				<status>
					<rspcod>
						B001
					</rspcod>
					<rspmsg>
						ok
					</rspmsg>
				</status>
				<fractn>
					<ibknum>
					</ibknum>
					<actacn>
					</actacn>
					<acntname>
					</acntname>
					<ibkname>
					</ibkname>
					<outref>
					</outref>
				</fractn>
				<toactn>
					<toibkn>
						20142
					</toibkn>
					<actacn>
						342867654823
					</actacn>
					<toname>
						捷信消费金融有限公司
					</toname>
					<tobank>
						中国银行北京工体北路支行
					</tobank>
					<tobref>
						A1041805D12024051100001188
					</tobref>
				</toactn>
				<mactibkn>
				</mactibkn>
				<mactacn>
				</mactacn>
				<mactname>
				</mactname>
				<mactbank>
				</mactbank>
				<vchnum>
					52569742558
				</vchnum>
				<transid>
					052569742999851558999851558
				</transid>
				<insid>
					20240511_A00
				</insid>
				<txndate>
					20240511
				</txndate>
				<txntime>
					091944
				</txntime>
				<txnamt>
					1139.72
				</txnamt>
				<acctbal>
					1058813.76
				</acctbal>
				<avlbal>
					1058813.76
				</avlbal>
				<frzamt>
					0.00
				</frzamt>
				<overdramt>
					0.00
				</overdramt>
				<avloverdramt>
					0.00
				</avloverdramt>
				<useinfo>
				</useinfo>
				<furinfo>
					OBSS050621403890GIRO20240511_A00
				</furinfo>
				<transtype>
					99
				</transtype>
				<bustype>
					8313
				</bustype>
				<trncur>
					CNY
				</trncur>
				<direction>
					1
				</direction>
				<feeact>
				</feeact>
				<feeamt>
				</feeamt>
				<feecur>
				</feecur>
				<valdat>
					20240511
				</valdat>
				<vouchtp>
				</vouchtp>
				<vouchnum>
				</vouchnum>
				<fxrate>
					1.000000
				</fxrate>
				<interinfo>
					F://A:OBSS050621403890GIRO20240511_A00//U://R:
				</interinfo>
				<channelflg>
					银企对接
				</channelflg>
				<commnum>
				</commnum>
				<reserve1>
					银企对接
				</reserve1>
				<reserve2>
					CTIS0000000034286765482320240511000052569742999851558999851558
				</reserve2>
				<reserve3>
				</reserve3>
				<reserve4>
				</reserve4>
			</b2e0035-rs>
			<b2e0035-rs>
				<status>
					<rspcod>
						B001
					</rspcod>
					<rspmsg>
						ok
					</rspmsg>
				</status>
				<fractn>
					<ibknum>
					</ibknum>
					<actacn>
					</actacn>
					<acntname>
					</acntname>
					<ibkname>
					</ibkname>
					<outref>
					</outref>
				</fractn>
				<toactn>
					<toibkn>
						20142
					</toibkn>
					<actacn>
						342867654823
					</actacn>
					<toname>
						捷信消费金融有限公司
					</toname>
					<tobank>
						中国银行北京工体北路支行
					</tobank>
					<tobref>
						A1041805D12024051100001203
					</tobref>
				</toactn>
				<mactibkn>
				</mactibkn>
				<mactacn>
				</mactacn>
				<mactname>
				</mactname>
				<mactbank>
				</mactbank>
				<vchnum>
					53183205556
				</vchnum>
				<transid>
					053183205999851556999851556
				</transid>
				<insid>
					20240511_A00
				</insid>
				<txndate>
					20240511
				</txndate>
				<txntime>
					092210
				</txntime>
				<txnamt>
					350.00
				</txnamt>
				<acctbal>
					1059163.76
				</acctbal>
				<avlbal>
					1059163.76
				</avlbal>
				<frzamt>
					0.00
				</frzamt>
				<overdramt>
					0.00
				</overdramt>
				<avloverdramt>
					0.00
				</avloverdramt>
				<useinfo>
				</useinfo>
				<furinfo>
					OBSS050621406800GIRO20240511_A00
				</furinfo>
				<transtype>
					99
				</transtype>
				<bustype>
					8313
				</bustype>
				<trncur>
					CNY
				</trncur>
				<direction>
					1
				</direction>
				<feeact>
				</feeact>
				<feeamt>
				</feeamt>
				<feecur>
				</feecur>
				<valdat>
					20240511
				</valdat>
				<vouchtp>
				</vouchtp>
				<vouchnum>
				</vouchnum>
				<fxrate>
					1.000000
				</fxrate>
				<interinfo>
					F://A:OBSS050621406800GIRO20240511_A00//U://R:
				</interinfo>
				<channelflg>
					银企对接
				</channelflg>
				<commnum>
				</commnum>
				<reserve1>
					银企对接
				</reserve1>
				<reserve2>
					CTIS0000000034286765482320240511000053183205999851556999851556
				</reserve2>
				<reserve3>
				</reserve3>
				<reserve4>
				</reserve4>
			</b2e0035-rs>
			<b2e0035-rs>
				<status>
					<rspcod>
						B001
					</rspcod>
					<rspmsg>
						ok
					</rspmsg>
				</status>
				<fractn>
					<ibknum>
					</ibknum>
					<actacn>
					</actacn>
					<acntname>
					</acntname>
					<ibkname>
					</ibkname>
					<outref>
					</outref>
				</fractn>
				<toactn>
					<toibkn>
						20142
					</toibkn>
					<actacn>
						342867654823
					</actacn>
					<toname>
						捷信消费金融有限公司
					</toname>
					<tobank>
						中国银行北京工体北路支行
					</tobank>
					<tobref>
						A1041805D12024051100001243
					</tobref>
				</toactn>
				<mactibkn>
				</mactibkn>
				<mactacn>
				</mactacn>
				<mactname>
				</mactname>
				<mactbank>
				</mactbank>
				<vchnum>
					58173080554
				</vchnum>
				<transid>
					058173080999851554999851554
				</transid>
				<insid>
					20240511_A00
				</insid>
				<txndate>
					20240511
				</txndate>
				<txntime>
					094221
				</txntime>
				<txnamt>
					200.00
				</txnamt>
				<acctbal>
					1059363.76
				</acctbal>
				<avlbal>
					1059363.76
				</avlbal>
				<frzamt>
					0.00
				</frzamt>
				<overdramt>
					0.00
				</overdramt>
				<avloverdramt>
					0.00
				</avloverdramt>
				<useinfo>
				</useinfo>
				<furinfo>
					OBSS050621414582GIRO20240511_A00
				</furinfo>
				<transtype>
					99
				</transtype>
				<bustype>
					8313
				</bustype>
				<trncur>
					CNY
				</trncur>
				<direction>
					1
				</direction>
				<feeact>
				</feeact>
				<feeamt>
				</feeamt>
				<feecur>
				</feecur>
				<valdat>
					20240511
				</valdat>
				<vouchtp>
				</vouchtp>
				<vouchnum>
				</vouchnum>
				<fxrate>
					1.000000
				</fxrate>
				<interinfo>
					F://A:OBSS050621414582GIRO20240511_A00//U://R:
				</interinfo>
				<channelflg>
					银企对接
				</channelflg>
				<commnum>
				</commnum>
				<reserve1>
					银企对接
				</reserve1>
				<reserve2>
					CTIS0000000034286765482320240511000058173080999851554999851554
				</reserve2>
				<reserve3>
				</reserve3>
				<reserve4>
				</reserve4>
			</b2e0035-rs>
			<b2e0035-rs>
				<status>
					<rspcod>
						B001
					</rspcod>
					<rspmsg>
						ok
					</rspmsg>
				</status>
				<fractn>
					<ibknum>
					</ibknum>
					<actacn>
					</actacn>
					<acntname>
					</acntname>
					<ibkname>
					</ibkname>
					<outref>
					</outref>
				</fractn>
				<toactn>
					<toibkn>
						20142
					</toibkn>
					<actacn>
						342867654823
					</actacn>
					<toname>
						捷信消费金融有限公司
					</toname>
					<tobank>
						中国银行北京工体北路支行
					</tobank>
					<tobref>
						A1041805D12024051100001244
					</tobref>
				</toactn>
				<mactibkn>
				</mactibkn>
				<mactacn>
				</mactacn>
				<mactname>
				</mactname>
				<mactbank>
				</mactbank>
				<vchnum>
					58314712552
				</vchnum>
				<transid>
					058314712999851552999851552
				</transid>
				<insid>
					20240511_A00
				</insid>
				<txndate>
					20240511
				</txndate>
				<txntime>
					094257
				</txntime>
				<txnamt>
					162.61
				</txnamt>
				<acctbal>
					1059526.37
				</acctbal>
				<avlbal>
					1059526.37
				</avlbal>
				<frzamt>
					0.00
				</frzamt>
				<overdramt>
					0.00
				</overdramt>
				<avloverdramt>
					0.00
				</avloverdramt>
				<useinfo>
				</useinfo>
				<furinfo>
					OBSS050621414633GIRO20240511_A00
				</furinfo>
				<transtype>
					99
				</transtype>
				<bustype>
					8313
				</bustype>
				<trncur>
					CNY
				</trncur>
				<direction>
					1
				</direction>
				<feeact>
				</feeact>
				<feeamt>
				</feeamt>
				<feecur>
				</feecur>
				<valdat>
					20240511
				</valdat>
				<vouchtp>
				</vouchtp>
				<vouchnum>
				</vouchnum>
				<fxrate>
					1.000000
				</fxrate>
				<interinfo>
					F://A:OBSS050621414633GIRO20240511_A00//U://R:
				</interinfo>
				<channelflg>
					银企对接
				</channelflg>
				<commnum>
				</commnum>
				<reserve1>
					银企对接
				</reserve1>
				<reserve2>
					CTIS0000000034286765482320240511000058314712999851552999851552
				</reserve2>
				<reserve3>
				</reserve3>
				<reserve4>
				</reserve4>
			</b2e0035-rs>
			<b2e0035-rs>
				<status>
					<rspcod>
						B001
					</rspcod>
					<rspmsg>
						ok
					</rspmsg>
				</status>
				<fractn>
					<ibknum>
					</ibknum>
					<actacn>
					</actacn>
					<acntname>
					</acntname>
					<ibkname>
					</ibkname>
					<outref>
					</outref>
				</fractn>
				<toactn>
					<toibkn>
						20142
					</toibkn>
					<actacn>
						342867654823
					</actacn>
					<toname>
						捷信消费金融有限公司
					</toname>
					<tobank>
						中国银行北京工体北路支行
					</tobank>
					<tobref>
						A1041805D12024051100001261
					</tobref>
				</toactn>
				<mactibkn>
				</mactibkn>
				<mactacn>
				</mactacn>
				<mactname>
				</mactname>
				<mactbank>
				</mactbank>
				<vchnum>
					59400177550
				</vchnum>
				<transid>
					059400177999851550999851550
				</transid>
				<insid>
					20240511_A00
				</insid>
				<txndate>
					20240511
				</txndate>
				<txntime>
					094724
				</txntime>
				<txnamt>
					150.00
				</txnamt>
				<acctbal>
					1059676.37
				</acctbal>
				<avlbal>
					1059676.37
				</avlbal>
				<frzamt>
					0.00
				</frzamt>
				<overdramt>
					0.00
				</overdramt>
				<avloverdramt>
					0.00
				</avloverdramt>
				<useinfo>
				</useinfo>
				<furinfo>
					OBSS050621413933GIRO20240511_A00
				</furinfo>
				<transtype>
					99
				</transtype>
				<bustype>
					8313
				</bustype>
				<trncur>
					CNY
				</trncur>
				<direction>
					1
				</direction>
				<feeact>
				</feeact>
				<feeamt>
				</feeamt>
				<feecur>
				</feecur>
				<valdat>
					20240511
				</valdat>
				<vouchtp>
				</vouchtp>
				<vouchnum>
				</vouchnum>
				<fxrate>
					1.000000
				</fxrate>
				<interinfo>
					F://A:OBSS050621413933GIRO20240511_A00//U://R:
				</interinfo>
				<channelflg>
					银企对接
				</channelflg>
				<commnum>
				</commnum>
				<reserve1>
					银企对接
				</reserve1>
				<reserve2>
					CTIS0000000034286765482320240511000059400177999851550999851550
				</reserve2>
				<reserve3>
				</reserve3>
				<reserve4>
				</reserve4>
			</b2e0035-rs>
			<b2e0035-rs>
				<status>
					<rspcod>
						B001
					</rspcod>
					<rspmsg>
						ok
					</rspmsg>
				</status>
				<fractn>
					<ibknum>
					</ibknum>
					<actacn>
					</actacn>
					<acntname>
					</acntname>
					<ibkname>
					</ibkname>
					<outref>
					</outref>
				</fractn>
				<toactn>
					<toibkn>
						20142
					</toibkn>
					<actacn>
						342867654823
					</actacn>
					<toname>
						捷信消费金融有限公司
					</toname>
					<tobank>
						中国银行北京工体北路支行
					</tobank>
					<tobref>
						A1041805D12024051100001441
					</tobref>
				</toactn>
				<mactibkn>
				</mactibkn>
				<mactacn>
				</mactacn>
				<mactname>
				</mactname>
				<mactbank>
				</mactbank>
				<vchnum>
					116702771548
				</vchnum>
				<transid>
					116702771999851548999851548
				</transid>
				<insid>
					20240511_A00
				</insid>
				<txndate>
					20240511
				</txndate>
				<txntime>
					141805
				</txntime>
				<txnamt>
					2137.86
				</txnamt>
				<acctbal>
					1061814.23
				</acctbal>
				<avlbal>
					1061814.23
				</avlbal>
				<frzamt>
					0.00
				</frzamt>
				<overdramt>
					0.00
				</overdramt>
				<avloverdramt>
					0.00
				</avloverdramt>
				<useinfo>
				</useinfo>
				<furinfo>
					OBSS050621505323GIRO20240511_A00
				</furinfo>
				<transtype>
					99
				</transtype>
				<bustype>
					8313
				</bustype>
				<trncur>
					CNY
				</trncur>
				<direction>
					1
				</direction>
				<feeact>
				</feeact>
				<feeamt>
				</feeamt>
				<feecur>
				</feecur>
				<valdat>
					20240511
				</valdat>
				<vouchtp>
				</vouchtp>
				<vouchnum>
				</vouchnum>
				<fxrate>
					1.000000
				</fxrate>
				<interinfo>
					F://A:OBSS050621505323GIRO20240511_A00//U://R:
				</interinfo>
				<channelflg>
					银企对接
				</channelflg>
				<commnum>
				</commnum>
				<reserve1>
					银企对接
				</reserve1>
				<reserve2>
					CTIS0000000034286765482320240511000116702771999851548999851548
				</reserve2>
				<reserve3>
				</reserve3>
				<reserve4>
				</reserve4>
			</b2e0035-rs>
		</trn-b2e0035-rs>
	</trans>
</bocb2e>
'''
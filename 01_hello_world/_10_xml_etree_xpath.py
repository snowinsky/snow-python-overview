import xml.etree.ElementTree as ET

xml_string = '''
        <ap>
          <RespSource>0</RespSource>
          <RespCode>0000</RespCode>
          <RespInfo>交易成功</RespInfo>
          <RxtInfo></RxtInfo>
          <RespSeqNo>672069097948</RespSeqNo>
          <Cmp>
            <BatchFileName>TBANK.2594.6612502044205888.67206909794815381504-D-017</BatchFileName>
            <RespPrvData></RespPrvData>
            <ContFlg></ContFlg>
            <BankNo>021900</BankNo>
            <DbProv>02</DbProv>
            <DbAccNo>02190001040018804</DbAccNo>
            <DbCur>CNY</DbCur>
            <QueryCnt>10</QueryCnt>
            <ContFlag>0</ContFlag>
          </Cmp>
          <Cme>
            <RecordNum>4</RecordNum>
            <FieldNum>35</FieldNum>
          </Cme>
          <FileFlag>1</FileFlag>
          <RespDate>20240613</RespDate>
          <RespTime>144633</RespTime>
          <TransCode>CQRA18</TransCode>
          <Version>
            <UpdateFlag>1</UpdateFlag>
          </Version>
          <Channel>
            <AccDate>20240613</AccDate>
            <JrnNo></JrnNo>
            <VchNo>0</VchNo>
            <RespInfo>交易成功</RespInfo>
            <RxtInfo>交易成功</RxtInfo>
            <AbisRespCode>0000</AbisRespCode>
          </Channel>
          <Corp>
            <CshDraFlag>0</CshDraFlag>
            <DbAccName>捷信消费金融有限公司</DbAccName>
            <DbBankName>中国农业银行股份有限公司天津南开支行</DbBankName>
          </Corp>
        </ap>
        '''

def xpath_etree(xml_str):
    root = ET.fromstring(xml_str)
    print(root.findall('.'))
    print(root.findall('./Cmp'))
    print(root.findall('./Cmp/BatchFileName')[0].text)

if __name__ == '__main__':
    xpath_etree(xml_string)

import requests
import xml.etree.ElementTree as ET

cmb_bank_acct = '''
152	CMB	122903873910269	22
153	CMB	122903873910346	22
154	CMB	122903873910363	22
155	CMB	122903873910377	22
156	CMB	122903873910437	22
157	CMB	122903873910440	22
158	CMB	122903873910454	22
159	CMB	122903873910468	22
160	CMB	122903873910545	22
161	CMB	122903873910559	22
162	CMB	122903873910562	22
163	CMB	122903873910758	22
164	CMB	122903873910761	22
165	CMB	122903873910866	22
166	CMB	122903873910943	22
167	CMB	122903873910957	22
168	CMB	122903873910960	22
169	CMB	122903873910499	22
170	CMB	122903873910203	22
171	CMB	122903873910402	22
172	CMB	122903873910601	22
173	CMB	122903873910507	22
174	CMB	122903873910615	22
175	CMB	122903873910922	22
176	CMB	122903873910416	22
177	CMB	122903873910723	22
178	CMB	122903873910919	22
179	CMB	122903873910220	22
180	CMB	122903873910905	22
26	CMB	122903873910626	75
27	CMB	122903873910653	22
28	CMB	122903873910717	22
29	CMB	122903873910720	22
30	CMB	122903873910181	22
31	CMB	122903873910195	22
32	CMB	122903873910238	22
33	CMB	122903873910706	22
34	CMB	122903873910112	22
35	CMB	122903873910828	22
36	CMB	122903873910524	22
37	CMB	122903873910325	22
38	CMB	122903873910632	22
39	CMB	122903873910106	75
40	CMB	122903873910123	75
41	CMB	122903873910305	75
42	CMB	122903873910319	75
43	CMB	122903873910322	75
44	CMB	122903873910427	75
45	CMB	122903873910504	75
46	CMB	122903873910518	75
47	CMB	122903873910521	75
48	CMB	122903873910609	75
49	CMB	122903873910703	75
50	CMB	122903873910808	75
51	CMB	122903873910102	22
52	CMB	122903873910207	22
53	CMB	122903873910301	22
54	CMB	122903873910406	22
55	CMB	122903873910605	22
56	CMB	122903873910804	22
57	CMB	122903873910902	22
58	CMB	122903873910137	22
59	CMB	122903873910140	22
60	CMB	122903873910185	22
61	CMB	122903873910168	22
62	CMB	122903873910171	22
63	CMB	122903873910228	22
64	CMB	122903873910231	22
65	CMB	122903873910245	22
66	CMB	122903873910259	22
67	CMB	122903873910262	22
68	CMB	122903873910276	22
69	CMB	122903873910336	22
70	CMB	122903873910353	22
71	CMB	122903873910367	22
72	CMB	122903873910370	22
73	CMB	122903873910384	22
74	CMB	122903873910430	22
75	CMB	122903873910444	22
76	CMB	122903873910458	22
77	CMB	122903873910461	22
78	CMB	122903873910475	22
79	CMB	122903873910535	22
80	CMB	122903873910549	22
81	CMB	122903873910552	22
82	CMB	122903873910566	22
83	CMB	122903873910643	22
84	CMB	122903873910657	22
85	CMB	122903873910660	22
86	CMB	122903873910674	22
87	CMB	122903873910734	22
88	CMB	122903873910748	22
89	CMB	122903873910751	22
90	CMB	122903873910765	22
91	CMB	122903873910779	22
92	CMB	122903873910782	22
93	CMB	122903873910839	22
94	CMB	122903873910842	22
95	CMB	122903873910856	22
96	CMB	122903873910873	22
97	CMB	122903873910887	22
98	CMB	122903873910933	22
99	CMB	122903873910947	22
100	CMB	122903873910950	22
101	CMB	122903873910964	22
102	CMB	122903873910978	22
103	CMB	122903873910981	22
104	CMB	122903873910154	22
105	CMB	122903873910214	22
106	CMB	122903873910413	22
107	CMB	122903873910612	22
108	CMB	122903873910811	22
109	CMB	122903873910825	22
110	CMB	122903873910916	22
111	CMB	122903873910583	22
112	CMB	122903873910116	22
113	CMB	122903873910199	22
114	CMB	122903873910210	22
115	CMB	122903873910315	22
116	CMB	122903873910500	22
117	CMB	122903873910514	22
118	CMB	122903873910713	22
119	CMB	122903873910818	22
120	CMB	122903873910909	22
121	CMB	122903873910912	22
122	CMB	122903873910133	22
123	CMB	122903873910224	22
124	CMB	122903873910329	22
125	CMB	122903873910332	22
126	CMB	122903873910423	22
127	CMB	122903873910531	22
128	CMB	122903873910619	22
129	CMB	122903873910622	22
130	CMB	122903873910636	22
131	CMB	122903873910727	22
132	CMB	122903873910730	22
133	CMB	122903873910835	22
134	CMB	122903873910926	22
135	CMB	122903873910380	22
136	CMB	122903873910576	22
137	CMB	122903873910394	22
138	CMB	122903873910485	22
139	CMB	122903873910593	22
140	CMB	122903873910684	22
141	CMB	122903873910698	22
142	CMB	122903873910792	22
143	CMB	122903873910897	22
144	CMB	122903873910988	22
145	CMB	122903873910670	22
146	CMB	122903873910471	22
147	CMB	122903873910147	22
148	CMB	122903873910150	22
149	CMB	122903873910164	22
150	CMB	122903873910241	22
151	CMB	122903873910255	22
'''

req_xml = '''
            <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
            <CMBSDKPGK>
                <INFO>
                    <FUNNAM>
                        GetTransInfo
                    </FUNNAM>
                    <DATTYP>
                        2
                    </DATTYP>
                    <LGNNAM>
                        N034346696
                    </LGNNAM>
                </INFO>
                <SDKTSINFX>
                    <BBKNBR>
                        22
                    </BBKNBR>
                    <ACCNBR>
                        122903873910545
                    </ACCNBR>
                    <BGNDAT>
                        20240612
                    </BGNDAT>
                    <ENDDAT>
                        20240612
                    </ENDDAT>
                </SDKTSINFX>
            </CMBSDKPGK>
'''

cmb_url = 'http://10.25.2.222:1080'
cmb_op_name = 'N034346696'


def get_bill(start_date, end_date, bank_acct, bank_no):
    req_data = f'{req_xml}'
    req_data = ''.join([a.strip() for a in req_data.split('\n')])
    # print('request=', req_data)
    res = requests.post(cmb_url, data=req_data)
    print("#########################\n\n\n")
    print(res.text)
    res_xml = ET.fromstring(res.text)
    res_ret_code = res_xml.findall('./INFO/RETCOD')[0].text
    res_ret_detail_list = res_xml.findall('./NTQTSINFZ')
    print(res_ret_code, len(res_ret_detail_list))

if __name__ == '__main__':
    acct_and_no = [(a.expandtabs(2)[8:22], a.expandtabs(2)[24:26]) for a in cmb_bank_acct.split('\n')]
    for a_n in acct_and_no:
        get_bill('20240501', '20240601', a_n[0], a_n[1])
    # get_bill('20240511', '20240511', '122903873910545', '22')

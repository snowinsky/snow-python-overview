import os
from batch_res_send_to_rabbitmq import send_res_json_to_router
from select_batch_res_from_mysql import selectFromMySql
import re
from datetime import datetime as dt

if __name__ == '__main__':
    with open("批量.txt", 'r', 1024) as f:
        for line in f:
            request_id = re.sub(r'\n','', line)
            has_date, rows = selectFromMySql(request_id, '20240527')
            if has_date:
                row_list = [{"requestId": row[2],
                   "responseTime": dt.strftime(row[3], '%Y-%m-%d %H:%M:%S'),
                   "returnCode": row[4],
                   "returnInfo": row[5],
                   "vendorRequestId": row[6],
                   "vendorRequestTime": dt.strftime(row[7], '%Y-%m-%d %H:%M:%S'),
                   "vendorResponseId": row[8],
                   "vendorResponseTime": dt.strftime(row[9], '%Y-%m-%d %H:%M:%S'),
                   "debitedAmount": str(row[10]),
                   "batchFileUrl": row[11],
                   "batchFileName": row[12],
                   "matchingResult": row[13],
                   "vendorResponseSettlementId": ''} for row in rows]
                send_res_json_to_router(row_list)

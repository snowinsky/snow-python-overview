import os
import re

re_id_card = "(\\D)(\\d{6})([19,20]\\d{7})(\\d{3}[0-9Xx])(\\D)"
re_bank_acct = "(\\D)([3-6]\\d{3})(\\d{8,12})(\\d{4})(\\D)"
re_phone = "(\\D)([13,14,15,16,17,18,19]\\d{2})(\\d{4})(\\d{4})(\\D)"
re_chinese_name = "(\\D)([\\u9FA6-\\u9FCB\\u3400-\\u4DB5\\u4E00-\\u9FA5]{2,10}([\\u25CF\\u00B7]{0,1}[\\u9FA6-\\u9FCB\\u3400-\\u4DB5\\u4E00-\\u9FA5]{2,10}){0,1})(\\D)"

mark_id_card = "$1$2********$4$5"
mark_bank_acct = "$1$2********$4$5"
mark_phone = "$1$2****$4$5"


def markLine(line):
    line = searchAndStarMark(line, re_id_card)
    line = searchAndStarMark(line, re_bank_acct)
    line = searchAndStarMark(line, re_phone)
    return line


def searchAndStarMark(text, regex):
    search_result = re.search(r'' + regex, text)
    if search_result:
        if len(search_result.groups()) == 5:
            replace_str = (search_result.group(1)
                           + search_result.group(2)
                           + '*' * len(search_result.group(3))
                           + search_result.group(4)
                           + search_result.group(5))
            id_list = re.sub(r'' + regex, replace_str, text)
            return id_list
    else:
        return text



def markBatchFile(batch_file, find_key):
    if not os.path.exists(batch_file):
        return None

    if os.path.exists(batch_file + "_marked"):
        os.remove(batch_file + "_marked")
    wf = open(batch_file + "_marked", 'w')

    with open(batch_file, 'r') as rf:
        for line in rf:
            if 'not found' in line:
                print("下载文件为空，或者没找到对应的文件，请手动处理")
                return None
            if find_key in line:
                marked_line = markLine(line)
                wf.write(marked_line)
            else:
                ignore_line = "*"*len(line)
                wf.write(ignore_line)
        wf.flush()
        wf.close()
    return batch_file + "_marked"


if __name__ == '__main__':
    # markBatchFile("D:\\doc\\audit\\202406\\2024-05-23\\XXCCB2024052300000057-120138127.res", '109710420725')
    markLine(
        "1|6217000830001384498|马忠春|3016.11|0.00|0|||||直连客户代收专用|109710420725||失败|账务交易失败:可用余额为零，不允许支取|YBLA01826406|13925468745|")

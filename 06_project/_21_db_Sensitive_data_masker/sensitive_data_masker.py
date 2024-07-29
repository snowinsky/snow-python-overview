import oracle_homerdb_uat as dao


digit_mark = {'0':'4','1':'5','2':'6','3':'7','4':'8','5':'9','6':'0','7':'1','8':'2','9':'3'}

digit_unmark = {'4':'0','5':'1','6':'2','7':'3','8':'4','9':'5','0':'6','1':'7','2':'8','3':'9'}

def maskBankAccountNumber(bank_acct_nbr:str)->str:
    if len(bank_acct_nbr) > 4:
        aa = bank_acct_nbr[0:-4]
        bb = bank_acct_nbr[-4:]
        return aa + ''.join([digit_mark[b] for a,b in enumerate(bb)])
    else:
        return bank_acct_nbr

def unmaskBankAccountNumber(bank_acct_nbr:str)->str:
    if len(bank_acct_nbr) > 4:
        aa = bank_acct_nbr[0:-4]
        bb = bank_acct_nbr[-4:]
        return aa + ''.join([digit_unmark[b] for a,b in enumerate(bb)])
    else:
        return bank_acct_nbr



def performBankAccountNameInBaTable():
    dao.execute_update_sql("update bank_account ba set ba.bank_account_name = (select p.name2 from person p where p.id = ba.id_person)", None);

def performBankAccountNumberInBaTable():
    l = dao.execute_query_sql('select ba.id, ba.bank_account_number from bank_account ba where  length(ba.bank_account_number) > 4', None)
    dao.batch_execute_update_sql('update bank_account set bank_account_number = :new_v where id = :id', [(maskBankAccountNumber(a[1]), a[0]) for a in l])


def performPhoneInBaTable():
    l = dao.execute_query_sql(
        '''select ba.id, ba.bank_reservation_phone_number
                  from bank_account ba
                 where length(ba.bank_reservation_phone_number) > 4''', None)
    # print([(maskBankAccountNumber(a[1]), a[0]) for a in l])
    dao.batch_execute_update_sql('update bank_account set bank_reservation_phone_number = :new_v where id = :id',
                                 [(maskBankAccountNumber(a[1]), a[0]) for a in l])

def performBankAccountNumberInAuthTable():
    l = dao.execute_query_sql(
        '''select baa.id, baa.bank_account_number
                  from bank_account_authorization baa
                 where length(baa.bank_account_number) > 4''', None)
    # print([(maskBankAccountNumber(a[1]), a[0]) for a in l])
    dao.batch_execute_update_sql('update bank_account_authorization set bank_account_number = :new_v where id = :id',
                                 [(maskBankAccountNumber(a[1]), a[0]) for a in l])
def mark_mini_plum():
    performBankAccountNameInBaTable()
    performBankAccountNumberInBaTable()
    performPhoneInBaTable()
    performBankAccountNumberInAuthTable()


if __name__ == '__main__':
    # print(performBankAccountNameInBaTable())
    # performBankAccountNumberInBaTable()
    # performPhoneInBaTable()
    # performBankAccountNumberInAuthTable()
    pass

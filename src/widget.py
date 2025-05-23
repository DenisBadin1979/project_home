from typing import Union
from masks import det_masks_card_number
from masks import get_masks_account

def mask_account_card(account_card: Union[str]) -> Union[str]:
    num = ""
    nam = ""
    for i in account_card:
        if i.isdigit():
            num += i
        elif i.isalpha():
            nam +=i
    if nam == "Счет":
        return nam + " " + get_masks_account(num)
    else:
        return nam + " " + det_masks_card_number(num)

def get_date (account_date: Union[str]) -> Union[str]:
    dat_acc = ''
    for i_d in range(10):
        dat_acc += account_date[i_d]
    new_dat_acc = dat_acc.split("-")
    new_dat_acc.reverse()
    return ".".join(new_dat_acc)




# print (mask_account_card('Maestro 1596837868705199'))
# print (mask_account_card('Счет 64686473678894779589'))
# print (mask_account_card('MasterCard 7158300734726758'))
# print (mask_account_card('Счет 35383033474447895560'))
# print (mask_account_card('Visa Classic 6831982476737658'))
# print (mask_account_card('Visa Platinum 8990922113665229'))
# print (mask_account_card('Visa Gold 5999414228426353'))
# print (mask_account_card('Счет 73654108430135874305'))
#
# print (get_date('2024-03-11T02:26:18.671407'))




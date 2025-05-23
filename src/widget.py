from dataclasses import replace
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








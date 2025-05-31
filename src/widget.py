from typing import Union

from src.masks import det_masks_card_number, get_masks_account


def mask_account_card(account_card: Union[str]) -> Union[str]:
    """Функция маскировки счета или карты"""
    num = ""
    nam = ""
    for i in account_card:
        if i.isdigit():
            num += i
        elif i.isalpha():
            nam += i
    if nam == "Счет":
        return f"{nam} {get_masks_account(num)}"
    else:
        return f"{nam} {det_masks_card_number(num)}"


def get_date(account_date: Union[str]) -> Union[str]:
    """Функция преобразует входящуюю дату в формат хх.хх.хххх"""
    dat_acc = ""
    for i_d in range(10):
        dat_acc += account_date[i_d]
    new_dat_acc = dat_acc.split("-")
    new_dat_acc.reverse()
    return ".".join(new_dat_acc)

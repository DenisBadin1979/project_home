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




def get_date(date_time: str) -> str:
    """
    Функция принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """
    times = date_time[:date_time.find("T")].split("-")
    return ".".join(times)

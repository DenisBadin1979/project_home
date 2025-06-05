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
    if nam == "Счет" and len(num) == 20:
        return f"{nam} {get_masks_account(num)}"
    elif len(num) == 16 and account_card[-16:].isdigit():
        # type_card = account_card[:-16]
        # number_card = account_card[-16:]
        return f"{nam} {det_masks_card_number(num)}"
    else:
        return "неверно указан номер"


# def get_date(account_date: Union[str]) -> Union[str]:
#     """Функция преобразует входящуюю дату в формат хх.хх.хххх"""
#     dat_acc = ""
#     for i_d in range(10):
#         dat_acc += account_date[i_d]
#     new_dat_acc = dat_acc.split("-")
#     new_dat_acc.reverse()
#     return ".".join(new_dat_acc)


def get_date(date_time: str) -> str:
    """
    Функция принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """
    if "T" in date_time and len(date_time) > 11:
        times = date_time[: date_time.find("T")].split("-")
        times.reverse()
        return ".".join(times)
    else:
        return "Неверный формат даты"

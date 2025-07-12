import logging
from typing import Union

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(r"D:/mypython/Personal_account/logs/maskslog.log", "w", "utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def det_masks_card_number(card_number: Union[str]) -> Union[str]:
    """Функция маскировки номера банковской карты"""
    logger.info("Запущена функция")
    card_list = []
    if len(card_number) == 16 and card_number.isdigit():
        for i in card_number:
            card_list.append(i)

        for i_d in range(len(card_list)):
            if 6 <= i_d <= 11:
                card_list[i_d] = "X"

        card_list.insert(4, " ")
        card_list.insert(9, " ")
        card_list.insert(14, " ")
        logger.info("номер карты замаскирован")
        return "".join(card_list)
    else:
        logger.error("неверно задан номер карты")
        return "неверно указан номер"


def get_masks_account(account: Union[str]) -> Union[str]:
    """Функция маскировки номера банковского счета"""
    logger.info("Запущена функция маскировки банковского счета")
    account_list = []
    if len(account) == 20 and account.isdigit():
        for i in account:
            account_list.append(i)

        for i_d in range(14):
            del account_list[0]

        account_list[0] = "X"
        account_list[1] = "X"
        logger.info("номер счета замаскирован")
        return "".join(account_list)
    else:
        logger.error("неверно задан номер счета")
        return "неверно указан номер"


print(det_masks_card_number("1111111111111111"))

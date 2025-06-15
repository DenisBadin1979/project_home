from typing import Union


def det_masks_card_number(card_number: Union[str]) -> Union[str]:
    """Функция маскировки номера банковской карты"""
    card_list = []
    if len(card_number) == 16 and card_number.isdigit() == True:
        for i in card_number:
            card_list.append(i)

        for i_d in range(len(card_list)):
            if 6 <= i_d <= 11:
                card_list[i_d] = "X"

        card_list.insert(4, " ")
        card_list.insert(9, " ")
        card_list.insert(14, " ")

        return "".join(card_list)
    else:
        return "неверно указан номер"


def get_masks_account(account: Union[str]) -> Union[str]:
    """Функция маскировки номера банковского счета"""
    account_list = []
    if len(account) == 20 and account.isdigit() == True:
        for i in account:
            account_list.append(i)

        for i_d in range(14):
            del account_list[0]

        account_list[0] = "X"
        account_list[1] = "X"

        return "".join(account_list)
    else:
        return "неверно указан номер"

from typing import Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator:
    """Функция принимает на вход список словарей, представляющих транзакции и возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    for operation in transactions:
        if operation["operationAmount"]["currency"]["code"] == currency:
            yield operation


def transaction_descriptions(transactions: list[dict]) -> Generator:
    """Функция принимает на вход список словарей, представляющих транзакции и возвращает описание каждой
    операции по очереди"""
    for operation in transactions:
        yield operation["description"]


def card_number_generator(start: int, end: int) -> Generator:
    """Функция запускает генератор по формированию номеров карт"""
    for card_i in range(start, end + 1):
        card_num = []
        number = str(card_i).zfill(16)
        for i in range(0, 16, 4):
            card_num.append(number[i : i + 4])
        yield " ".join(card_num)

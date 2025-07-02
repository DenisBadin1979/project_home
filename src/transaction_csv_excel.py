import csv

import pandas as pd


def reader_transaction_csv(file_path: str) -> list[dict]:
    """Принимает на данные с транзакциями в формате CSV  и возвращает список словарей"""
    try:
        with open(file_path) as transaction:
            transaction_csv = list(csv.DictReader(transaction, delimiter=";"))
        return transaction_csv
    except FileNotFoundError:
        raise FileNotFoundError(f"По заданному пути {file_path} ничего не найдено")
    except Exception as e:
        raise Exception(f"Ошибка {e}")


def reader_transaction_excel(file_path: str) -> list[dict]:
    """Принимает на данные с транзакциями в формате excel  и возвращает список словарей"""
    df = pd.read_excel(file_path)
    excel_data = df.to_dict()
    list_excel = [excel_data]
    return list_excel

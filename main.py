from src.external_api import currency_converter
from src.process_bank import process_bank_search
from src.processing import filter_by_state, sort_by_date
from src.transaction_csv_excel import reader_transaction_csv, reader_transaction_excel
from src.utils import operations_json
from src.widget import get_date, mask_account_card


def main():
    """отвечает за основную логику проекта и связывает функциональности между собой"""
    while True:
        print(
            """
        Программа: Привет! Добро пожаловать в программу работы
        с банковскими транзакциями.
        Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла
        """
        )
        user_input = int(input("Введите нужную цифру:   "))
        if user_input in [1, 2, 3]:
            break

    if user_input == 1:
        transaction_data = operations_json(r"data\operations.json")
    elif user_input == 2:
        transaction_data = reader_transaction_csv(r"data\transactions.csv")
    elif user_input == 3:
        transaction_data = reader_transaction_excel(r"data\transactions_excel.xlsx")
    #
    print(
    """
    Программа: Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
    """
    )
user_input = input("Введите статус:   ").upper()
    
    while True:
        print(f"Программа: Статус операции {user_input} недоступен. ")
        print(
            """
        Программа: Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
        """
        )
        user_input = input("Введите статус:   ").upper()
        if user_input in ["EXECUTED", "CANCELED", "PENDING"]:
            break
    transaction_data = filter_by_state(transaction_data, stat=user_input)

    print("Программа: Отсортировать операции по дате? Да/Нет")
    user_input1 = input("Сделайте выбор:   ").upper()
    if user_input1 == "ДА":
        while True:
            print("Программа: Отсортировать по возрастанию (1) или по убыванию (2)?")
            user_input2 = int(input("Поставьте необходимое число:   "))
            if user_input2 in [1, 2]:
                break
        if user_input2 == 1:
            transaction_data = sort_by_date(transaction_data, bool == False)
        else:
            transaction_data = sort_by_date(transaction_data)
    else:
        transaction_data = filter_by_state(transaction_data, stat=user_input)

    print("Программа: Выводить только рублевые транзакции? Да/Нет")
    user_input3 = input("Сделайте выбор:   ").upper()
    if user_input3 == "ДА":
        code_currency = "RUB"
        print(f'код валюты {code_currency}')
    print("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    user_input4 = input("Сделайте выбор:   ").upper()
    if user_input4 == "ДА":
        user_input5 = input("Введите слово:   ")
    else:
        user_input5 = "перевод"
    transaction_data = process_bank_search(transaction_data, search_string=user_input5)
    total_bank_transaction = len(transaction_data)
    print(f"Всего банковских операций в выборке: {total_bank_transaction}")
    for i in transaction_data:
        id = i.get("date")
        di = get_date(id)
        fromi = i.get("from")
        toi = i.get("to")
        icur = i["operationAmount"]["currency"]["code"]
        iammount = i["operationAmount"]["amount"]

        print(
            f"""
        {di} {i['description']}
        {mask_account_card(fromi)} - > {mask_account_card(toi)}
        {currency_converter(icur, iammount)}
        """
        )


main()

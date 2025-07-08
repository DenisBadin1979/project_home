from src.transaction_csv_excel import reader_transaction_excel


if __name__ == "__main__":

    path = r"D:\mypython\Personal_account\data\transactions_excel.xlsx"
    print(reader_transaction_excel(path))

import pandas as pd


def reader_transaction_csv(file_path: str) -> list[dict]:
    """Принимает на данные с транзакциями в формате CSV  и возвращает список словарей"""
    try:
        df = pd.read_csv(file_path, delimiter=";")
        return df.to_dict(orient="records")
    except FileNotFoundError:
        raise FileNotFoundError(f"По заданному пути {file_path} ничего не найдено")
    except Exception as e:
        raise Exception(f"Ошибка {e}")


def reader_transaction_excel(file_path: str) -> list[dict]:
    """Принимает на данные с транзакциями в формате excel  и возвращает список словарей"""
    try:
        df = pd.read_excel(file_path)
        excel_data = df.to_dict(orient="records")
        return excel_data
    except FileNotFoundError:
        raise FileNotFoundError(f"По заданному пути {file_path} ничего не найдено")
    except Exception as e:
        raise Exception(f"Ошибка {e}")


# ddd = reader_transaction_csv(r"D:\mypython\Personal_account\data\transactions.csv")
# for i in ddd:
#     print (i)

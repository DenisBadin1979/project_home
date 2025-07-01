import json

from src.external_api import currency_converter


def operations_json(file_path: str) -> list[dict]:
    """функция,  принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []

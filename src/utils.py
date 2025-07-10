import json
import logging
from typing import Any

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(r"D:/mypython/Personal_account/logs/utilslog.log", "w", "utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def operations_json(file_path: str) -> list | dict | Any:
    """функция,  принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых
    транзакциях."""
    logger.info("Запущена функция открытия файла JSON")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            logger.info("Файла прочитан JSON")
            f_j = json.load(f)
            return f_j
    except json.JSONDecodeError:
        logger.error("Ошибка формата")
        return []
    except FileNotFoundError:
        logger.error("Ничего не нашел")
        return []


# def oper_currecy(trnasac: list[dict],)
# sss = operations_json(r"D:\mypython\Personal_account\data\operations.json")
# for i in sss:
#     print(i)

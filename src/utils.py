import json
import logging
from typing import Any


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/utilslog.log", "w", "utf-8")
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
            return json.load(f)
    except json.JSONDecodeError:
        logger.error("Ошибка формата")
        return []
    except FileNotFoundError:
        logger.error("Ничего не нашел")
        return []

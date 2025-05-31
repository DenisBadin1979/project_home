def filter_by_state(operation: list[dict], stat: str="EXECUTED") -> list[dict]:
    """Функция принимает список словарей и опционально значение для ключа
    state и возвращает новый список словарей, содержащий только те словари, у которых ключ
    state
     соответствует указанному значению."""
    filter_result = []
    for operations in operation:
        if operations["state"] == stat:
            filter_result.append(operations)
    return filter_result


def sort_by_date(operation: list[dict], revers: bool=True)-> list[dict]:
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание).  должна возвращать новый список"""
    sorted_date = sorted(operation, key=lambda operations: operations["date"], reverse=revers)
    return sorted_date

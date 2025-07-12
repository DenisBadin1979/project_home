def filter_by_state(operation: list[dict], stat: str = "EXECUTED") -> list[dict]:
    """Функция, которая принимает список словарей и опционально значение для ключа
    state и возвращает новый список словарей, содержащий только те словари, у которых ключ
    state
     соответствует указанному значению."""
    filter_result = []
    for operations in operation:
        i_op = operations.get("state", "")
        if i_op == stat:
            filter_result.append(operations)
    return filter_result


def sort_by_date(operation: list[dict], selection_of_sorting: bool = True) -> list[dict]:
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание) должна возвращать новый список"""
    sorted_date = sorted(operation, key=lambda operations: operations["date"], reverse=selection_of_sorting)
    return sorted_date


# print(
#     sort_by_date(
#         [
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ],
#         selection_of_sorting=False,
#     )
# sp =  operations_json(r"D:\mypython\Personal_account\data\operations.json")
# print (filter_by_state(sp))

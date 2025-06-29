import json
from src.external_api import currency_converter



def operations_json (file_path: str) -> list[dict]:
    try:
        with open(file_path , "r", encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []







import json
from unittest.mock import Mock, patch

from src.external_api import currency_converter
from src.utils import operations_json
from tests.conftest import transaction


def test_operations_json() -> None:
    mock_load = Mock(return_value=transaction)
    json.load = mock_load
    assert operations_json(r"D:\mypython\Personal_account\data\operations.json") == transaction


def test_operations_json_none() -> None:
    mock_load = Mock(return_value=[])
    json.load = mock_load
    assert operations_json(r" ") == []


@patch("requests.get")
def test_currency_converter(mock_get) -> None:
    mock_get.return_value.json.return_value = {"result": 7811.1611}
    assert currency_converter("USD", "100") == 7811.1611


@patch("requests.get")
def test_currency_converter2(mock_get) -> None:
    mock_get.return_value.json.return_value = {"result": 90.01}
    assert currency_converter("EUR", "1") == 90.01

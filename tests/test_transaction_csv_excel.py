import unittest
from unittest.mock import Mock, patch

import pytest

from src.transaction_csv_excel import reader_transaction_csv
from tests.conftest import list_dictionary


@patch("builtins.open")
def test_reader_transaction_csv(self, mock_open):

    # Вызываем тестируемую функцию
    result = reader_transaction_csv("dummy_path.csv")


    # Проверяем результат
    expected = [
        {"id": "1", "amount": "100.50", "date": "2023-01-01"},
        {"id": "2", "amount": "200.75", "date": "2023-01-02"}
    ]
    self.assertEqual(result, expected)

    # Проверяем вызов open
    mock_open.assert_called_once_with("dummy_path.csv", "r", encoding=None)

    # Проверяем вызов DictReader
    with patch('csv.DictReader') as mock_dict_reader:
        reader_transaction_csv("dummy_path.csv")
        mock_dict_reader.assert_called_once_with(mock_open_func.return_value, delimiter=';')

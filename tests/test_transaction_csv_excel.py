import unittest
from unittest.mock import patch, mock_open, MagicMock
import pandas as pd
import pytest

from src.transaction_csv_excel import reader_transaction_csv, reader_transaction_excel
from tests.conftest import list_dictionary




# Тестовый класс
class TestReaderTransactionCSV(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open,
           read_data="id;amount;date\n1;100.50;2023-01-01\n2;200.75;2023-01-02")
    def test_reader_transaction_csv(self, mock_open_func):
        """
        Тестируем, что функция правильно читает CSV файл
        """
        # 1. Вызываем нашу функцию с фальшивым путем
        result = reader_transaction_csv("test.csv")

        # 2. Проверяем результат
        expected = [
            {"id": "1", "amount": "100.50", "date": "2023-01-01"},
            {"id": "2", "amount": "200.75", "date": "2023-01-02"}
        ]
        self.assertEqual(result, expected)

        # # 3. Проверяем, что open вызывался правильно
        mock_open_func.assert_called_once_with("test.csv")


# Тесты с использованием unittest
class TestReaderTransactionExcel(unittest.TestCase):
    @patch('pandas.read_excel')
    def test_success_read(self, mock_read_excel):
        """Тест успешного чтения Excel-файла"""
        # Создаем мок DataFrame
        mock_df = MagicMock()
        mock_df.to_dict.return_value = {
            'id': {0: 1, 1: 2},
            'amount': {0: 100.50, 1: 200.75}
        }

        # Настраиваем мок pandas.read_excel
        mock_read_excel.return_value = mock_df

        # Вызываем тестируемую функцию
        result = reader_transaction_excel("dummy.xlsx")

        # Проверяем результат
        expected = [{
            'id': {0: 1, 1: 2},
            'amount': {0: 100.50, 1: 200.75}
        }]
        self.assertEqual(result, expected)
        mock_read_excel.assert_called_once_with("dummy.xlsx")

    @patch('pandas.read_excel')
    def test_file_not_found(self, mock_read_excel):
        """Тест обработки отсутствующего файла"""
        # Настраиваем исключение
        mock_read_excel.side_effect = FileNotFoundError("File not found")

        # Проверяем, что исключение пробрасывается правильно
        with self.assertRaises(FileNotFoundError) as context:
            reader_transaction_excel("missing.xlsx")

        self.assertIn("По заданному пути missing.xlsx ничего не найдено", str(context.exception))

    @patch('pandas.read_excel')
    def test_general_exception(self, mock_read_excel):
        """Тест обработки общего исключения"""
        # Настраиваем исключение
        mock_read_excel.side_effect = Exception("Test error")

        # Проверяем обработку исключения
        with self.assertRaises(Exception) as context:
            reader_transaction_excel("broken.xlsx")

        self.assertIn("Ошибка Test error", str(context.exception))
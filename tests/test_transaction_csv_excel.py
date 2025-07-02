import unittest
from unittest.mock import Mock, patch

import pytest

from src.transaction_csv_excel import reader_transaction_csv
from tests.conftest import list_dictionary


class TestReaderTransactionCSV(unittest.TestCase):
    @patch("builtins.open", read_data="id;amount;date\n1;100.50;2023-01-01\n2;200.75;2023-01-02")
    def test_reader_transaction_csv(self, mock_file):
        expected = [
            {"id": "1", "amount": "100.50", "date": "2023-01-01"},
            {"id": "2", "amount": "200.75", "date": "2023-01-02"},
        ]
        result = reader_transaction_csv("dummy_path.csv")

        self.assertEqual(result, expected)
        mock_file.assert_called_once_with("dummy_path.csv", "r")

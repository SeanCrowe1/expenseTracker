import unittest
from expenses import ExpenseRecord

class TestExpenses(unittest.TestCase):
    def test_valid_data_input(self) -> None:
        record = ExpenseRecord()
        input_data = ("Rent", "1165", "01-06-2026")
        name, amount, date = input_data
        actual = record.add_record(name, amount, date, "expense")
        expected = {"name": name, "amount": "€" + amount, "date": date, "type": "expense"}
        self.assertEqual(actual, expected)

    def test_invalid_name_input(self) -> None:
        record = ExpenseRecord()
        input_data = ("", "1165", "01-06-2026")
        name, amount, date = input_data
        self.assertRaises(ValueError, record.add_record, name, amount, date, "expense")

    def test_invalid_amount_input(self) -> None:
        record = ExpenseRecord()
        input_data = ("Rent", "-1165", "01-06-2026")
        name, amount, date = input_data
        self.assertRaises(ValueError, record.add_record, name, amount, date, "expense")

    def test_invalid_date_input_format(self) -> None:
        record = ExpenseRecord()
        input_data = ("Rent", "1165", "01/06/2026")
        name, amount, date = input_data
        self.assertRaises(ValueError, record.add_record, name, amount, date, "expense")

    def test_invalid_date_input_day(self) -> None:
        record = ExpenseRecord()
        input_data = ("Rent", "1165", "1-06-2026")
        name, amount, date = input_data
        self.assertRaises(ValueError, record.add_record, name, amount, date, "expense")

    def test_invalid_date_input_month(self) -> None:
        record = ExpenseRecord()
        input_data = ("Rent", "1165", "01-6-2026")
        name, amount, date = input_data
        self.assertRaises(ValueError, record.add_record, name, amount, date, "expense")

    def test_invalid_date_input_year(self) -> None:
        record = ExpenseRecord()
        input_data = ("Rent", "1165", "01-06-26")
        name, amount, date = input_data
        self.assertRaises(ValueError, record.add_record, name, amount, date, "expense")
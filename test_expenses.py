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

    def test_update_entry(self) -> None:
        record = ExpenseRecord()
        record.add_record("Rent", "1165", "01-06-2026", "expense")
        actual = record.update_record(0, "Google", "2115", "25-06-2025", "income")
        expected = {"name": "Google", "amount": "€2115", "date":"25-06-2025", "type":"income"}
        self.assertEqual(actual, expected)

    def test_invalid_update(self) -> None:
        record = ExpenseRecord()
        id, name, amount, date, type = (0, "Google", "2115", "25-06-2025", "income")
        self.assertRaises(IndexError, record.update_record, id, name, amount, date, type)

    def test_delete_entry(self) -> None:
        record = ExpenseRecord()
        name, amount, date = ("Rent", "1165", "01-06-2026")
        record.add_record(name, amount, date, "expense")
        actual = record.delete_record(0)
        expected = True
        self.assertEqual(actual, expected)

    def test_invalid_delete(self) -> None:
        record = ExpenseRecord()
        self.assertRaises(IndexError, record.delete_record, 0)


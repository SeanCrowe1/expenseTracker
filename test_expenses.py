import unittest
from expenses import ExpenseRecord

class TestExpenses(unittest.TestCase):
    def test_valid_data_input(self) -> None:
        record = ExpenseRecord()
        input_data = ("Rent", "1165", "01-06-2026")
        name, amount, date = input_data
        record.add_record(name, amount, date)
        actual = record.all()
        expected = [input_data]
        self.assertEqual(actual, expected)

    def test_invalid_name_input(self) -> None:
        record = ExpenseRecord()
        input_data = ("", "1165", "01-06-2026")
        name, amount, date = input_data
        actual_err = record.add_record(name, amount, date)
        actual_records = record.all()
        expected_err = "Name is required"
        expected_records = []
        self.assertEqual(actual_err, expected_err)
        self.assertEqual(actual_records, expected_records)

    def test_invalid_amount_input(self) -> None:
        record = ExpenseRecord()
        input_data = ("Rent", "-1165", "01-06-2026")
        name, amount, date = input_data
        actual_err = record.add_record(name, amount, date)
        actual_records = record.all()
        expected_err = "Amount must be a valid number greater than 0."
        expected_records = []
        self.assertEqual(actual_err, expected_err)
        self.assertEqual(actual_records, expected_records)

    def test_invalid_date_input_format(self) -> None:
        record = ExpenseRecord()
        input_data = ("Rent", "1165", "01/06/2026")
        name, amount, date = input_data
        actual_err = record.add_record(name, amount, date)
        actual_records = record.all()
        expected_err = "Date must be valid date in the format 'DD-MM-YYYY'."
        expected_records = []
        self.assertEqual(actual_err, expected_err)
        self.assertEqual(actual_records, expected_records)

    def test_invalid_date_input_day(self) -> None:
        record = ExpenseRecord()
        input_data = ("Rent", "1165", "1-06-2026")
        name, amount, date = input_data
        actual_err = record.add_record(name, amount, date)
        actual_records = record.all()
        expected_err = "Date must be valid date in the format 'DD-MM-YYYY'."
        expected_records = []
        self.assertEqual(actual_err, expected_err)
        self.assertEqual(actual_records, expected_records)

    def test_invalid_date_input_month(self) -> None:
        record = ExpenseRecord()
        input_data = ("Rent", "1165", "01-6-2026")
        name, amount, date = input_data
        actual_err = record.add_record(name, amount, date)
        actual_records = record.all()
        expected_err = "Date must be valid date in the format 'DD-MM-YYYY'."
        expected_records = []
        self.assertEqual(actual_err, expected_err)
        self.assertEqual(actual_records, expected_records)

    def test_invalid_date_input_year(self) -> None:
        record = ExpenseRecord()
        input_data = ("Rent", "1165", "01-06-26")
        name, amount, date = input_data
        actual_err = record.add_record(name, amount, date)
        actual_records = record.all()
        expected_err = "Date must be valid date in the format 'DD-MM-YYYY'."
        expected_records = []
        self.assertEqual(actual_err, expected_err)
        self.assertEqual(actual_records, expected_records)
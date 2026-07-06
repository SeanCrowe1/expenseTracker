import unittest
from expenses import ExpenseRecord

class TestExpenses(unittest.TestCase):
    def test_valid_data_input(self) -> None:
        record = ExpenseRecord()
        record.delete_all()
        input_data = ("Rent", "1165", "01-06-2026")
        name, amount, date = input_data
        record.add_expense(name, amount, date, "Expense")
        actual = record.all()
        expected = [{"name": name, "amount": "€1165.00", "date": date, "type": "Expense"}]
        self.assertEqual(actual, expected)

    def test_invalid_name_input(self) -> None:
        record = ExpenseRecord()
        record.delete_all()
        input_data = ("", "1165", "01-06-2026")
        name, amount, date = input_data
        actual = record.add_expense(name, amount, date, "Expense")
        expected = "Name is required"
        self.assertEqual(actual, expected)

    def test_invalid_amount_input(self) -> None:
        record = ExpenseRecord()
        record.delete_all()
        input_data = ("Rent", "-1165", "01-06-2026")
        name, amount, date = input_data
        actual = record.add_expense(name, amount, date, "Expense")
        expected = "Amount must be a valid number greater than 0."
        self.assertEqual(actual, expected)

    def test_invalid_date_input_format(self) -> None:
        record = ExpenseRecord()
        record.delete_all()
        input_data = ("Rent", "1165", "01/06/2026")
        name, amount, date = input_data
        actual = record.add_expense(name, amount, date, "Expense")
        expected = "Date must be valid date in the format 'DD-MM-YYYY'."
        self.assertEqual(actual, expected)

    def test_invalid_date_input_day(self) -> None:
        record = ExpenseRecord()
        record.delete_all()
        input_data = ("Rent", "1165", "1-06-2026")
        name, amount, date = input_data
        actual = record.add_expense(name, amount, date, "Expense")
        expected = "Date must be valid date in the format 'DD-MM-YYYY'."
        self.assertEqual(actual, expected)

    def test_invalid_date_input_month(self) -> None:
        record = ExpenseRecord()
        record.delete_all()
        input_data = ("Rent", "1165", "01-6-2026")
        name, amount, date = input_data
        actual = record.add_expense(name, amount, date, "Expense")
        expected = "Date must be valid date in the format 'DD-MM-YYYY'."
        self.assertEqual(actual, expected)

    def test_invalid_date_input_year(self) -> None:
        record = ExpenseRecord()
        record.delete_all()
        input_data = ("Rent", "1165", "01-06-26")
        name, amount, date = input_data
        actual = record.add_expense(name, amount, date, "Expense")
        expected = "Date must be valid date in the format 'DD-MM-YYYY'."
        self.assertEqual(actual, expected)

    def test_update_entry(self) -> None:
        record = ExpenseRecord()
        record.delete_all()
        record.add_expense("Rent", "1165", "01-06-2026", "expense")
        record.update_expense(0, "Google", "2115", "25-06-2025", "Income")
        actual = record.all()
        expected = [{"name": "Google", "amount": "€2115.00", "date":"25-06-2025", "type":"Income"}]
        self.assertEqual(actual, expected)

    def test_invalid_update(self) -> None:
        record = ExpenseRecord()
        record.delete_all()
        id, name, amount, date, type = (0, "Google", "2115", "25-06-2025", "income")
        actual = record.update_expense(id, name, amount, date, type)
        expected = "Cannot find id in record: 0"
        self.assertEqual(actual, expected)

    def test_delete_entry(self) -> None:
        record = ExpenseRecord()
        record.delete_all()
        name, amount, date = ("Rent", "1165", "01-06-2026")
        record.add_expense(name, amount, date, "expense")
        actual = record.delete_expense(0)
        expected = ""
        self.assertEqual(actual, expected)

    def test_invalid_delete(self) -> None:
        record = ExpenseRecord()
        record.delete_all()
        actual = record.delete_expense(0)
        expected = "Cannot find id in record: 0"
        self.assertEqual(actual, expected)

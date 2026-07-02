import json as js
from os import path

class ExpenseRecord:
    def __init__(self):
        self._expenses = self.read_json_record()
        self.total = 0
        self.calc_total()

    def all(self):
        return self._expenses
    
    def calc_total(self):
        total = 0

        for record in self._expenses:
            num = float(record["amount"][1:])
            
            if record["type"] == "Income":
                total += num
            else:
                total -= num

        self.total = total
    
    def validate(self, name, amount, date):
        """Return an error message if the data is invalid, else None."""
        if not name:
            return ValueError("Name is required")
        
        if float(amount) < 0:
            return ValueError("Amount must be a valid number greater than 0.")
        
        INVALID_DATE = ValueError("Date must be valid date in the format 'DD-MM-YYYY'.")
        segments = date.split("-")
        if len(segments) != 3:
            return INVALID_DATE
        
        day, month, year = segments
        if len(day) != 2 or int(day) < 1 or int(day) > 31:
            return INVALID_DATE
        
        if len(month) != 2 or int(month) < 1 or int(month) > 12:
            return INVALID_DATE
        
        if len(year) != 4:
            return INVALID_DATE
        
        if int(year) < 0:
            return INVALID_DATE
        
        if month == "02":
            if (int(month) % 4 == 0 and int(day) > 29) or int(day) > 28:
                return INVALID_DATE
        elif month in ["04", "06", "09", "11"]:
            if int(day) > 30:
                return INVALID_DATE
        else:
            if int(day) > 31:
                return INVALID_DATE
            
        return ""
            
    def add_record(self, name, amount, date, type):
        name = name.strip()
        err = self.validate(name, amount, date)
        if err:
            raise err
        
        expense = {
            "name": name,
            "amount": f"€{float(amount):.2f}",
            "date": date,
            "type": type,
        }

        self._expenses.append(expense)
        self.calc_total()
        return expense
    
    def update_record(self, id, name, amount, date, type_v):
        expense = {}

        if id >= len(self._expenses):
            raise IndexError(f"Cannot receive selection from records: {id}")
        
        expense = self._expenses[id]

        expense["name"] = name
        expense["amount"] = f"€{amount:.2f}"
        expense["date"] = date
        expense["type"] = type_v

        self._expenses[id] = expense
        self.calc_total()

        return expense
    
    def delete_record(self, id) -> bool:
        if id >= len(self._expenses):
            raise IndexError(f"Cannot find record in record: {id}")
        
        del self._expenses[id]
        self.calc_total()
        return True
    
    def read_json_record(self, filename="records.json"):
        record = []

        if path.isfile(filename):
            with open(filename) as f:
                record = js.loads(f.read())

        return record

    def write_json_record(self, record_data, filename="records.json"):
        with open(filename, "w", encoding="utf-8") as f:
            js.dump(record_data, f, indent=2)
    
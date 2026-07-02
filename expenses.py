class ExpenseRecord:
    def __init__(self):
        self._expenses = []

    def all(self):
        return self._expenses
    
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
            "amount": "€" + amount,
            "date": date,
            "type": type,
        }

        self._expenses.append(expense)
        return expense
    
    def update_record(self, id, name, amount, date, type_v):
        expense = {}

        if id >= len(self._expenses):
            return IndexError(f"Cannot receive selection from records: {id}")
        
        expense = self._expenses[id]

        expense["name"] = name
        expense["amount"] = f"€{amount}"
        expense["date"] = date
        expense["type"] = type_v
    
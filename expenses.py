from json_record import read_json_record

class ExpenseRecord:
    def __init__(self):
        self._expenses = read_json_record()
        self.expense = 0
        self.income = 0
        self.total = 0
        self.calc_total()

    def all(self):
        return self._expenses
    
    def calc_total(self):
        expenses = 0
        income = 0
        total = 0

        for record in self._expenses:
            num = float(record["amount"][1:])
            
            if record["type"] == "Income":
                income += num
                total += num
            else:
                expenses += num
                total -= num

        self.expense = expenses
        self.income = income
        self.total = total
    
    def validate(self, name, amount, date):
        """Return an error message if the data is invalid, else None."""
        if not name:
            return "Name is required"
        
        if amount == "" or float(amount) < 0:
            return "Amount must be a valid number greater than 0."
        
        INVALID_DATE = "Date must be valid date in the format 'DD-MM-YYYY'."
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
            return err
        
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
            return f"Cannot find id in record: {id}"

        err = self.validate(name, amount, date)
        if err:
            return err
        
        expense = self._expenses[id]

        expense["name"] = name
        expense["amount"] = f"€{float(amount):.2f}"
        expense["date"] = date
        expense["type"] = type_v

        self._expenses[id] = expense
        self.calc_total()

        return expense
    
    def delete_record(self, id) -> bool:
        if id >= len(self._expenses):
            return f"Cannot find id in record: {id}"
        
        del self._expenses[id]
        self.calc_total()
        return True
    
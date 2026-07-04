from json_record import read_json_record

class ExpenseRecord:
    def __init__(self):
        """Initializes app's internal record with stored JSON data and expense totals for summary display."""
        self._expenses = read_json_record()
        self.expense = 0
        self.income = 0
        self.total = 0
        self.calc_total()

    def all(self):
        """Return all currently stored expenses."""
        return self._expenses
    
    def calc_total(self):
        """Calculate and update all summary totals for currently stored expenses."""
        expenses = 0
        income = 0
        total = 0

        for record in self._expenses:
            # Remove the leading € sign from the amount string and convert to a float
            num = float(record["amount"][1:])
            
            # If expense is an income, add to total and add to income, otherwise subtract from total and add to expense amount
            if record["type"] == "Income":
                income += num
                total += num
            else:
                expenses += num
                total -= num

        # Update all totals
        self.expense = expenses
        self.income = income
        self.total = total
    
    def validate(self, name, amount, date):
        """Return an error message if the inptut data is invalid, else None."""
        # Empty 'Name' field error
        if not name:
            return "Name is required"
        
        # Empty or invalid 'Amount' field error
        if amount == "" or float(amount) < 0:
            return "Amount must be a valid number greater than 0."
        
        INVALID_DATE = "Date must be valid date in the format 'DD-MM-YYYY'."
        segments = date.split("-")
        # Check that date.split made exactly 3 segments for day, month and year
        if len(segments) != 3:
            return INVALID_DATE
        
        day, month, year = segments
        # Check for valid day entry
        if len(day) != 2 or int(day) < 1 or int(day) > 31:
            return INVALID_DATE
        
        # Check for valid month entry
        if len(month) != 2 or int(month) < 1 or int(month) > 12:
            return INVALID_DATE
        
        # Check for valid year entry (I decided that year must be AD, number below 0 is invalid)
        if len(year) != 4 or int(year) < 0:
            return INVALID_DATE
        
        # Recheck for valid day entry based on month entry
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
        """Add an expense to the current record."""
        name = name.strip()
        # Validate entry fields
        err = self.validate(name, amount, date)
        if err:
            return err
        
        # Construct expense entry for stored record list
        expense = {
            "name": name,
            "amount": f"€{float(amount):.2f}",
            "date": date,
            "type": type,
        }

        # Update record list and recalculate the summary totals
        self._expenses.append(expense)
        self.calc_total()
        return ""
    
    def update_record(self, id, name, amount, date, type_v):
        """Update an expense stored in the current record."""
        expense = {}

        # id will be the index of the expense to be updated
        # Check that id exists for the current record list
        if id >= len(self._expenses):
            return f"Cannot find id in record: {id}"

        # Validate entry fields
        err = self.validate(name, amount, date)
        if err:
            return err
        
        # Capture selected expense from stored list
        expense = self._expenses[id]

        # Update captured expense with new data
        expense["name"] = name
        expense["amount"] = f"€{float(amount):.2f}"
        expense["date"] = date
        expense["type"] = type_v

        # Update selected expense in place in stored record list and recalculate summary totals
        self._expenses[id] = expense
        self.calc_total()
        return ""
    
    def delete_record(self, id: int) -> str:
        """Delete an expense stored in the current record."""
        # id will be the index of the expense to be deleted
        # Check that id exists for the current record list
        if id >= len(self._expenses):
            return f"Cannot find id in record: {id}"
        
        # Delete the expense from the record and recalculate the summary totals
        del self._expenses[id]
        self.calc_total()
        return ""
    
    def delete_all(self):
        """Delete all stored expenses from current record"""
        self._expenses = []
    
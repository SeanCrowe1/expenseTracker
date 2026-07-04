import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from expenses import ExpenseRecord as ER
from json_record import write_json_record

class ExpenseTrackerApp:
    def __init__(self, root: tk.Tk):
        """Initialize app display and all entry and display variables."""
        self.record = ER()
        self.root = root
        
        root.title("Expense Tracker")
        root.geometry("1000x800")
        root.option_add("*Font", ("", 12))
        root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.name_var = tk.StringVar()
        self.amount_var = tk.StringVar()
        self.date_var = tk.StringVar()
        self.type_var = tk.StringVar(value="Income")
        self.expenses_var = tk.DoubleVar(value=self.record.expense)
        self.income_var = tk.DoubleVar(value=self.record.income)
        self.total_var = tk.DoubleVar(value=self.record.total)

        self.build_form()
        self.build_table()
        self.build_footer()
        self.refresh_tree()

    def build_form(self):
        """Construct and format the app's form entry fields."""
        form = ttk.Frame(self.root, padding=8)
        form.pack(fill="x")

        ttk.Label(form, text="Name:").grid(row=0, column=0, padx=10, pady=2, sticky="e")
        ttk.Entry(form, width=86, textvariable=self.name_var).grid(row=0, column=1, columnspan=4, padx=10, pady=2, sticky="ew")

        ttk.Label(form, text="Amount:").grid(row=1,column=0, padx=10, pady=2, sticky="e")
        ttk.Entry(form, width=86, textvariable=self.amount_var).grid(row=1, column=1, columnspan=4, padx=10, pady=2, sticky="ew")

        ttk.Label(form, text="Date:").grid(row=2,column=0, padx=10, pady=2, sticky="e")
        ttk.Entry(form, width=86, textvariable=self.date_var).grid(row=2, column=1, columnspan=4, padx=10, pady=2, sticky="ew")

        ttk.Label(form, text="Type:").grid(row=3, column=0, padx=10, pady=2, sticky="e")
        ttk.Radiobutton(form, text="Income", variable=self.type_var, value="Income").grid(row=3, column=2, padx=10, pady=2, sticky="ew")
        ttk.Radiobutton(form, text="Expense", variable=self.type_var, value="Expense").grid(row=3, column=3, padx=10, pady=2, sticky="ew")

        ttk.Button(form, width=15, text="Add", command=self.add_expense).grid(row=4, column=1, rowspan=2)
        ttk.Button(form, width=15, text="Save Changes", command=self.save_changes).grid(row=4, column=2, rowspan=2)
        ttk.Button(form, width=15, text="Delete", command=self.delete_expense).grid(row=4, column=3, rowspan=2)
        ttk.Button(form, width=15, text="Clear", command=self.clear_form).grid(row=4, column=4, rowspan=2)

    def build_table(self):
        """Construct and format the app's treeview table field to display stored expense record."""
        table_frame = ttk.Frame(self.root)
        table_frame.pack(fill="both", expand=True)

        columns = ("name", "amount", "date", "type")

        self.table = ttk.Treeview(table_frame, columns=columns, show="headings", height=8)
        self.table.bind("<<TreeviewSelect>>", self.on_select)

        self.table.heading("name", text="Name")
        self.table.column("name", width=120)

        self.table.heading("amount", text="Amount")
        self.table.column("amount", width=120)

        self.table.heading("date", text="Date")
        self.table.column("date", width=120)

        self.table.heading("type", text="Type")
        self.table.column("type", width=120)

        scroll = ttk.Scrollbar(table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scroll.set)
        scroll.pack(side="right", fill="y")

        self.table.pack(side="left", fill="both", expand=True)

    def build_footer(self):
        """Construct and format the app's footer display with all summary totals."""
        footer = ttk.Frame(self.root, padding=8)
        footer.pack(fill="x")
        self.footer = footer
        self.expenses_label = ttk.Label(footer, width=36, text=f"Total Expenses: €{self.expenses_var.get()}")
        self.expenses_label.grid(row=0, column=0, sticky="w")
        self.income_label = ttk.Label(footer, width=36, text=f"Total Income: €{self.income_var.get()}")
        self.income_label.grid(row=0, column=1, sticky="w")
        self.total_label = ttk.Label(footer, width=36, text=f"Total Balance: €{self.total_var.get()}")
        self.total_label.grid(row=0, column=2, sticky="w")

    def refresh_tree(self):
        """Update the app's stored variables and table."""
        # Delete all items in treeview and insert everything from current record
        for item in self.table.get_children():
            self.table.delete(item)
        
        all_records = self.record.all()
        for index, record in enumerate(all_records):
            self.table.insert("", "end", iid=str(index), values=list(record.values()))

        # Set all summary total variables and update display
        self.expenses_var.set(self.record.expense)
        self.income_var.set(self.record.income)
        self.total_var.set(self.record.total)

        str_expense = '{:.2f}'.format(self.expenses_var.get())
        self.expenses_label.config(text=f"Total Expenses: €{str_expense}")
        str_income = '{:.2f}'.format(self.income_var.get())
        self.income_label.config(text=f"Total Income: €{str_income}")
        str_total = '{:.2f}'.format(self.total_var.get())
        self.total_label.config(text=f"Total Balance: €{str_total}")
        
    # Event handlers
    def add_expense(self):
        """Use app's entry fields to store an expense in the record."""
        name = self.name_var.get()
        amount = self.amount_var.get()
        date = self.date_var.get()
        type_var = self.type_var.get()

        # Display error message to user and stop the current operation if add_record returns an error message
        res = self.record.add_record(name, amount, date, type_var)
        if res:
            mb.showerror("Validation Error", res)
            return
        
        # Update app display and clear entry fields
        self.refresh_tree()
        self.clear_form()

    def save_changes(self):
        """Update a selected entry in the app's record with new values"""
        id = self.table.focus()
        
        # Display error message to user and stop the current operation if no item is selected
        if id == "":
            mb.showerror("Selection Error", "Error: No item in table selected")
            return
        
        id = int(id)

        name = self.name_var.get()
        amount = self.amount_var.get()
        date = self.date_var.get()
        type_v = self.type_var.get()

        self.record.validate(name, amount, date)

        # Display error message to user and stop the current operation if update_record returns an error message
        res = self.record.update_record(id, name, amount, date, type_v)
        if res:
            mb.showerror("Validation Error", res)
            return
        
        # Update app display and clear entry fields
        self.refresh_tree()
        self.clear_form()

    def delete_expense(self):
        """Delete a selected entry from the app's record"""
        id = self.table.focus()
        
        # Display error message to user and stop the current operation if no item is selected
        if id == "":
            mb.showerror("Selection Error", "Error: No item in table selected")
            return
        
        id = int(id)

        # Prompt the user to confirm their choice before deleting selected entry
        if mb.askquestion("Confirmation", "Are you sure you want to delete this record?", icon="warning") == "no":
            return
        
        # Display error message to user and stop the current operation if delete_record returns an error message
        res = self.record.delete_record(id)
        if res:
            mb.showerror("Validation Error", res)
            return
        
        # Update app display and clear entry fields
        self.refresh_tree()
        self.clear_form()

    def clear_form(self):
        """Reset all entry fields to their default values"""
        self.name_var.set("")
        self.amount_var.set("")
        self.date_var.set("")
        self.type_var.set("Income")

    def on_select(self, event):
        """Fill app's entry fields with selected expense's details"""
        selected = self.table.focus()

        # Gracefully stops operation when no entry is selected
        if not selected:
            return
        
        record_vals = self.table.item(selected)["values"]

        self.name_var.set(record_vals[0])
        self.amount_var.set(record_vals[1][1:])
        self.date_var.set(record_vals[2])
        self.type_var.set(record_vals[3])

    def on_close(self):
        """Save all stored record data to JSON file when closing the app window"""
        record_data = self.record.all()
        write_json_record(record_data)
        self.root.destroy()

if __name__ == "__main__":
    main_window = tk.Tk()
    app = ExpenseTrackerApp(main_window)
    app.root.mainloop()
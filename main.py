import tkinter as tk
from tkinter import ttk
from expenses import ExpenseRecord

class ExpenseTrackerApp:
    def __init__(self, root):
        self.record = ExpenseRecord()
        self.root = root
        root.title("Expense Tracker")
        root.geometry("1000x800")

        self.name_var = tk.StringVar()
        self.amount_var = tk.StringVar()
        self.date_var = tk.StringVar()
        self.type_var = tk.StringVar(value="Income")

        self.build_form()
        self.build_table()
        self.refresh_tree()

    def build_form(self):
        form = ttk.Frame(self.root, padding=8)
        form.pack(fill="x")

        ttk.Label(form, text="Name:").grid(row=0, column=0, sticky="e")
        ttk.Entry(form, width=112, textvariable=self.name_var).grid(row=0, column=1, columnspan=4, padx=10, pady=2, sticky="ew")

        ttk.Label(form, text="Amount:").grid(row=1,column=0, sticky="e")
        ttk.Entry(form, width=112, textvariable=self.amount_var).grid(row=1, column=1, columnspan=4, padx=10, pady=2, sticky="ew")

        ttk.Label(form, text="Date:").grid(row=2,column=0, sticky="e")
        ttk.Entry(form, width=112, textvariable=self.date_var).grid(row=2, column=1, columnspan=4, padx=10, pady=2, sticky="ew")

        ttk.Label(form, text="Type:").grid(row=3, column=0, sticky="e")
        ttk.Radiobutton(form, text="Income", variable=self.type_var, value="Income").grid(row=3, column=2, padx=10, pady=2, sticky="ew")
        ttk.Radiobutton(form, text="Expense", variable=self.type_var, value="Expense").grid(row=3, column=3, padx=10, pady=2, sticky="ew")

        ttk.Button(form, text="Add", command=self.add_expense).grid(row=4, column=1)
        ttk.Button(form, text="Save Changes", command=self.save_changes).grid(row=4, column=2)
        ttk.Button(form, text="Delete", command=self.delete_expense).grid(row=4, column=3)
        ttk.Button(form, text="Clear", command=self.clear_form).grid(row=4, column=4)

    def build_table(self):
        table_frame = ttk.Frame(self.root)
        table_frame.pack(fill="both", expand=True)

        columns = ("name", "amount", "date", "type")

        self.table = ttk.Treeview(table_frame, columns=columns, show="headings", height=8)

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

    def refresh_tree(self):
        for item in self.table.get_children():
            self.table.delete(item)
        
        all_records = self.record.all()
        for index, record in enumerate(all_records):
            self.table.insert("", "end", iid=str(index), values=list(record.values()))

    def clear_form(self):
        self.name_var.set("")
        self.amount_var.set("")
        self.date_var.set("")
        self.type_var.set("Income")
        
    def add_expense(self):
        name = self.name_var.get()
        amount = self.amount_var.get()
        date = self.date_var.get()
        type_var = self.type_var.get()

        res = self.record.add_record(name, amount, date, type_var)
        if res is None:
            return
        
        self.refresh_tree()

    def on_select(self):
        pass

    def save_changes(self):
        pass

    def delete_expense(self):
        pass

    def on_close(self):
        pass    

if __name__ == "__main__":
    main_window = tk.Tk()
    app = ExpenseTrackerApp(main_window)
    app.root.mainloop()
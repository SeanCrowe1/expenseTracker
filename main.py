import tkinter as tk

class ExpenseTrackerApp:
    
    def __init__(self, window):
        self.root_window = window
        window.title("Expense Tracker")
        window.geometry("700x500")
        # self.root_window.geometry("700x500") # This also works as it's the same object

        tk.Label(window, text="Expense Tracker").pack()
        tk.Button(window, text="Add", command=self.add_expense).pack()
        tk.Button(window, text="Save Changes", command=self.save_changes).pack()
        tk.Button(window, text="Delete", command=self.delete_expense).pack()
        tk.Button(window, text="Clear", command=self.clear_form).pack()
        
    # Handlers (event handlers)
    def add_expense(self):
        pass

    def on_select(self):
        pass

    def save_changes(self):
        pass

    def delete_expense(self):
        pass

    def clear_form(self):
        pass

    def on_close(self):
        pass    

if __name__ == "__main__":
    # main_window is a reference to a tkinter window object
    main_window = tk.Tk()
    # app is not really used
    app = ExpenseTrackerApp(main_window)
    app.root_window.mainloop()
    # main_window.mainloop()
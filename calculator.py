import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Calculator")
        self.master.geometry("300x400")

        self.result_var = tk.StringVar()

        # Entry field for the expression
        self.entry = tk.Entry(master, textvariable=self.result_var, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4)

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            if button == '=':
                btn = tk.Button(master, text=button, padx=20, pady=20, command=self.calculate)
            elif button == 'C':
                btn = tk.Button(master, text=button, padx=20, pady=20, command=self.clear)
            else:
                btn = tk.Button(master, text=button, padx=20, pady=20, command=lambda b=button: self.append_to_expression(b))

            btn.grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def append_to_expression(self, value):
        current_expression = self.result_var.get()
        self.result_var.set(current_expression + value)

    def calculate(self):
        try:
            result = eval(self.result_var.get())
            self.result_var.set(result)
        except Exception as e:
            self.result_var.set("Error")

    def clear(self):
        self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

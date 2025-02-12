import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 24, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
LIGHT_GREY = "#F5F5F5"
LABEL_COLOR = "#25265E"
WHITE = "#FFFFFF"
OFF_WHITE = "#F8FAFF"

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("300x400")
        self.window.resizable(0, 0)

        self.current_expression = ""

        self.display_frame = self.create_display_frame()
        self.label = self.create_display_label()

        self.buttons_frame = self.create_buttons_frame()
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_clear_button()
        self.create_equals_button()

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=100, bg=LIGHT_GREY)
        frame.pack(expand=True, fill="both")
        return frame

    def create_display_label(self):
        label = tk.Label(
            self.display_frame, text=self.current_expression, anchor=tk.E,
            bg=LIGHT_GREY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE
        )
        label.pack(expand=True, fill="both")
        return label

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        for i in range(5):
            frame.rowconfigure(i, weight=1)
            frame.columnconfigure(i, weight=1)
        return frame

    def create_digit_buttons(self):
        digits = {
            7: (1, 0), 8: (1, 1), 9: (1, 2),
            4: (2, 0), 5: (2, 1), 6: (2, 2),
            1: (3, 0), 2: (3, 1), 3: (3, 2),
            0: (4, 1)
        } 

        for digit, grid_value in digits.items():
            button = tk.Button(
                self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR,
                font=SMALL_FONT_STYLE, borderwidth=0,
                command=lambda x=digit: self.add_to_expression(str(x))
            )
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_operator_buttons(self):
        operators = {"+": (1, 3), "-": (2, 3), "*": (3, 3), "/": (4, 4)}

        for operator, grid_value in operators.items():
            button = tk.Button(
                self.buttons_frame, text=operator, bg=OFF_WHITE, fg=LABEL_COLOR,
                font=SMALL_FONT_STYLE, borderwidth=0,
                command=lambda x=operator: self.add_to_expression(x)
            )
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_clear_button(self):
        button = tk.Button(
            self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR,
            font=SMALL_FONT_STYLE, borderwidth=0, command=self.clear
        )
        button.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW)

    def create_equals_button(self):
        button = tk.Button(
            self.buttons_frame, text="=", bg=OFF_WHITE, fg=LABEL_COLOR,
            font=SMALL_FONT_STYLE, borderwidth=0, command=self.evaluate
        )
        button.grid(row=4, column=2, columnspan=2, sticky=tk.NSEW)

    def add_to_expression(self, value):
        self.current_expression += value
        self.update_label()

    def clear(self):
        self.current_expression = ""
        self.update_label()

    def evaluate(self):
        try:
            self.current_expression = str(eval(self.current_expression))
        except Exception:
            self.current_expression = "Error"
        self.update_label()

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()

import tkinter as tk
from tkinter import messagebox


class TuringMachineSimulator(tk.Tk):
    # initialize the GUI Window
    def __init__(self):
        super().__init__()
        self.title("Turing Machine Simulator")
        self.geometry("1200x1200")
        self.create_welcome_page()
        # transition display
        self.transition_display = tk.Text(self, height=10, state='disabled')
        self.transition_display.pack(pady=(5, 20))

    def create_welcome_page(self):
        self.configure(bg="#4a36bf")  # background color

        tk.Label(self, text="Turing Machine Simulator", bg="#2f1d91",
                 fg="white",
                 font=('Times New Roman', 45, "bold")).pack(pady=150)

        # button configuration
        tk.Button(self, text="Enter", bg="#2f1d91", font=(
            'Times New Roman', 30, "bold"),
                  command=self.create_options_page).pack(pady=150)

    def create_options_page(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.configure(bg="#4a36bf")

        tk.Label(self, text="Pick anyone to test:", bg="#2f1d91",
                 font=('Times New Roman', 50)).pack(pady=20)

        options = [
            ("Accept odd one's and even zero's", 0),
            ("Accept even one's and odd zero's", 1),
            ("Accept even one's and even zero's", 2),
            ("Accept odd one's and odd zero's", 3)]
        self.selected_option = tk.IntVar()

        for option, value in options:
            # radio buttons for the options
            tk.Radiobutton(self, text=option, bg="#2f1d91", font=(
                'Times New Roman', 26),
                           variable=self.selected_option, value=value).pack(pady=50)

        tk.Button(self, text="Next", bg="#2f1d91", font=(
            'Times New Roman', 22),
                  command=self.create_input_page).pack(pady=50)

    def create_input_page(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.configure(bg="#4a36bf")
        tk.Label(self, text="Enter string:", bg="#2f1d91",
                 font=('Times New Roman', 26)).pack(pady=50)

        self.string_input = tk.Entry(self, bg="#2f1d91", font=("Times New Roman", 34))
        self.string_input.pack(pady=100)

        tk.Button(self, text="Check", bg="#FFFACD", font=(
            'Times New Roman', 22),
                  command=self.check_string).pack(pady=40)
        # Recreate the transition display
        self.transition_display = tk.Text(self, height=10, state='disabled')
        self.transition_display.pack(expand=True, fill='both')

    # retrieves the input string and checks on the coditions
    def check_string(self):
        string = self.string_input.get()
        option = self.selected_option.get()
        if option == 0:
            if self.accepts_odd_ones_even_zeros(string):
                messagebox.showinfo(
                    "Result", f"The string '{string}' is accepted.")
            else:
                messagebox.showinfo(
                    "Result", f"The string '{string}' is not accepted.")
        elif option == 1:
            if self.accepts_even_ones_odd_zeros(string):
                messagebox.showinfo(
                    "Result", f"The string '{string}' is accepted.")
            else:
                messagebox.showinfo(
                    "Result", f"The string '{string}' is not accepted.")
        elif option == 2:
            if self.accepts_even_ones_even_zeros(string):
                messagebox.showinfo(
                    "Result", f"The string '{string}' is accepted.")
            else:
                messagebox.showinfo(
                    "Result", f"The string '{string}' is not accepted.")
        elif option == 3:
            if self.accepts_odd_ones_odd_zeros(string):
                messagebox.showinfo(
                    "Result", f"The string '{string}' is accepted.")
            else:
                messagebox.showinfo(
                    "Result", f"The string '{string}' is not accepted.")

        restart_button = tk.Button(self, text='Restart', font=(
            'Times New Roman', 22), command=self.restart)
        restart_button.pack(side="left", padx=120, pady=30)

        exit_button = tk.Button(self, text='Close', padx=10, font=(
            'Times New Roman', 22), command=self.exit)
        exit_button.pack(side="left", padx=175, pady=30)

    # Turing Machine logic method
    def transition(self, state, symbol, transitions):
        """
        Performs a state transition.
        :param state: The current state
        :param symbol: The current symbol
        :param transitions: A dictionary containing the transitions
        :return: The next state
        """
        next_state = transitions.get((state, symbol), None)
        self.update_transition_display(state, symbol, next_state)
        return next_state

    def update_transition_display(self, state, symbol, next_state):
        # Update the Text widget with the current transition
        self.transition_display.config(state='normal')  # Enable editing of the widget
        transition_message = f"Current State: {state}, Symbol: '{symbol}', Next State: {next_state}\n"
        self.transition_display.insert('end', transition_message)
        self.transition_display.config(state='disabled')  # Disable editing of the widget
        self.transition_display.see('end')  # Scroll to the end of the widget

    def accepts_odd_ones_even_zeros(self, string):
        transitions = {
            (0, '0'): 2,
            (0, '1'): 1,
            (1, '0'): 3,
            (1, '1'): 0,
            (2, '0'): 0,
            (2, '1'): 3,
            (3, '0'): 1,
            (3, '1'): 2
        }
        state = 0

        # iterated through the input string
        for symbol in string:
            state = self.transition(state, symbol, transitions)
            if state is None:
                print("Invalid symbol or transition.")
                return False
        print(f"Final State: {state}")
        return state == 1

    def accepts_even_ones_odd_zeros(self, string):
        transitions = {
            (0, '0'): 2,
            (0, '1'): 1,
            (1, '0'): 3,
            (1, '1'): 0,
            (2, '0'): 0,
            (2, '1'): 3,
            (3, '0'): 1,
            (3, '1'): 2
        }
        state = 0
        for symbol in string:
            state = self.transition(state, symbol, transitions)
            if state is None:
                return False
        return state == 2

    def accepts_even_ones_even_zeros(self, string):
        transitions = {
            (0, '0'): 1,
            (0, '1'): 2,
            (1, '0'): 0,
            (1, '1'): 3,
            (2, '0'): 3,
            (2, '1'): 0,
            (3, '0'): 2,
            (3, '1'): 1
        }
        state = 0
        for symbol in string:
            state = self.transition(state, symbol, transitions)
            if state is None:
                return False
        return state == 0

    def accepts_odd_ones_odd_zeros(self, string):
        transitions = {
            (0, '0'): 2,
            (0, '1'): 1,
            (1, '0'): 3,
            (1, '1'): 0,
            (2, '0'): 0,
            (2, '1'): 3,
            (3, '0'): 1,
            (3, '1'): 2
        }
        state = 0
        for symbol in string:
            state = self.transition(state, symbol, transitions)
            if state is None:
                return False
        return state == 3

    def restart(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.create_welcome_page()

    def exit(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.exit_frame = tk.Frame(self)
        self.exit_frame.pack(pady=50)

        self.exit_label = tk.Label(self.exit_frame,
                                   font=('Times New Roman', 34))

        self.exit_label.config(text='Thank You')
        self.exit_label.pack()

        self.after(1000, self.destroy)


if __name__ == '__main__':
    app = TuringMachineSimulator()
    app.mainloop()
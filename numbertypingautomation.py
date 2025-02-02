import pyautogui
import time
import random
import threading
import customtkinter as ctk
from tkinter import messagebox

class BotApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Typing Bot by za Cubes")
        self.geometry("500x400")
        self.resizable(False, False) 
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")

        self.constraints = {}

        self.create_widgets()

    def create_widgets(self):
        frame = ctk.CTkFrame(self)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Centrar los widgets
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        ctk.CTkLabel(frame, text="Starting Number:").grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        self.start_entry = ctk.CTkEntry(frame)
        self.start_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(frame, text="Ending Number:").grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        self.end_entry = ctk.CTkEntry(frame)
        self.end_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        self.use_sleep_var = ctk.StringVar(value="off")
        self.use_sleep_switch = ctk.CTkSwitch(frame, text="Use Random Sleep", variable=self.use_sleep_var, onvalue="on", offvalue="off")
        self.use_sleep_switch.grid(row=2, columnspan=2, pady=5, sticky="ew")

        ctk.CTkLabel(frame, text="Min Sleep (seconds):").grid(row=3, column=0, padx=10, pady=5, sticky="ew")
        self.min_sleep_entry = ctk.CTkEntry(frame)
        self.min_sleep_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(frame, text="Max Sleep (seconds):").grid(row=4, column=0, padx=10, pady=5, sticky="ew")
        self.max_sleep_entry = ctk.CTkEntry(frame)
        self.max_sleep_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

        self.use_constraints_var = ctk.StringVar(value="off")
        self.use_constraints_switch = ctk.CTkSwitch(frame, text="Use Digit Constraints", variable=self.use_constraints_var, onvalue="on", offvalue="off")
        self.use_constraints_switch.grid(row=5, columnspan=2, pady=5, sticky="ew")

        self.constraints_button = ctk.CTkButton(frame, text="Add Constraints", command=self.add_constraints)
        self.constraints_button.grid(row=6, column=0, pady=5, sticky="ew")

        self.delete_constraints_button = ctk.CTkButton(frame, text="Delete Constraints", command=self.delete_constraints)
        self.delete_constraints_button.grid(row=6, column=1, pady=5, sticky="ew")

        self.constraints_label = ctk.CTkLabel(frame, text="Constraints: None")
        self.constraints_label.grid(row=7, columnspan=2, pady=5, sticky="ew")

        self.start_button = ctk.CTkButton(frame, text="Start Typing Bot", command=self.start_bot_thread)
        self.start_button.grid(row=8, column=0, pady=10, sticky="ew")

        self.end_button = ctk.CTkButton(frame, text="Stop Typing Bot", command=self.stop_bot)
        self.end_button.grid(row=8, column=1, pady=10, sticky="ew")

    def add_constraints(self):
        pos = ctk.CTkInputDialog(text="Enter the digit position:", title="Constraint Position").get_input()
        value = ctk.CTkInputDialog(text="Enter the value on this digit position:", title="Constraint Value").get_input()

        if pos and value:
            try:
                pos = int(pos)
                value = int(value)
                self.constraints[pos] = value
                constraints_text = ", ".join([f"{k}={v}" for k, v in self.constraints.items()])
                self.constraints_label.configure(text=f"Constraints: {constraints_text}")
            except ValueError:
                messagebox.showerror("Error", "Please enter valid integer values.")

    def delete_constraints(self):
        self.constraints.clear()
        self.constraints_label.configure(text="Constraints: None")

    def start_bot_thread(self):
        self.running = True
        bot_thread = threading.Thread(target=self.start_bot, daemon=True)
        bot_thread.start()

    def get_filtered_numbers(self, start, end, digit_constraints):
        filtered_numbers = []
        for number in range(start, end + 1):
            num_str = str(number).zfill(len(str(end)))
            valid = all(num_str[pos - 1] == str(value) for pos, value in digit_constraints.items())
            if valid:
                filtered_numbers.append(number)
        return filtered_numbers

    def start_bot(self):
        try:
            start = int(self.start_entry.get())
            end = int(self.end_entry.get())

            if self.use_sleep_var.get() == "on":
                min_sleep = float(self.min_sleep_entry.get())
                max_sleep = float(self.max_sleep_entry.get())
            else:
                min_sleep = max_sleep = 0

            numbers = self.get_filtered_numbers(start, end, self.constraints) if self.use_constraints_var.get() == "on" else list(range(start, end + 1))

            if not numbers:
                messagebox.showwarning("Warning", "No valid numbers found with the given constraints.")
                return

            messagebox.showinfo("Info", "Focus on the target window. Writing starts in 5 seconds.")
            time.sleep(5)

            for num in numbers:
                if not self.running:
                    break
                pyautogui.typewrite(str(num))
                pyautogui.press('enter')
                if self.use_sleep_var.get() == "on":
                    sleep_time = random.uniform(min_sleep, max_sleep)
                    time.sleep(sleep_time)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

    def stop_bot(self):
        self.running = False

if __name__ == "__main__":
    app = BotApp()
    app.mainloop()

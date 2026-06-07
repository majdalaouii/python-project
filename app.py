import tkinter as tk
from tkinter import messagebox
import random


class MiniHub:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mini Hub")
        self.root.geometry("600x450")
        self.root.configure(bg="white")
        self.root.resizable(False, False)

        self.player_name = ""
        self.secret_number = random.randint(1, 20)

        self.quiz_questions = [
            ("5 + 7 =", "12"),
            ("9 x 6 =", "54"),
            ("25 ÷ 5 =", "5"),
            ("15 - 8 =", "7"),
            ("12 x 4 =", "48")
        ]

        self.quiz_index = 0
        self.quiz_score = 0

        self.current_frame = None

        self.show_login()
        self.root.mainloop()

    # ---------------- UTIL ----------------
    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()

    def set_frame(self, func):
        self.clear()
        func()

    # ---------------- LOGIN ----------------
    def show_login(self):
        self.set_frame(self._login_ui)

    def _login_ui(self):
        tk.Label(self.root, text="Mini Hub",
                 font=("Arial", 24, "bold"), bg="white").pack(pady=30)

        tk.Label(self.root, text="Enter your name", bg="white").pack()

        self.name_entry = tk.Entry(self.root, font=("Arial", 12), width=25)
        self.name_entry.pack(pady=10)
        self.name_entry.bind("<Return>", lambda e: self.enter_app())

        tk.Button(self.root, text="Continue",
                  width=15, command=self.enter_app).pack(pady=10)

    def enter_app(self):
        name = self.name_entry.get().strip()

        if not name:
            messagebox.showwarning("Warning", "Please enter your name.")
            return

        self.player_name = name
        self.show_menu()

    # ---------------- MENU ----------------
    def show_menu(self):
        self.set_frame(self._menu_ui)

    def _menu_ui(self):
        tk.Label(self.root, text=f"Welcome {self.player_name}",
                 font=("Arial", 20, "bold"), bg="white").pack(pady=20)

        tk.Label(self.root, text="Choose an app", bg="white").pack(pady=10)

        tk.Button(self.root, text="Guess Game",
                  width=25, command=self.guess_screen).pack(pady=5)

        tk.Button(self.root, text="Calculator",
                  width=25, command=self.calc_screen).pack(pady=5)

        tk.Button(self.root, text="Math Quiz",
                  width=25, command=self.quiz_start).pack(pady=5)

        tk.Button(self.root, text="Exit",
                  width=25, command=self.root.destroy).pack(pady=20)

    # ---------------- BACK ----------------
    def back_to_menu(self):
        self.show_menu()

    # ---------------- GUESS GAME ----------------
    def guess_screen(self):
        self.set_frame(self._guess_ui)
        self.secret_number = random.randint(1, 20)

    def _guess_ui(self):
        tk.Label(self.root, text="Guess The Number",
                 font=("Arial", 20, "bold"), bg="white").pack(pady=20)

        tk.Label(self.root, text="Pick a number 1 - 20", bg="white").pack()

        self.guess_entry = tk.Entry(self.root, font=("Arial", 12))
        self.guess_entry.pack(pady=10)
        self.guess_entry.bind("<Return>", lambda e: self.check_guess())

        tk.Button(self.root, text="Check",
                  command=self.check_guess).pack()

        self.guess_result = tk.Label(self.root, text="", bg="white")
        self.guess_result.pack(pady=10)

        tk.Button(self.root, text="Back",
                  command=self.back_to_menu).pack(pady=10)

    def check_guess(self):
        try:
            val = int(self.guess_entry.get())
        except:
            self.guess_result.config(text="Enter a valid number")
            return

        if val < self.secret_number:
            self.guess_result.config(text="Too low")
        elif val > self.secret_number:
            self.guess_result.config(text="Too high")
        else:
            self.guess_result.config(text=f"Correct {self.player_name} 🎉")

    # ---------------- CALCULATOR ----------------
    def calc_screen(self):
        self.set_frame(self._calc_ui)

    def _calc_ui(self):
        tk.Label(self.root, text="Calculator",
                 font=("Arial", 20, "bold"), bg="white").pack(pady=20)

        self.calc_entry = tk.Entry(self.root, font=("Arial", 14))
        self.calc_entry.pack(pady=10)
        self.calc_entry.bind("<Return>", lambda e: self.calculate())

        tk.Button(self.root, text="Calculate",
                  command=self.calculate).pack(pady=10)

        self.calc_result = tk.Label(self.root, text="", bg="white")
        self.calc_result.pack()

        tk.Button(self.root, text="Back",
                  command=self.back_to_menu).pack(pady=20)

    def calculate(self):
        try:
            result = eval(self.calc_entry.get(), {"__builtins__": None}, {})
            self.calc_result.config(text=f"Result: {result}")
        except:
            self.calc_result.config(text="Invalid expression")

    # ---------------- QUIZ ----------------
    def quiz_start(self):
        self.quiz_index = 0
        self.quiz_score = 0
        self.quiz_screen()

    def quiz_screen(self): 
        self.set_frame(self._quiz_ui)

    def _quiz_ui(self):
        if self.quiz_index >= len(self.quiz_questions):
            tk.Label(self.root,
                     text=f"Finished!\nScore: {self.quiz_score}/{len(self.quiz_questions)}",
                     font=("Arial", 18, "bold"),
                     bg="white").pack(pady=50)

            tk.Button(self.root, text="Back",
                      command=self.back_to_menu).pack()
            return

        question, _ = self.quiz_questions[self.quiz_index]

        tk.Label(self.root, text=question,
                 font=("Arial", 16), bg="white").pack(pady=20)

        self.quiz_entry = tk.Entry(self.root, font=("Arial", 14))
        self.quiz_entry.pack(pady=10)
        self.quiz_entry.bind("<Return>", lambda e: self.check_quiz())

        tk.Button(self.root, text="Submit",
                  command=self.check_quiz).pack()

    def check_quiz(self):
        correct = self.quiz_questions[self.quiz_index][1]

        if self.quiz_entry.get().strip() == correct:
            self.quiz_score += 1
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", f"Wrong! Answer: {correct}")

        self.quiz_index += 1
        self.quiz_screen()


MiniHub()
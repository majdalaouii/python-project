import tkinter as tk
from tkinter import messagebox
import random


class MiniHub:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mini Hub")
        self.root.geometry("600x450")
        self.root.resizable(False, False)

        # Colors
        self.bg_color = "#0f172a"
        self.card_color = "#1e293b"
        self.btn_color = "#38bdf8"
        self.text_color = "white"

        self.root.configure(bg=self.bg_color)

        self.player_name = ""

        self.quiz_questions = [
            ("5 + 7 =", "12"),
            ("9 x 6 =", "54"),
            ("25 ÷ 5 =", "5"),
            ("15 - 8 =", "7"),
            ("12 x 4 =", "48")
        ]

        self.quiz_index = 0
        self.quiz_score = 0
        self.high_score = 0

        self.show_login()
        self.root.mainloop()

    # ================= SYSTEM =================
    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()

    def set_frame(self, func):
        self.clear()
        func()

    # ================= LOGIN =================
    def show_login(self):
        self.set_frame(self._login_ui)

    def _login_ui(self):
        main = tk.Frame(self.root, bg=self.card_color, padx=20, pady=20)
        main.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            main,
            text="Mini Hub",
            font=("Arial", 26, "bold"),
            bg=self.card_color,
            fg=self.text_color
        ).pack(pady=10)

        tk.Label(main, text="Enter your name", bg=self.card_color, fg=self.text_color).pack()

        self.name_entry = tk.Entry(main, justify="center")
        self.name_entry.pack(pady=10)

        tk.Button(
            main,
            text="START",
            bg=self.btn_color,
            fg="black",
            width=20,
            command=self.enter_app
        ).pack()

    def enter_app(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Warning", "Enter name")
            return
        self.player_name = name
        self.show_menu()

    # ================= MENU =================
    def show_menu(self):
        self.set_frame(self._menu_ui)

    def _menu_ui(self):
        main = tk.Frame(self.root, bg=self.bg_color)
        main.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            main,
            text=f"Welcome {self.player_name}",
            font=("Arial", 18, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        ).pack(pady=15)

        def btn(text, cmd):
            tk.Button(
                main,
                text=text,
                width=25,
                bg=self.card_color,
                fg=self.text_color,
                activebackground=self.btn_color,
                activeforeground="black",
                relief="flat",
                command=cmd
            ).pack(pady=6)   # 👈 مسافات بين الأزرار

        btn("🎯 Guess Game", self.guess_screen)
        btn("🧮 Calculator", self.calc_screen)
        btn("🧠 Quiz", self.quiz_start)
        btn("🎨 Drawing Pad", self.drawing_screen)
        btn("🧩 Block Blast", self.block_blast_screen)

        tk.Button(
            main,
            text="❌ Exit",
            width=25,
            bg="red",
            fg="white",
            relief="flat",
            command=self.root.destroy
        ).pack(pady=15)

    def back_to_menu(self):
        self.show_menu()

    # ================= GUESS GAME =================
    def guess_screen(self):
        self.secret = random.randint(1, 20)
        self.set_frame(self._guess_ui)

    def _guess_ui(self):
        tk.Label(self.root, text="Guess Number", fg=self.text_color, bg=self.bg_color, font=("Arial", 18)).pack(pady=20)

        self.guess_entry = tk.Entry(self.root)
        self.guess_entry.pack()

        self.guess_result = tk.Label(self.root, bg=self.bg_color, fg=self.text_color)
        self.guess_result.pack()

        tk.Button(self.root, text="Check", command=self.check_guess).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.back_to_menu).pack()

    def check_guess(self):
        try:
            v = int(self.guess_entry.get())
        except:
            self.guess_result.config(text="Enter number")
            return

        if v < self.secret:
            self.guess_result.config(text="Too low")
        elif v > self.secret:
            self.guess_result.config(text="Too high")
        else:
            self.guess_result.config(text="Correct!")

    # ================= CALCULATOR =================
    def calc_screen(self):
        self.set_frame(self._calc_ui)

    def _calc_ui(self):
        tk.Label(self.root, text="Calculator", fg=self.text_color, bg=self.bg_color, font=("Arial", 18)).pack(pady=20)

        self.calc_entry = tk.Entry(self.root)
        self.calc_entry.pack()

        self.calc_result = tk.Label(self.root, fg=self.text_color, bg=self.bg_color)
        self.calc_result.pack()

        tk.Button(self.root, text="=", command=self.calculate).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.back_to_menu).pack()

    def calculate(self):
        try:
            res = eval(self.calc_entry.get(), {"__builtins__": None}, {})
            self.calc_result.config(text=str(res))
        except:
            self.calc_result.config(text="Error")

    # ================= QUIZ =================
    def quiz_start(self):
        self.quiz_index = 0
        self.quiz_score = 0
        self.quiz_screen()

    def quiz_screen(self):
        self.set_frame(self._quiz_ui)

    def _quiz_ui(self):
        if self.quiz_index >= len(self.quiz_questions):
            tk.Label(
                self.root,
                text=f"Score: {self.quiz_score}/{len(self.quiz_questions)}",
                fg=self.text_color,
                bg=self.bg_color,
                font=("Arial", 18)
            ).pack(pady=40)

            tk.Button(self.root, text="Back", command=self.back_to_menu).pack()
            return

        q, _ = self.quiz_questions[self.quiz_index]

        tk.Label(self.root, text=q, fg=self.text_color, bg=self.bg_color, font=("Arial", 16)).pack(pady=20)

        self.quiz_entry = tk.Entry(self.root)
        self.quiz_entry.pack()

        tk.Button(self.root, text="Submit", command=self.check_quiz).pack(pady=5)

    def check_quiz(self):
        correct = self.quiz_questions[self.quiz_index][1]

        if self.quiz_entry.get().strip() == correct:
            self.quiz_score += 1
            messagebox.showinfo("OK", "Correct")
        else:
            messagebox.showinfo("NO", f"Answer: {correct}")

        self.quiz_index += 1
        self.quiz_screen()

    # ================= DRAWING =================
    def drawing_screen(self):
        self.set_frame(self._drawing_ui)

    def _drawing_ui(self):
        tk.Label(self.root, text="Drawing Pad", fg=self.text_color, bg=self.bg_color, font=("Arial", 18)).pack()

        self.canvas = tk.Canvas(self.root, width=500, height=280, bg="white")
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)

        tk.Button(self.root, text="Clear", command=lambda: self.canvas.delete("all")).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.back_to_menu).pack()

    def start_draw(self, e):
        self.x, self.y = e.x, e.y

    def draw(self, e):
        self.canvas.create_line(self.x, self.y, e.x, e.y, width=3)
        self.x, self.y = e.x, e.y

    # ================= BLOCK BLAST =================
    def block_blast_screen(self):
        self.set_frame(self._block_blast_ui)

    def _block_blast_ui(self):
        self.tk_board = [[0]*8 for _ in range(8)]
        self.score = 0
        self.game_over_flag = False

        tk.Label(self.root, text="Block Blast", fg=self.text_color, bg=self.bg_color, font=("Arial", 18)).pack()

        self.score_label = tk.Label(self.root, text="Score: 0", fg=self.text_color, bg=self.bg_color)
        self.score_label.pack()

        self.frame = tk.Frame(self.root, bg=self.bg_color)
        self.frame.pack()

        self.board = []

        for r in range(8):
            row = []
            for c in range(8):
                btn = tk.Button(self.frame, width=3, height=1,
                                command=lambda rr=r, cc=c: self.try_place(rr, cc))
                btn.grid(row=r, column=c)
                row.append(btn)
            self.board.append(row)

        self.shapes = [
            [(0,0)], [(0,0),(0,1)], [(0,0),(1,0)],
            [(0,0),(0,1),(0,2)], [(0,0),(1,0),(2,0)],
            [(0,0),(1,0),(1,1)], [(0,0),(0,1),(1,0),(1,1)]
        ]

        self.preview = tk.Label(self.root, fg=self.text_color, bg=self.bg_color, font=("Courier", 12))
        self.preview.pack(pady=10)

        tk.Button(self.root, text="Restart", command=self.block_blast_screen).pack()
        tk.Button(self.root, text="Back", command=self.back_to_menu).pack()

        self.new_shape()

    def new_shape(self):
        self.current_shape = random.choice(self.shapes)

        view = [[" " for _ in range(4)] for _ in range(4)]
        for r, c in self.current_shape:
            view[r][c] = "■"

        self.preview.config(text="\n".join("".join(row) for row in view))

        if not self.can_place_anywhere():
            self.game_over()

    def try_place(self, r, c):
        if self.game_over_flag:
            return

        for dr, dc in self.current_shape:
            nr, nc = r + dr, c + dc
            if nr >= 8 or nc >= 8 or self.tk_board[nr][nc] == 1:
                return

        for dr, dc in self.current_shape:
            nr, nc = r + dr, c + dc
            self.tk_board[nr][nc] = 1
            self.board[nr][nc].config(bg="black")

        self.score += 10
        self.score_label.config(text=f"Score: {self.score}")
        self.new_shape()

    def can_place_anywhere(self):
        for r in range(8):
            for c in range(8):
                for shape in self.shapes:
                    ok = True
                    for dr, dc in shape:
                        nr, nc = r + dr, c + dc
                        if nr >= 8 or nc >= 8 or self.tk_board[nr][nc] == 1:
                            ok = False
                            break
                    if ok:
                        return True
        return False

    def game_over(self):
        self.game_over_flag = True

        if self.score > self.high_score:
            self.high_score = self.score

        messagebox.showinfo("Game Over", f"Score: {self.score}\nHigh Score: {self.high_score}")


MiniHub()

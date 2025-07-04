import os
import tkinter as tk
from quiz_brain import QuizBrain
from tkinter import PhotoImage

THEME_COLOR = "#375362"
BASEDIR = os.path.dirname(__file__)


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title("Quzzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tk.Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file=f"{BASEDIR}/images/true.png")
        self.true_button = tk.Button(
            image=true_image,
            command=self.click_true,
            highlightthickness=0,
            borderwidth=0,
        )
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file=f"{BASEDIR}/images/false.png")
        self.false_button = tk.Button(
            image=false_image,
            command=self.click_false,
            highlightthickness=0,
            borderwidth=0,
        )
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You've reached the end of the quiz :)"
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def click_true(self):
        is_right = self.quiz.check_answer("True")
        self.get_feedback(is_right)

    def click_false(self):
        is_right = self.quiz.check_answer("False")
        self.get_feedback(is_right)

    def get_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

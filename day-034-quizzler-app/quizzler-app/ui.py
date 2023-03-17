import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
CORRECT_COLOR = "#81DB46"
WRONG_COLOR = "#DB4646"
QUESTION_FONT = ("Arial", 18)


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz_brain = quiz_brain
        self.n_questions = quiz_brain.n_questions
        self.score = 0
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=25, pady=25)

        # Canvas
        self.canvas = tk.Canvas()
        self.canvas.config(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=3, pady=(15, 30))
        self.text_question = self.canvas.create_text(
            150, 125, text="Hello whirled", font=QUESTION_FONT, width=285
        )

        # Buttons
        true_img = tk.PhotoImage(file="images/true.png")
        false_img = tk.PhotoImage(file="images/false.png")

        self.true_button = tk.Button(
            image=true_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.true_pressed,
        )

        self.true_button.grid(row=2, column=0)

        self.false_button = tk.Button(
            image=false_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.false_pressed,
        )
        self.false_button.grid(row=2, column=2)

        # Label
        self.score_label = tk.Label(
            text=f"Score: {self.score}/{self.n_questions}",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial", 15),
        )
        self.score_label.grid(row=0, column=1)
        self.next_question()
        self.window.mainloop()

    def add_score(self):
        self.score += 1
        self.score_label.config(text=f"Score: {self.score}/{self.n_questions}")

    def next_question(self) -> None:
        if self.quiz_brain.still_has_questions():
            text = self.quiz_brain.next_question()

        else:
            text = "You have reached the end of the quiz"

        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.text_question, text=text, font=QUESTION_FONT)

    def true_pressed(self) -> None:
        if self.quiz_brain.still_has_questions():
            is_correct = self.quiz_brain.check_answer("True")
            if is_correct:
                self.add_score()
            self.canvas_feedback(is_correct=is_correct)

    def false_pressed(self) -> None:
        if self.quiz_brain.still_has_questions():
            is_correct = self.quiz_brain.check_answer("False")
            if is_correct:
                self.add_score()

            self.canvas_feedback(is_correct=is_correct)

    def canvas_feedback(self, is_correct: bool) -> None:
        if is_correct:
            color = CORRECT_COLOR
        else:
            color = WRONG_COLOR

        self.canvas.config(bg=color)
        self.window.after(1000, self.next_question)

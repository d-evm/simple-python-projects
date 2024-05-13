from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(background=THEME_COLOR, padx=40, pady=40)

        self.score = Label(text="Score: 0")
        self.score.config(padx=10, pady=10, background=THEME_COLOR,
                          font=("Roboto", 14, "bold"), foreground='white')
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=460, height=400, bg="white")
        self.q_box = self.canvas.create_text(
            230, 200,
            text="The question comes here",
            font=("Belanosima", 20, "bold italic"),
            fill=THEME_COLOR,
            width=440)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true = PhotoImage(
            file=r"images\true.png")
        self.true_button = Button(
            image=true, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false = PhotoImage(
            file=r"images\false.png")
        self.false_button = Button(
            image=false, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_box, text=q_text)
        else:
            self.gameover()

    def true_pressed(self):
        is_correct = self.quiz.check_answer("true")
        self.give_feedback(is_correct)

    def false_pressed(self):
        is_correct = self.quiz.check_answer("false")
        self.give_feedback(is_correct)

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
            self.score.config(text=f"Score: {self.quiz.score}")

        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

    def gameover(self):
        self.score.destroy()
        self.false_button.destroy()
        self.true_button.destroy()
        self.canvas.itemconfig(
            self.q_box, text=f"GAME OVER\nScore: {self.quiz.score}/{len(self.quiz.question_list)}")

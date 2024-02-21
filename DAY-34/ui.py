from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50, padx=50)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="question", font=("Arial", 20, "italic"))
        true_image = PhotoImage(file = r"C:\Users\koush\PycharmProjects\days100code\DAY-34\images\true.png")
        self.correct_but = Button(image=true_image, highlightthickness=0, command=self.sent_true)
        self.correct_but.grid(row=2, column=0)
        false_image = PhotoImage(file = r"C:\Users\koush\PycharmProjects\days100code\DAY-34\images\false.png")
        self.wrong_but = Button(image=false_image, highlightthickness=0, command=self.sent_false)
        self.wrong_but.grid(row=2, column=1)
        self.score_label = Label(text = f"Score:0", bg = THEME_COLOR, font=("Arial", 20, "italic"))
        self.score_label.grid(row=0, column=1)
        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text =q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="YOU ARE DONE!!!")
    def sent_true(self):
        ans = self.quiz.check_answer("True")
        if ans:
            score = self.quiz.score
            self.score_label.config(text = f"Score:{score}")

        self.give_feedback(ans)


    def sent_false(self):
        ans = self.quiz.check_answer("False")
        if ans:
            score = self.quiz.score
            self.score_label.config(text=f"Score:{score}")
        self.give_feedback(ans)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question())

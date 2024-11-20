import tkinter as tk

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_data: QuizBrain):
        self.quiz = quiz_data
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = tk.Canvas(width=350, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(row=1,column=0,columnspan=2,padx=15,pady=20)
        self.score_label = tk.Label(text=f"Score: 0",bg=THEME_COLOR,font=("Arial",12,"bold"),fg="white")
        self.score_label.grid(row=0,column=1,pady=20)
        self.question_canvas = self.canvas.create_text(175, 125, text="Question", font=("Arial", 18, "italic"), width=300)
        self.true_check_img = tk.PhotoImage(file="images/true.png")
        self.false_x_img = tk.PhotoImage(file="images/false.png")
        self.true_button = tk.Button(image=self.true_check_img,highlightthickness=0,borderwidth=0,command=self.true_button_clicked)
        self.true_button.grid(row=2,column=0,pady=20)
        self.false_button = tk.Button(image=self.false_x_img,highlightthickness=0,borderwidth=0,command=self.false_button_clicked)
        self.false_button.grid(row=2,column=1,pady=20)
        self.update_question()
        self.window.mainloop()

    def update_score(self):
        score = self.quiz.score
        self.score_label.config(text=f"Score: {score}")


    def update_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_canvas,text=f"{q_text}")
            self.canvas.config(bg="white")
        else:
            self.canvas.itemconfig(self.question_canvas,text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button_clicked(self):
        self.check_answer("True")
        self.update_score()
    def false_button_clicked(self):
        self.check_answer("False")
        self.update_score()

    def check_answer(self, user_answer):
        self.disable_buttons()
        correct_answer = self.quiz.correct_answer
        print(correct_answer)
        if self.quiz.check_answer(user_answer):
            correct_or_incorrect: str = "Correct!"
            bg = "#29EDA7"
        else:
            correct_or_incorrect: str = "Incorrect!"
            bg = "#FF685F"
        self.canvas.itemconfig(self.question_canvas,text=f"Thats is {correct_or_incorrect} answer is: {correct_answer}")
        self.canvas.config(bg=bg)
        self.window.update_idletasks()
        self.window.after(3000, self.enable_buttons)


    def disable_buttons(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")


    def enable_buttons(self):
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")
        self.update_question()

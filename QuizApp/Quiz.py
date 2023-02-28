import tkinter as tk
import csv
import random


class Quiz:
    def __init__(self, fr):

        self.question_text = tk.StringVar()
        self.question_text.set("")
        self.question_label = tk.Label(fr, textvariable=self.question_text, font=("Arial", 20), bg="white", fg="black")
        self.question_label.pack(pady=20)

        self.answer_text = tk.StringVar()
        self.answer_text.set("")
        self.answer_label = tk.Label(fr, textvariable=self.answer_text, font=("Arial", 20), bg="white", fg="black")
        self.answer_label.pack(pady=20)

        self.answer_buttons = []
        self.answer_button_texts = []
        self.answer_button_texts.append(tk.StringVar())
        self.answer_button_texts[0].set("")
        self.answer_buttons.append(tk.Button(fr, textvariable=self.answer_button_texts[0], font=("Arial", 20), bg="white", fg="black", command=lambda: self.answer_button_click(self.answer_button_texts[0])))
        self.answer_buttons[0].pack(pady=10)

        self.answer_button_texts.append(tk.StringVar())
        self.answer_button_texts[1].set("")
        self.answer_buttons.append(tk.Button(fr, textvariable=self.answer_button_texts[1], font=("Arial", 20), bg="white", fg="black", command=lambda: self.answer_button_click(self.answer_button_texts[1])))
        self.answer_buttons[1].pack(pady=10)

        self.answer_button_texts.append(tk.StringVar())
        self.answer_button_texts[2].set("")
        self.answer_buttons.append(tk.Button(fr, textvariable=self.answer_button_texts[2], font=("Arial", 20), bg="white", fg="black", command=lambda: self.answer_button_click(self.answer_button_texts[2])))
        self.answer_buttons[2].pack(pady=10)

        self.answer_button_texts.append(tk.StringVar())
        self.answer_button_texts[3].set("")
        self.answer_buttons.append(tk.Button(fr, textvariable=self.answer_button_texts[3], font=("Arial", 20), bg="white", fg="black", command=lambda: self.answer_button_click(self.answer_button_texts[3])))
        self.answer_buttons[3].pack(pady=10)

        self.next_question_button = tk.Button(fr, text="Next", font=("Arial", 20), bg="white", fg="black", command=self.next_question)
        self.next_question_button.pack(pady=30)

        self.questions = []
        self.answers = []
        self.correct_answers = []
        self.current_question = 0

        self.score = 0

    def load_quiz(self, filename):
        self.questions.clear()
        self.answers.clear()
        self.correct_answers.clear()
        with open(filename, "r", encoding='utf-8-sig') as questions_file:
            reader = csv.reader(questions_file)
            for row in reader:
                self.questions.append(row[0])
                self.answers.append(row[1:5])
                self.correct_answers.append(row[1])

    def next_question(self):
        if self.current_question < len(self.questions):
            self.question_text.set(self.questions[self.current_question])
            self.answer_text.set("")

            all_answers_for_current_q = self.answers[self.current_question]
            random.shuffle(all_answers_for_current_q)
            i = 0
            for an_ans in all_answers_for_current_q:
                self.answer_button_texts[i].set(an_ans)
                i += 1
            self.current_question += 1
        else:
            self.question_text.set("")
            self.answer_text.set("You've finished all the questions! \n "
                                 "Hope you enjoyed revising, revise again soon!\n\nYou answered correctly: "
                                 +  str(self.score) + "/" + str(len(self.questions)))
            self.answer_buttons[0].pack_forget()
            self.answer_buttons[1].pack_forget()
            self.answer_buttons[2].pack_forget()
            self.answer_buttons[3].pack_forget()
            self.next_question_button.pack_forget()

    def answer_button_click(self, ans):
        if ans.get() in self.correct_answers:
            self.answer_text.set("Correct!")
            self.score += 1
        else:
            self.answer_text.set("Incorrect!")

    def restart_quiz(self):
        self.current_question = 0
        self.score = 0
        self.answer_buttons[0].pack(pady=10)
        self.answer_buttons[1].pack(pady=10)
        self.answer_buttons[2].pack(pady=10)
        self.answer_buttons[3].pack(pady=10)
        self.next_question_button.pack(pady=30)



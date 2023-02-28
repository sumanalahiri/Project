from tkinter import *
import csv


class FlashCards:

    def __init__(self, fl_frame):
        self.subject_file = ""
        self.reload = False
        self.mydict = {}
        self.fl_frame = fl_frame

        #add flashcard widgets
        self.add_fc_label = Label(fl_frame, text='Add a flashcard', font=("Arial", 20))

        self.question_label = Label(fl_frame, text='Question:')
        self.question_txt = Text(fl_frame, height=1, width=80, borderwidth=3, relief="sunken")

        self.right_ans_label = Label(fl_frame, text='Correct answer:')
        self.right_ans_txt = Text(fl_frame, height=1, width=80, borderwidth=3, relief="sunken")

        self.wrong_ans1_label = Label(fl_frame, text='Wrong answer 1:')
        self.wrong_ans1_txt = Text(fl_frame, height=1, width=80, borderwidth=3, relief="sunken")
        self.wrong_ans2_label = Label(fl_frame, text='Wrong answer 2:')
        self.wrong_ans2_txt = Text(fl_frame, height=1, width=80, borderwidth=3, relief="sunken")
        self.wrong_ans3_label = Label(fl_frame, text='Wrong answer 3:')
        self.wrong_ans3_txt = Text(fl_frame, height=1, width=80, borderwidth=3, relief="sunken")

        self.insert_but = Button(fl_frame, text='Add', command=self.insert_to_file)

        self.added_text = StringVar()
        self.added_text.set("")
        self.added_label = Label(fl_frame, textvariable=self.added_text, font=("Arial", 20))
        self.added_label.pack()

        #view flashcard widgets
        self.view_flc_label = Label(fl_frame, text='View flashcards')
        self.view_flc_label.pack()

        self.question_listbox = Listbox(fl_frame, width=60)
        self.question_listbox.pack()
        self.reveal_but = Button(fl_frame, text='Reveal answer', command=self.reveal_answer)
        self.reveal_but.pack()

        self.ans_label = Label(fl_frame, text='Answer: ')
        self.ans_label.pack()
        self.ans_reveal_txt = Text(fl_frame, height=10, width=70, borderwidth=3, relief="sunken")
        self.ans_reveal_txt.pack()

    def initialise_flashcard(self, filename):
        self.subject_file = filename

    def load_cards(self, filename):
        file = open(filename, encoding='utf-8-sig')
        reader = csv.reader(file)
        self.mydict.clear()
        self.mydict = {rows[0]: rows[1] for rows in reader}
        file.close()

    def load_question_listbox(self):
        self.question_listbox.delete(0, END)
        insert_questions = list(self.mydict.keys())
        for q in insert_questions:
            self.question_listbox.insert(0, q)
        self.question_listbox.select_set(0)

    def clear_text(self):
        self.ans_reveal_txt.delete('1.0', 'end')
        self.question_txt.delete('1.0', 'end')
        self.right_ans_txt.delete('1.0', 'end')
        self.wrong_ans1_txt.delete('1.0', 'end')
        self.wrong_ans2_txt.delete('1.0', 'end')
        self.wrong_ans3_txt.delete('1.0', 'end')

    def reveal_answer(self):
        self.clear_text()
        selection = self.question_listbox.get(self.question_listbox.curselection())
        self.ans_reveal_txt.insert(END, self.mydict.get(selection))

    def hide_view_flashcard(self):
        self.view_flc_label.pack_forget()
        self.question_listbox.pack_forget()
        self.reveal_but.pack_forget()
        self.ans_label.pack_forget()
        self.ans_reveal_txt.pack_forget()

    def show_view_flashcard(self):
        self.view_flc_label.pack()
        self.question_listbox.pack()
        self.reveal_but.pack()
        self.ans_label.pack()
        self.ans_reveal_txt.pack()

    def hide_add_flashcard(self):
        self.add_fc_label.pack_forget()
        self.question_label.place_forget()
        self.question_txt.place_forget()
        self.right_ans_label.place_forget()
        self.right_ans_txt.place_forget()
        self.wrong_ans1_label.place_forget()
        self.wrong_ans1_txt.place_forget()
        self.wrong_ans2_label.place_forget()
        self.wrong_ans2_txt.place_forget()
        self.wrong_ans3_label.place_forget()
        self.wrong_ans3_txt.place_forget()
        self.insert_but.place_forget()
        self.added_label.pack_forget()

    def show_add_flashcard(self):
        self.add_fc_label.pack()
        self.question_label.place(x=100, y=100)
        self.question_txt.place(x=230, y=100)
        self.right_ans_label.place(x=100, y=150)
        self.right_ans_txt.place(x=230, y=150)
        self.wrong_ans1_label.place(x=100, y=200)
        self.wrong_ans1_txt.place(x=230, y=200)
        self.wrong_ans2_label.place(x=100, y=250)
        self.wrong_ans2_txt.place(x=230, y=250)
        self.wrong_ans3_label.place(x=100, y=300)
        self.wrong_ans3_txt.place(x=230, y=300)
        self.insert_but.place(x=480, y=350)

    def insert_to_file(self):
        add_row = []
        add_row.append(str(self.question_txt.get("1.0", END)).rstrip())
        add_row.append(str(self.right_ans_txt.get("1.0", END)).rstrip())
        add_row.append(str(self.wrong_ans1_txt.get("1.0", END)).rstrip())
        add_row.append(str(self.wrong_ans2_txt.get("1.0", END)).rstrip())
        add_row.append(str(self.wrong_ans3_txt.get("1.0", END)).rstrip())

        with open(self.subject_file, 'a') as my_file:
            writer = csv.writer(my_file)
            writer.writerow(add_row)

        self.hide_add_flashcard()
        self.added_text.set(("Flashcard has been added."))
        self.reload = True
        self.added_label.pack()

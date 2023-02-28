from tkinter import *
from Quiz import Quiz
from FlashCards import FlashCards


class FrameController:
    def __init__(self, master):
        topic_frame = Frame(master)
        menu_frame = Frame(master)
        view_frame = Frame(master)
        quiz_frame = Frame(master)

        self.selected_topic = ""

        # stack up the frames
        for frame in (topic_frame, menu_frame, view_frame, quiz_frame):
            frame.grid(row=0, column=0, sticky='nesw')

        Label(topic_frame, text='Revision Helper',font=("Arial", 30)).pack()
        Label(topic_frame, text='Choose a subject:',font=("Arial", 20)).pack()
        self.subjects = {'Computing Technology':'computing.csv',
                        'Biology': 'biology.csv'}
        insert_subjects = StringVar(value=list(self.subjects.keys()))
        self.topic_lbox = Listbox(topic_frame, listvariable=insert_subjects, width=30)
        self.topic_lbox.select_set(0)
        self.topic_lbox.pack()

        go_but = Button(topic_frame, text='Go', font=("Arial", 30), command=lambda: self.select_topic(menu_frame))
        go_but.pack()

        self.img = PhotoImage(file="revise.gif")
        img_label = Label(topic_frame, image=self.img)
        img_label.pack(side="bottom", fill="both", expand="yes")

        self.error_text = StringVar()
        self.error_text.set("")
        self.error_label = Label(topic_frame, textvariable=self.error_text)
        self.error_label.pack()

        lb_frame = LabelFrame(menu_frame, text='Main Menu')
        lb_frame.grid(row=1, column=1, padx=80, pady=20)

        sel_label = Label(lb_frame, text='Selected subject:', font=("Arial", 30))
        sel_label.grid(row=0, column=0, ipadx=10, ipady=10, sticky='w')

        self.subj_text = StringVar()
        self.subj_text.set("")
        self.sub_label = Label(lb_frame, textvariable=self.subj_text, font=("Arial", 30))
        self.sub_label.grid(row=0, column=1, ipadx=20, ipady=20, sticky='w')

        add_fc_but = Button(lb_frame, text='Add Flashcard', font=("Arial", 30), command=lambda: self.show_add_flashcard(view_frame))
        add_fc_but.grid(row=1, column=1, ipadx=20, ipady=10, sticky='w')

        flashcard_but = Button(lb_frame, text='View flashcards', font=("Arial", 30), command=lambda: self.init_view_flashcards(view_frame))
        flashcard_but.grid(row=2, column=1, ipadx=20, ipady=10, sticky='w')

        quiz_but = Button(lb_frame, text='Quiz', font=("Arial", 30), command=lambda: self.start_quiz(quiz_frame))
        quiz_but.grid(row=3, column=1, ipadx=20, ipady=10, sticky='w')

        #load flashcards
        self.flash_Card = FlashCards(view_frame)
        #load the quiz screen
        self.qz = Quiz(quiz_frame)

        l_frame2 = LabelFrame(menu_frame)
        l_frame2.grid(row=0, column=0, padx=20, pady=20)

        back_but = Button(l_frame2, text='Back', command=lambda: self.raise_frame(topic_frame))
        back_but.grid(row=1, column=1, ipadx=10, ipady=10, sticky='w')


        Button(view_frame, text='Home', command=lambda: self.raise_frame(menu_frame)).pack(side='bottom')
        Button(quiz_frame, text='Home', command=lambda: self.restart_quiz(menu_frame)).pack(side='bottom')

        self.raise_frame(topic_frame)

    def select_topic(self, mframe):
        try:
            self.error_text.set("")
            self.selected_topic = self.topic_lbox.get(self.topic_lbox.curselection())
            self.subj_text.set(self.selected_topic)
            self.load_questions()
            self.raise_frame(mframe)
        except Exception as e:
            self.error_text.set("Please select a subject!")
            print (e)

    def load_questions(self):
        self.flash_Card.initialise_flashcard(self.subjects.get(self.selected_topic))
        self.flash_Card.load_cards(self.subjects.get(self.selected_topic))
        self.qz.load_quiz(self.subjects.get(self.selected_topic))

    def init_view_flashcards(self, vframe):
        self.flash_Card.load_question_listbox()
        self.flash_Card.hide_add_flashcard()
        self.flash_Card.show_view_flashcard()
        self.flash_Card.clear_text()
        #self.flash_Card.initialise_flashcard(self.subjects.get(self.selected_topic))
        #self.flash_Card.load_cards(self.subjects.get(self.selected_topic))
        self.raise_frame(vframe)

    def show_add_flashcard(self, vframe):
        self.flash_Card.hide_view_flashcard()
        self.flash_Card.show_add_flashcard()
        self.flash_Card.clear_text()
        #self.flash_Card.initialise_flashcard(self.subjects.get(self.selected_topic))
        self.raise_frame(vframe)

    def start_quiz(self, qframe):
        #self.qz.load_quiz(self.subjects.get(self.selected_topic))
        self.qz.next_question()
        self.raise_frame(qframe)

    def restart_quiz(self, tframe):
        self.qz.restart_quiz()
        self.raise_frame(tframe)

    def raise_frame(self, frame):
        if self.flash_Card.reload == True:
            self.load_questions()
            self.flash_Card.reload = False
        frame.tkraise()







from tkinter import *
from tkinter import messagebox as mb
import json


root = Tk()
root.geometry('800x500')
root.title('Carbon Footprint Calculator')
bg = PhotoImage(file="background.png")

canvas1 = Canvas(root, highlightthickness=0)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg, anchor = "nw")
canvas1.configure(bg='black')


class Quiz():

    def __init__(self):
        self.question_no = 0
        self.carbon_points = 0
        self.option_select = IntVar()
        self.option = self.radio_btns()
        self.quest = self.question(self.question_no)
        self.display_option(self.question_no)
        self.buttons()
    
    def question(self, question_no):
        t = Label(root, text="Carbon Footprint", width=50, bg="black", fg="white", font="Verdana 20 underline")
        t.place(x=0, y=5)
        question_no = Label(root, text = "", wraplength=645, bg="black", fg="white", font=("times", 18, "bold"), anchor="w")
        question_no.place(x=80, y=100)
        return question_no

    def radio_btns(self):
        val = 0
        y_pos = 150
        btn_list = []
        while val < len(options[self.question_no]):
            btn = Radiobutton(root, text=options[self.question_no][val], variable=self.option_select, fg="green", value=val+1, font=("times", 16, "bold"), bg="black", selectcolor="black", activebackground="black", activeforeground="black")
            btn_list.append(btn)
            btn.place(x=100, y=y_pos)
            val += 1
            y_pos += 40
        return btn_list

    def display_option(self, question_no):
        val = 0
        self.option_select.set(0)
        self.quest['text'] = questions[question_no]
        for opt in options[question_no]:
            self.option[val]['text'] = opt
            val += 1

    def buttons(self):
        next_btn = Button(root, text="Next", command=self.next, width=10, bg="#666666", fg="white", font=("times", 16, "bold"))
        next_btn.place(x=650, y=440)
        quit_btn = Button(root, text="Quit", command=root.destroy, width=5, bg="red", fg="white", font=("times", 12, "bold"))
        quit_btn.place(x=735, y=48)

    def points_calc(self, question_no):
        self.carbon_points += points[question_no][self.option_select.get()-1]

    def next(self):
        self.points_calc(self.question_no)
        self.question_no += 1
        if self.question_no == len(questions):
            self.display_result()
            root.destroy()
        else:
            self.display_option(self.question_no)
    
    def carbon(self):
        return self.carbon_points

    def display_result(self):
        if self.carbon_points >= 50:
            res = "You are making a major impact on the environment"
        else:
            res = "You are making a very small impact on the environment"
        mb.showinfo("Result", f"Your Carbon Points : {self.carbon_points}\n{res}")


with open('data.json') as file:
    data = json.load(file)

questions = data['questions']
options = data['options']
points = data['points']

quiz = Quiz()

root.mainloop()

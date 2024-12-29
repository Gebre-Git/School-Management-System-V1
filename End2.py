from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import csv


def mai():

    global system
    system = Tk()
    system.title("STEM Management System")
    system.geometry("1600x1600")
    system.config(bg="black")

    menu_bar = Menu(system)
    system.config(menu=menu_bar)
    filemenu = Menu(menu_bar, font=("Lucida Calligraphy", 20))
    menu_bar.add_cascade(label="Info", menu=filemenu)
    filemenu.add_command(label="Help", command=help_me)
    filemenu.add_command(label="Quit", command=quit)
    background_image = PhotoImage(file="su.PNG")
    background_label = Label(system, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    te = Label(system, text="Wellcome To Our System ", font=("Algerian", 40), fg="green", bg="red", relief=SUNKEN,
               bd=10)
    te.pack()

    student_lable = Label(system, text="Students Management System",
                          font=("Algerian", 20), relief=SUNKEN, bd=10, fg="white", bg="black")
    student_lable.place(x=150, y=150)
    student_image = PhotoImage(file="stud.png")
    students = Button(system,
                      bg="green",
                      bd=20, relief=RAISED,
                      pady=100, padx=50,
                      image=student_image,
                      command=pin_students)
    students.place(x=100, y=200)
    tea = Label(system, text="teachers management system", font=("Algerian", 20), relief=SUNKEN, bd=10, fg="white",
                bg="black")
    tea.place(x=620, y=150)
    teacher_image = PhotoImage(file="Capture.PNG")
    teachers = Button(system,
                      bg="blue",
                      bd=20, relief=RAISED, image=teacher_image,
                      pady=100, padx=50,
                      command=pin_teachers)
    teachers.place(x=630, y=200)

    system.mainloop()
mai()

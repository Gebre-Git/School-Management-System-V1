import csv
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

# Creating a function to register new student
def new_student():
    global registration
    # destroying pre  existing tkinter page
    stud.destroy()
    registration = Tk()
    registration.geometry("1200x1200")
    registration.config(bg="brown")
    background_ima = PhotoImage(file="regi.PNG")
    background_lab = Label(registration, image=background_ima)
    background_lab.place(x=0, y=0, relwidth=1, relheight=1)
    registration_lable = Label(registration, text="Please fill all required things", font=("Lucida Calligraphy", 20),
                bd=5, relief=RAISED, bg="#CCFFFF", padx=10000, pady=20)
    registration_lable.pack()

    def register_employee():
        namer = name_e.get().strip()
        ager = age_e.get().strip()
        grader = grade_e.get().strip()
        kebeler = kebele_e.get().strip()
        phoner = phone_e.get().strip()
        emergencyr = emergency_e.get().strip()
        if (namer == "" or ager == "" or grader == "" or kebeler == "" or phoner == "" or emergencyr == ""):
            messagebox.showwarning("Error", "There is unfilled place. Please fill it.")
            return
        found =False
        student_data = [namer, ager, grader, kebeler, phoner, emergencyr]
        filename = f"grade{grader}.csv"
        for grade in range(9, 13):
            filename = f"grade{grade}.csv"
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if (row[0].lower() == namer.lower() and row[1] == ager.lower() and row[2].lower() == grader.lower() and row[3].lower() == kebeler.lower() and row[4].lower() == phoner.lower() and row[5].lower() == emergencyr.lower()) :
                        found = True
                        break
        if found:
            messagebox.showwarning("ALREADY EXIST","The student already exist")
        else:
            with open(filename, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(student_data)

            messagebox.showinfo("Success", "The student registered successfully.")

    def key_event(event):
        register_employee()

    registration.bind("<Return>", key_event)
    reg = Frame(registration, width=10, height=5)
    reg.place(x=400, y=135)
    name = Label(reg, text="Name: ", font=("Lucida Calligraphy", 15), )
    name_e = Entry(reg, font=("Comic Sans MS", 15))
    age = Label(reg, text="Age: ", font=("Lucida Calligraphy", 15))
    age_e = Entry(reg, font=("Comic Sans MS", 15))
    grade = Label(reg, text="Grade", font=("Lucida Calligraphy", 15))
    grade_e = Entry(reg, font=("Comic Sans MS", 15))
    kebele = Label(reg, text="Kebele", font=("Lucida Calligraphy", 15))
    kebele_e = Entry(reg, font=("Comic Sans MS", 15))
    phone = Label(reg, text="phone.No", font=("Lucida Calligraphy", 15))
    phone_e = Entry(reg, font=("Comic Sans MS", 15))
    emergency = Label(reg, text="emergency", font=("Lucida Calligraphy", 15))
    emergency_e = Entry(reg, font=("Comic Sans MS", 15))
    register = Button(reg, text="register", font=("Lucida Calligraphy", 15), command=register_employee)
    name.grid(row=1, column=1)
    name_e.grid(row=1, column=2)
    age.grid(row=2, column=1)
    age_e.grid(row=2, column=2)
    grade.grid(row=3, column=1)
    grade_e.grid(row=3, column=2)
    kebele.grid(row=4, column=1)
    kebele_e.grid(row=4, column=2)
    phone.grid(row=5, column=1)
    phone_e.grid(row=5, column=2)
    emergency.grid(row=6, column=1)
    emergency_e.grid(row=6, column=2)
    register.grid(row=7, column=1)

    def back_1():
        registration.destroy()
        main()

    ba = Button(registration, text="back", command=back_1, font=("Algerian", 20), bg="black",fg="green")
    ba.place(x=600, y=600)
    registration.mainloop()


def student_search():
    st_search = Tk()
    stud.destroy()
    st_search.title("searching for students")
    st_search.geometry("1200x1200")

    def finder():
        found = False
        ent = search_entry.get().strip()
        student_info = ""

        for grade in range(9, 13):
            filename = f"grade{grade}.csv"
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0].lower() == ent.lower():
                        student_info += f"Name:    {row[0]}\n"
                        student_info += f"Age:     {row[1]}\n"
                        student_info += f"Grade:   {row[2]}\n"
                        student_info += f"Kebele:  {row[3]}\n"
                        student_info += f"Phone.No:{row[4]}\n"
                        student_info += f"parent:  {row[5]}\n\n"
                        found = True
                        break
        q = Label(st_search, text=student_info, font=("Comic Sans MS", 20))
        q.pack()

        if not found:
            messagebox.showwarning("NOT FOUND", f'There is no one in this school with name {ent} ')

    def key_event(event):
        finder()

    st_search.bind("<Return>", key_event)
    st_search.config(bg="#FAF0DD")
    sa = Label(st_search, text="write the student name please", font=("Lucida Calligraphy", 20),width=500,height=2,bg="#00BFFF")
    sa.pack()
    frame = Frame(st_search)
    frame.pack()
    search_entry = Entry(frame, width=50, font=("Comic Sans MS", 20))
    search_entry.pack(side=LEFT)
    na = Button(frame, text="🔎", font=("Lucida Calligraphy", 20), command=finder)
    na.pack(side=LEFT)

    def back_2():
        st_search.destroy()
        main()

    ad = Button(st_search, text="back", command=back_2, font=("Algerian", 20))
    ad.place(x=600, y=600)
    st_search.mainloop()


def search_by_grade():
    search_grade = Tk()
    search_grade.geometry("1200x1200")
    search_grade.config(bg="#FAF0DD")
    def finder_grade():
        entry = search_grade_entry.get().strip()
        student_grade_info = ""
        found_grade = False

        for grade in range(9, 13):
            filename = f"grade{grade}.csv"
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                y = 1
                for row in reader:
                    if row[2] == entry:
                        student_grade_info += f"{y}: {row[0]}\n"
                        found_grade = True
                    y += 1
        if entry=="":
            messagebox.showerror("NO NAME","You didn't write anything")
        elif found_grade:
            search.destroy()
            search_grade_entry.destroy()
            sear_g.destroy()
            q = Label(search_grade, text=student_grade_info,bg="white", font=("Comic Sans MS", 20),padx=2)
            q.pack()
        else:
            messagebox.showwarning("NOT FOUND", f"There are no students in grade {entry}")

    def key_event(event):
        finder_grade()

    search_grade.bind("<Return>", key_event)
    sear_g = Label(search_grade, text="Write the student grade, please:",width=500,height=2,bg="#00BFFF", font=("Lucida Calligraphy", 20))
    sear_g.pack()
    frame_gr = Frame(search_grade)
    frame_gr.pack()
    search_grade_entry = Entry(frame_gr, width=50, font=("Comic Sans MS", 20))
    search_grade_entry.pack(side=LEFT)
    search = Button(frame_gr, text="🔎",bg="white", font=("Lucida Calligraphy", 20), command=finder_grade)
    search.pack(side=LEFT)

    search_grade.mainloop()


def help_me():
    messagebox.showinfo("It will help you!!!",
                        '''Enter the first button to enter into STEM student management system \n Enter the second to enter in to Teachers management system''')


def student_roster():
    stud.destroy()
    stros = Tk()
    stros.geometry("1000x800")
    background_img = PhotoImage(file="2img.PNG")
    background_label = Label(stros, image=background_img)
    background_label.place(x=0, y=0)

    def roster_view_grade():
        def finde():
            entr = g.get().strip()
            student_grade_roster = ""
            found_grade = False
            for grade in range(9, 13):
                filename = f"grade {grade} roster.csv"
                with open(filename, 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if row[1] == entr:
                            if (x.get() == 0):
                                student_grade_roster += f"Name:-------- {row[0]}\n"
                                student_grade_roster += f"grade-------- {row[1]}\n"
                                student_grade_roster += f"biology:----- {row[2]}\n"
                                student_grade_roster += f"chemistry:--- {row[3]}\n"
                                student_grade_roster += f"physics:----- {row[4]}\n"
                                student_grade_roster += f"Mathematics:- {row[5]}\n"
                                student_grade_roster += f"English:----- {row[6]}\n"
                                student_grade_roster += f"ICT:--------- {row[7]}\n"
                                student_grade_roster += f"Average:----- {row[8]}\n"
                                if float(row[8]) >= 80:
                                    student_grade_roster += "PASSED!!!!!\n\n"

                                else:
                                    student_grade_roster += "FAILED.This can't continue here\n\n"
                            elif (x.get() == 1):
                                student_grade_roster += f"Name:-------- {row[0]}\n"
                                student_grade_roster += f"Average:----- {row[8]}\n"
                                if float(row[8]) >= 80:
                                    student_grade_roster += "PASSED!!!!!\n\n"

                                else:

                                    student_grade_roster += "FAILED.This can't continue here\n\n"
                            found_grade = True

            if found_grade:
                save_roster.destroy()
                see_roster.destroy()
                fr.destroy()
                enter.destroy()
                canvas = Canvas(stros)
                canvas.pack(side='left', fill='both', expand=True)

                # Add a scrollbar to the canvas
                scrollbar = ttk.Scrollbar(stros, orient='vertical', command=canvas.yview)
                scrollbar.pack(side='right', fill='y')

                # Configure the canvas to use the scrollbar
                canvas.configure(yscrollcommand=scrollbar.set)

                # Create a frame inside the canvas for scrollable content
                scrollable_frame = ttk.Frame(canvas)

                # Add the scrollable frame to the canvas
                canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')

                y = Label(scrollable_frame, text=student_grade_roster, font=("Comic Sans MS", 15))
                y.pack()
                # b = Button(scrollable_frame, text="Quit",font=("Algerian",20), command=quit)
                # b.pack()
                scrollable_frame.update_idletasks()
                canvas.configure(scrollregion=canvas.bbox("all"))

            else:
                messagebox.showwarning("NOT FOUND", f"There are no students in grade {entr}")

        def finderr():
            entry1 = n.get().strip()
            student_name_roster = ""
            found_name = False
            for grade in range(9, 13):
                filename = f"grade {grade} roster.csv"
                with open(filename, 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if row[0] == entry1:
                            if (x.get() == 0):
                                student_name_roster += f"Name:-------- {row[0]}\n"
                                student_name_roster += f"grade-------- {row[1]}\n"
                                student_name_roster += f"biology:----- {row[2]}\n"
                                student_name_roster += f"chemistry:--- {row[3]}\n"
                                student_name_roster += f"physics:----- {row[4]}\n"
                                student_name_roster += f"Mathematics:- {row[5]}\n"
                                student_name_roster += f"English:----- {row[6]}\n"
                                student_name_roster += f"ICT:--------- {row[7]}\n"
                                student_name_roster += f"Average:----- {row[8]}\n"
                                if float(row[8]) >= 80:
                                    student_name_roster += "PASSED!!!!!\n\n"
                                else:
                                    student_name_roster += "FAILED.This student can't continue here\n\n"
                            elif (x.get() == 1):
                                student_name_roster += f"Name:-------- {row[0]}\n"
                                student_name_roster += f"Average:----- {row[8]}\n"
                                if float(row[8]) >= 80:
                                    student_name_roster += "PASSED!!!!!\n\n"
                                else:
                                    student_name_roster += "FAILED.This student can't continue here\n\n"
                            found_name = True

            if found_name:
                save_roster.destroy()
                see_roster.destroy()
                fr.destroy()
                enter.destroy()
                canvas = Canvas(stros)
                canvas.pack(side='left', fill='both', expand=True)

                # Add a scrollbar to the canvas
                scrollbar = ttk.Scrollbar(stros, orient='vertical', command=canvas.yview)
                scrollbar.pack(side='right', fill='y')

                # Configure the canvas to use the scrollbar
                canvas.configure(yscrollcommand=scrollbar.set)

                # Create a frame inside the canvas for scrollable content
                scrollable_frame = ttk.Frame(canvas)

                # Add the scrollable frame to the canvas
                canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')

                y = Label(scrollable_frame, text=student_name_roster, font=("Comic Sans MS", 15))
                y.pack()
                # b = Button(scrollable_frame, text="Quit",font=("Algerian",20), command=quit)
                # b.pack()
                scrollable_frame.update_idletasks()
                canvas.configure(scrollregion=canvas.bbox("all"))

            else:
                messagebox.showwarning("NOT FOUND", f"There are no students in grade {entry1}")

        x = IntVar()
        fr = Frame(stros)
        fr.place(x=200, y=400)
        ne = Label(fr, text="Name ", font=("Comic Sans MS", 20))
        n = Entry(fr, font=("Comic Sans MS", 20))
        ent = Button(fr, text="🔎", font=("Comic Sans MS", 20), command=finderr)
        check = Checkbutton(fr, text="Only Average", font=("Comic Sans MS", 20), variable=x, onvalue=1, offvalue=0)
        orr = Label(fr, text="OR", font=("Comic Sans MS", 30))
        ge = Label(fr, text="Grade", font=("Comic Sans MS", 20))
        g = Entry(fr, font=("Comic Sans MS", 20))
        enter = Button(fr, text="🔎", font=("Comic Sans MS", 20), command=finderr)
        ne.grid(row=1, column=1)
        n.grid(row=1, column=2)
        ent.grid(row=1, column=3)
        check.grid(row=1, column=4)
        orr.grid(row=2, column=2)
        ge.grid(row=3, column=1)
        g.grid(row=3, column=2)
        enter.place(x=400, y=600)
        e = Button(stros, text="find", font=("Algerian", 20), command=finde)
        e.place(x=620, y=520)

    def score():
        global x
        x = Tk()
        x.config(bg="black")
        x.geometry("1200x1200")

        def pro():
            namee = name_ent.get().strip()
            gradee = grade_ent.get().strip()
            bioe = bio.get().strip()
            cheme = chem.get().strip()
            phye = phy.get().strip()
            mathe = math.get().strip()
            enge = eng.get().strip()
            ict = ICT.get().strip()

            if (
                    namee == "" or gradee == "" or bioe == "" or cheme == "" or phye == "" or mathe == "" or enge == "" or ict == ""):
                messagebox.showwarning("Error", "There is unfilled place. Please fill it.")
                return
            average = round(((int(bioe) + int(mathe) + int(enge) + int(ict) + int(cheme) + int(phye)) / 6), 2)
            student_score = [namee, gradee, bioe, cheme, phye, mathe, enge, ict, average]
            filename = f"grade {gradee} roster.csv"
            with open(filename, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(student_score)

            messagebox.showinfo("Success", "The student score SAVED  successfully.")

        fn = Frame(x, width=20, height=10)
        fn.place(x=400, y=50)
        name = Label(fn, text="Name", font=("Lucida Calligraphy", 20))
        name_ent = Entry(fn, font=("Lucida Calligraphy", 20))
        grade = Label(fn, text="Grade", font=("Lucida Calligraphy", 20))
        grade_ent = Entry(fn, font=("Lucida Calligraphy", 20))
        name.grid(row=1, column=1)
        name_ent.grid(row=1, column=2)
        grade.grid(row=2, column=1)
        grade_ent.grid(row=2, column=2)
        frame = Frame(x, width=20, height=10)
        frame.place(x=400, y=200)

        def key_event(event):
            pro()

        bio_b = Label(frame, text="Biology", font=("Lucida Calligraphy", 20))
        bio = Entry(frame, font=("Lucida Calligraphy", 20))
        chem_b = Label(frame, text="Chemistry", font=("Lucida Calligraphy", 20))
        chem = Entry(frame, font=("Lucida Calligraphy", 20))
        phy_b = Label(frame, text="Physics", font=("Lucida Calligraphy", 20))
        phy = Entry(frame, font=("Lucida Calligraphy", 20))
        math_b = Label(frame, text="Mathimatics", font=("Lucida Calligraphy", 20))
        math = Entry(frame, font=("Lucida Calligraphy", 20))
        eng_b = Label(frame, text="English", font=("Lucida Calligraphy", 20))
        eng = Entry(frame, font=("Lucida Calligraphy", 20))
        ICT_b = Label(frame, text="ICT", font=("Lucida Calligraphy", 20))
        ICT = Entry(frame, font=("Lucida Calligraphy", 20))
        save = Button(x, text="💾💾Save💾💾", font=("Algerian", 20), command=pro)
        x.bind("<Return>", key_event)
        bio_b.grid(row=1, column=1)
        bio.grid(row=1, column=2)
        chem_b.grid(row=2, column=1)
        chem.grid(row=2, column=2)
        phy_b.grid(row=3, column=1)
        phy.grid(row=3, column=2)
        math_b.grid(row=4, column=1)
        math.grid(row=4, column=2)
        eng_b.grid(row=5, column=1)
        eng.grid(row=5, column=2)
        ICT_b.grid(row=6, column=1)
        ICT.grid(row=6, column=2)
        save.place(x=540, y=460)
        x.mainloop()

    save_roster = Button(stros, text="Save students roster", relief=RAISED, bd=10, font=("Comic Sans MS", 30),
                         bg="black", fg="white", padx=20, command=score)
    save_roster.place(x=100, y=50)
    see_roster = Button(stros, text="see students roster ", relief=RAISED, bd=10, font=("Comic Sans MS", 30),
                        bg="black", fg="white", padx=30, command=roster_view_grade)
    see_roster.place(x=100, y=200)

    def back_6():
        stros.destroy()
        main()

    ba = Button(stros, text="back", command=back_6, font=("Algerian", 20), bg="red")
    ba.place(x=600, y=600)
    stros.mainloop()


# Setting password for to enter in to student management system
def pin_students():
    global pin_s
    pin_s = Tk()
    pin_s.attributes("-alpha", 0.8)
    pin_s.attributes("-fullscreen", True)
    pin_s.resizable(width=False, height=False)
    pin_s.config(bg="black")
    pin_s.title("Password")

    def code1():
        x = ps.get().strip()
        if x == "0000":
            student_management()
            return
        messagebox.showerror("Invalid password", "please try again the input is not correct")

    def key_event(event):
        student_management()

    p = Label(pin_s, text="Please input the SM System login password", font=("Algerian", 30), bg="black", fg="green")
    p.pack()
    ps = Entry(pin_s, font=("Comic Sans MS", 15), bg="white", fg="green", show="*")
    ps.pack()
    p = Button(pin_s, text="Enter", font=("Comic Sans MS", 20), bg="red", fg="black", command=code1)
    p.place(x=650, y=120)
    pin_s.bind("<Return>", key_event)
    pin_s.mainloop()


def messages_to_students():
    message_tk = Tk()
    message_tk.geometry("1000x1000+30+30")
    message_tk.config(bg="#DEB887")

    def save_message():
        save = text.get("1.0", END)
        assi = ""
        time_message_sent = datetime.now().strftime("Date %Y/%m/%d     time %H:%M:%S")
        for i in save:
            assi = assi + i
        assi += time_message_sent
        filename = "information for students.txt"
        with open(filename, 'a', newline='') as file:
            w = file.write(assi)
            w = file.write("-----------------------------------------\n\n")
        messagebox.showinfo("SUCCESS","Submitted Successfully")
    text = Text(message_tk, height=10, width=50, font=("Comic Sans Ms", 20))
    text.pack()
    submit = Button(message_tk, text="Submit", font=("Comic Sans Ms", 20), command=save_message)
    submit.place(x=300, y=400)
    message_tk.mainloop()


def student_management():
    global stud
    pin_s.destroy()
    system.destroy()
    stud = Tk()
    stud.title("student management system")
    stud.geometry("1200x1200")

    background_im = PhotoImage(file="school.PNG")
    background_la = Label(stud, image=background_im)
    background_la.place(x=0, y=0, relwidth=1, relheight=1)
    #    stud.config(background="black")
    title_stud = Label(stud, text="Wellcome to student management system",
                       font=("Lucida Calligraphy", 30),
                       bd=20, relief=SUNKEN, bg="green", fg="white")
    title_stud.pack()
    s = Frame(stud, width=200, height=200)
    s.place(x=50, y=100)
    new_stud = Button(s, width=30, height=2, text="New student    ",
                      font=("Algerian", 20),
                      bd=20, relief=RAISED, bg="black", fg="white", command=new_student
                      )
    message_for_students = Button(s, width=30, height=2,
                                  text="Messages",
                                  font=("Algerian", 20),
                                  bd=20, relief=RAISED, bg="black", fg="white", command=messages_to_students
                                  )
    stud_roster = Button(s, width=30, height=2,
                         text="students roster",
                         font=("Algerian", 20),
                         bd=20, bg="black", fg="white", relief=RAISED, command=student_roster)
    stud_search = Button(s, width=30, height=2,
                         text="student search by name ",
                         font=("Algerian", 20),
                         bd=20, bg="black", fg="white", relief=RAISED,
                         command=student_search)
    stud_search_by_grade = Button(s, width=30, height=2,
                                  text="student search by grade ",
                                  font=("Algerian", 20),
                                  bd=20, bg="black", fg="white", relief=RAISED,
                                  command=search_by_grade)
    new_stud.pack(side=TOP)
    message_for_students.pack(side=TOP)
    stud_roster.pack(side=BOTTOM)
    stud_search.pack(side=LEFT)
    stud_search_by_grade.pack(side=LEFT)

    def back():
        stud.destroy()
        main()

    ba = Button(stud, text="back", command=back, font=("Algerian", 20), foreground="green", bg="black")
    ba.place(x=1000, y=600)
    stud.mainloop()


def search_name():
    sea.destroy()
    tsearch = Tk()
    tsearch.title("searching for students")
    tsearch.geometry("1200x1200")

    def finder_name():
        found = False
        ent = search_entry.get().strip()
        teach_info = ""

        for grade in range(9, 13):
            filename = f"grade {grade} teachers.csv"
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == ent:
                        teach_info += f"Name:    {row[0]}\n"
                        teach_info += f"Age:     {row[1]}\n"
                        teach_info += f"Grade:   {row[2]}\n"
                        teach_info += f"Kebele:  {row[3]}\n"
                        teach_info += f"Phone.No:{row[4]}\n"
                        teach_info += f"subject:  {row[5]}\n\n"
                        found = True
                        break

        q = Label(tsearch, text=teach_info, bg="white",font=("Comic Sans MS", 15))
        q.pack()

        if not found:
            messagebox.showwarning("NOT FOUND", f'There is no any lecturer in this school with name {ent} ')

    sa = Label(tsearch, text="write the Teacher name please", font=("Lucida Calligraphy", 20))
    sa.pack()
    frame = Frame(tsearch)
    frame.pack()
    search_entry = Entry(frame, width=50, font=("Comic Sans MS", 15))
    search_entry.pack(side=LEFT)
    na = Button(frame, text="🔎", font=("Lucida Calligraphy", 20), command=finder_name)
    na.pack(side=LEFT)

    tsearch.mainloop()


def search_grade():
    sea.destroy()
    search_grad = Tk()

    def finder_grad():
        entry = search_grad_entry.get().strip()
        teach_grad_info = ""
        found_grad = False
        for grade in range(9, 13):
            filename = f"grade {grade} teachers.csv"
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                y = 1
                for row in reader:
                    if row[2] == entry:
                        teach_grad_info += f"{y}: {row[0]}  {row[5]} teacher\n"
                        found_grad = True
                    y += 1
        if found_grad:
            canvas = Canvas(search_grad)
            canvas.pack(side='left', fill='both', expand=True)

            # Add a scrollbar to the canvas
            scrollbar = ttk.Scrollbar(search_grad, orient='vertical', command=canvas.yview)
            scrollbar.pack(side='right', fill='y')

            # Configure the canvas to use the scrollbar
            canvas.configure(yscrollcommand=scrollbar.set)

            # Create a frame inside the canvas for scrollable content
            scrollable_frame = ttk.Frame(canvas)

            # Add the scrollable frame to the canvas
            canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')

            y = Label(scrollable_frame, text=teach_grad_info,bg="white", font=("Comic Sans MS", 15))
            y.pack()
            # b = Button(scrollable_frame, text="Quit",font=("Algerian",20), command=quit)
            # b.pack()
            scrollable_frame.update_idletasks()
            canvas.configure(scrollregion=canvas.bbox("all"))

        else:
            messagebox.showwarning("NOT FOUND", f"There are no teachers in grade {entry}")

    def back2():
        search_grad.destroy()
        main()

    ad = Button(search_grad, text="back", command=back2, font=("Algerian", 20), bg="black", fg="green")
    ad.place(x=600, y=600)
    sear_g = Label(search_grad, text="Write the teacher grade, please:", font=("Lucida Calligraphy", 20))
    sear_g.pack()
    frame_gr = Frame(search_grad)
    frame_gr.pack()
    search_grad_entry = Entry(frame_gr, width=50, font=("Comic Sans MS", 15))
    search_grad_entry.pack(side=LEFT)
    search = Button(frame_gr, text="🔎", font=("Lucida Calligraphy", 20), command=finder_grad)
    search.pack(side=LEFT)

    search_grad.mainloop()


def search_subject():
    sea.destroy()
    search_sub = Tk()

    def finder_sub():
        entry = search_subj_entry.get().strip()
        teach_subject_info = ""
        found_grad = False
        for grade in range(9, 13):
            filename = f"grade {grade} teachers.csv"
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[5] == entry:
                        teach_subject_info += f"➡ grade {grade} {row[0]}\n"
                        found_grad = True
        if found_grad:
            canvas = Canvas(search_sub)
            canvas.pack(side='left', fill='both', expand=True)

            # Add a scrollbar to the canvas
            scrollbar = ttk.Scrollbar(search_sub, orient='vertical', command=canvas.yview)
            scrollbar.pack(side='right', fill='y')

            # Configure the canvas to use the scrollbar
            canvas.configure(yscrollcommand=scrollbar.set,bg="#CCFFFF")

            # Create a frame inside the canvas for scrollable content
            scrollable_frame = ttk.Frame(canvas)

            # Add the scrollable frame to the canvas
            canvas.create_window((300,100), window=scrollable_frame)

            y = Label(scrollable_frame, text=teach_subject_info,bg="white", font=("Comic Sans MS", 15))
            y.pack()
            # b = Button(scrollable_frame, text="Quit",font=("Algerian",20), command=quit)
            # b.pack()
            scrollable_frame.update_idletasks()
            canvas.configure(scrollregion=canvas.bbox("all"))

        else:
            messagebox.showwarning("NOT FOUND", f"There are no  {entry} teacher here!!!!!!1")

    sear_g = Label(search_sub, text="Write the it's subject please:", font=("Lucida Calligraphy", 20))
    sear_g.pack()
    frame_gr = Frame(search_sub)
    frame_gr.pack()
    search_subj_entry = Entry(frame_gr, width=50, font=("Comic Sans MS", 15))
    search_subj_entry.pack(side=LEFT)
    search = Button(frame_gr, text="🔎", font=("Lucida Calligraphy", 20), command=finder_sub)
    search.pack(side=LEFT)

    search_sub.mainloop()


def new_teacher():
    global registration_teach
    teach.destroy()
    registration_teach = Tk()
    registration_teach.geometry("1200x1200")
    regist_back = PhotoImage(file="regi.PNG")
    regi_out = Label(registration_teach, image=regist_back)
    regi_out.place(x=0, y=0, relwidth=1, relheight=1)
    com = Label(registration_teach, text="Please fill all required things", font=("Lucida Calligraphy", 20),
                bd=20, relief=SUNKEN, bg="green", fg="white")
    com.pack()

    def register_teacher():
        namer = name_e.get().strip()
        ager = age_e.get().strip()
        grader = grade_e.get().strip()
        kebeler = kebele_e.get().strip()
        phoner = phone_e.get().strip()
        subjectr = subject_e.get().strip()
        logine = login.get().strip()
        if (namer == "" or ager =="" or grader == "" or kebeler =="" or phoner == "" or subjectr == "" or logine == ""):
            messagebox.showwarning("Error", "Please check your input.")
            return
        found=False
        student_data = [namer, ager, grader, kebeler, phoner, subjectr, logine]
        filename = f"grade {grader} teachers.csv"
        for grade in range(9, 13):
            filename = f"grade {grade} teachers.csv"
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if (row[0].lower() == namer.lower() and row[1] == ager.lower() and row[2].lower() == grader.lower() and row[3].lower() == kebeler.lower() and row[4].lower() == phoner.lower() and row[5].lower() == subjectr.lower() and row[6].lower() == logine.lower()):
                        found = True
                        break
        if found:
            messagebox.showwarning("ALREADY EXIST", "The Teacher already exist")
        else:
            with open(filename, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(student_data)

            messagebox.showinfo("Success", "Employee registered successfully.")
    reg = Frame(registration_teach, width=10, height=5)
    reg.pack()
    name = Label(reg, text="Name: ", font=("Lucida Calligraphy", 15), )
    name_e = Entry(reg, font=("Comic Sans MS", 15))
    age = Label(reg, text="Age: ", font=("Lucida Calligraphy", 15))
    age_e = Entry(reg, font=("Comic Sans MS", 15))
    grade = Label(reg, text="Grade", font=("Lucida Calligraphy", 15))
    grade_e = Entry(reg, font=("Comic Sans MS", 15))
    kebele = Label(reg, text="Kebele", font=("Lucida Calligraphy", 15))
    kebele_e = Entry(reg, font=("Comic Sans MS", 15))
    phone = Label(reg, text="phone.No", font=("Lucida Calligraphy", 15))
    phone_e = Entry(reg, font=("Comic Sans MS", 15))
    subject = Label(reg, text="subject", font=("Lucida Calligraphy", 15))
    subject_e = Entry(reg, font=("Comic Sans MS", 15))
    login_pass = Label(reg, text="Login_password", font=("Lucida Calligraphy", 15))
    login = Entry(reg, font=("Comic Sans MS", 15))
    register = Button(registration_teach, text="register", font=("Lucida Calligraphy", 15), command=register_teacher)
    name.grid(row=1, column=1)
    name_e.grid(row=1, column=2)
    age.grid(row=2, column=1)
    age_e.grid(row=2, column=2)
    grade.grid(row=3, column=1)
    grade_e.grid(row=3, column=2)
    kebele.grid(row=4, column=1)
    kebele_e.grid(row=4, column=2)
    phone.grid(row=5, column=1)
    phone_e.grid(row=5, column=2)
    subject.grid(row=6, column=1)
    subject_e.grid(row=6, column=2)
    login_pass.grid(row=7, column=1)
    login.grid(row=7, column=2)
    register.place(x=500, y=320)

    def back3():
        registration_teach.destroy()
        main()

    ad = Button(registration_teach, text="back", command=back3, font=("Algerian", 20),fg="green",bg="black")
    ad.place(x=600, y=600)
    registration_teach.mainloop()


def te():
    a = Tk()

    def ne():
        def save_text():
            nam = nae.get().strip()
            grade = gd.get().strip()
            subjec = sb.get().strip()
            save = text.get("1.0", END)
            assi = ""
            tup = [nam, grade, subjec, save]
            for i in tup:
                assi += f'{i} \n'
                assi += f'---------------------------\n\n'
            filename = f"grade{grade}.txt"
            with open(filename, 'a', newline='') as file:
                w = file.write(assi)

        fr = Frame(a)
        fr.place(x=200, y=100)
        na = Label(fr, text="name")
        nae = Entry(fr)
        na.grid(row=1, column=1)
        nae.grid(row=1, column=2)
        grad = Label(fr, text="grade")
        gd = Entry(fr)
        grad.grid(row=2, column=1)
        gd.grid(row=2, column=2)
        subject = Label(fr, text="subject")
        sb = Entry(fr)
        subject.grid(row=3, column=1)
        sb.grid(row=3, column=2)
        text = Text(a, height=10, width=50)
        text.pack()
        but = Button(a, text="click here to submit", command=save_text)
        but.pack()

    def check():
        found1 = True
        for gr in range(9, 13):
            filename = f"grade {gr} teachers.csv"
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == nm.get().strip():
                        if row[6] == login.get().strip():
                            found1 = True
        if found1:
            ne()

    frame = Frame(a)
    frame.pack()
    name = Label(frame, text="name")
    name.grid(row=1, column=1)
    nm = Entry(frame)
    nm.grid(row=1, column=2)
    logi = Label(frame, text="enter your login password")
    login = Entry(frame)
    login.grid(row=2, column=2)
    logi.grid(row=2, column=1)
    ent = Label(frame, text="Grade")
    ent.grid(row=3, column=1)
    entr = Entry(frame)
    entr.grid(row=3, column=2)
    en = Button(frame, text="ENTER", command=check)
    en.grid(row=4, column=1)

    a.mainloop()


def receive_assignments_stud():
    sc.destroy()
    tk = Tk()
    tk.geometry("1000x600+200+0")
    tk.config(background="yellow")
    tk.resizable(width=False, height=False)
    canvas = Canvas(tk)
    canvas.pack(side='left', fill='both', expand=True)

    # Add a scrollbar to the canvas
    scrollbar = ttk.Scrollbar(tk, orient='vertical', command=canvas.yview)
    scrollbar.pack(side='right', fill='y')

    # Configure the canvas to use the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame inside the canvas for scrollable content
    scrollable_frame = ttk.Frame(canvas)

    # Add the scrollable frame to the canvas
    canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')

    def grade_9():
        m = " \n name  "
        with open('grade 9 assignment.txt', 'r') as file:
            for i in file:
                m += i
        grade9.destroy()
        grade10.destroy()
        grade11.destroy()
        grade12.destroy()
        label.destroy()
        g9 = Label(scrollable_frame, text=f' {m}\n\n', font=("Comic Sans MS", 20))
        g9.pack()

    def grade_10():
        m = " \n name  "
        with open('grade 10 assignment.txt', 'r') as file:
            for i in file:
                m += i
        grade9.destroy()
        grade10.destroy()
        grade11.destroy()
        grade12.destroy()
        label.destroy()
        g9 = Label(scrollable_frame, text=f' {m}\n\n', font=("Comic Sans MS", 20))
        g9.pack()

    def grade_11():
        m = " \n name  "
        with open('grade 11 assignment.txt', 'r') as file:
            for i in file:
                m += i
        grade9.destroy()
        grade10.destroy()
        grade11.destroy()
        grade12.destroy()
        g9 = Label(scrollable_frame, text=m, font=("Comic Sans MS", 20))
        g9.pack()
        label.destroy()

    def grade_12():
        m = " \n name  "
        with open('grade 12 assignment.txt', 'r') as file:
            for i in file:
                m += i
        grade9.destroy()
        grade10.destroy()
        grade11.destroy()
        grade12.destroy()
        g9 = Label(scrollable_frame, text=m, font=("Comic Sans MS", 20))
        g9.pack()
        label.destroy()

    photo = PhotoImage(file="stock1.PNG")
    label = Label(tk, image=photo)
    label.place(x=135,y=0)
    grade9 = Button(tk, text="Grade 9", font=("Comic Sans MS", 20), bg="#F8B88B", fg="white",command=grade_9, padx=20)
    grade9.place(x=110,y=450)
    grade10 = Button(tk, text="Grade 10", font=("Comic Sans MS", 20), bg="#F8B88B", fg="white",command=grade_10, padx=15)
    grade10.place(x=315,y=450)
    grade11 = Button(tk, text="Grade 11", font=("Comic Sans MS", 20), bg="#F8B88B", fg="white",command=grade_11, padx=16)
    grade11.place(x=520,y=450)
    grade12 = Button(tk, text="Grade 12", font=("Comic Sans MS", 20), bg="#F8B88B", fg="white",command=grade_12, padx=14)
    grade12.place(x=730,y=450)
    scrollable_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))
    tk.mainloop()


def receive_message_stud():
    receive_messages = Tk()
    receive_messages.title("Messages")
    receive_messages.geometry("500x300+50+50")
    receive_messages.config(bg="#B1907F")

    def m_from_admin():
        receive_messages.destroy()
        admin_message = Tk()
        admin_message.geometry("900x600")
        admin_message.title("Messages from adminstrator")
        canvas = Canvas(admin_message)
        canvas.pack(side='left', fill='both', expand=True)

        # Add a scrollbar to the canvas
        scrollbar = ttk.Scrollbar(admin_message, orient='vertical', command=canvas.yview)
        scrollbar.pack(side='right', fill='y')

        # Configure the canvas to use the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas for scrollable content
        scrollable_frame = ttk.Frame(canvas)

        # Add the scrollable frame to the canvas
        canvas.create_window((300, 100), window=scrollable_frame)
        def message():

            holder = ""
            filename = "information for students.txt"
            with open(filename, 'r') as file:
                for i in file:
                    holder += i
                    found = True
            if not found:
                messagebox.showinfo("No content", 'There is no message')

            display = Label(scrollable_frame, text=holder, font=("Comic Sans MS", 20),bg="#CCFFFF")
            display.pack()
            scrollable_frame.update_idletasks()
            canvas.configure(scrollregion=canvas.bbox("all"))
        message()
        admin_message.mainloop()

    def m_from_teach():
        receive_messages.destroy()
        mess_teach = Tk()
        mess_teach.title("Messages from teachers")
        mess_teach.geometry("800x600+50+30")
        canvas = Canvas(mess_teach)
        canvas.pack(side='left', fill='both', expand=True)

        # Add a scrollbar to the canvas
        scrollbar = ttk.Scrollbar(mess_teach, orient='vertical', command=canvas.yview)
        scrollbar.pack(side='right', fill='y')

        # Configure the canvas to use the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas for scrollable content
        scrollable_frame = ttk.Frame(canvas)

        # Add the scrollable frame to the canvas
        canvas.create_window((500, 100), window=scrollable_frame)
        def message():
            grade = grade_entry.get().strip()
            holder = ""
            filename = f"information from {grade} teachers.txt"
            with open(filename, 'r') as file:
                for i in file:
                    holder += i

            grade_entry.destroy()
            grade_lable.destroy()
            enter.destroy()
            display = Label(scrollable_frame, text=holder,bg="#CCFFFF", font=("Comic Sans MS", 20))
            display.pack()
            scrollable_frame.update_idletasks()
            canvas.configure(scrollregion=canvas.bbox("all"))
        grade_lable = Label(mess_teach, font=("Comic Sans MS", 20), text="grade")
        grade_entry = Entry(mess_teach, font=("Comic Sans MS", 20))
        enter = Button(mess_teach, font=("Comic Sans MS", 20), text="🔎", command=message, bg="#7F5A58" )
        grade_lable.place(x=50, y=100)
        grade_entry.place(x=150, y=100)
        enter.place(x=150, y=150)
        mess_teach.mainloop()

    message_administrater = Button(receive_messages, text="From Administrator", font=("Comic Sans MS", 20),
                                   command=m_from_admin, bg="#3A3B3C", fg="#E5E4E2")
    message_administrater.place(x=150, y=100)
    message_teacher = Button(receive_messages, text="From Teachers       ", font=("Comic Sans MS", 20),
                             command=m_from_teach, bg="#3A3B3C", fg="#E5E4E2")
    message_teacher.place(x=150, y=200)
    receive_messages.mainloop()


def login_as_student():
    global sc
    tk.destroy()
    sc = Tk()
    sc.title("Students")
    sc.geometry("1600x1600")
    sc.config(bg="#E3F9A6")
    teach_image = PhotoImage(file="student1.PNG")
    butt = Label(sc, image=teach_image, width=640)
    butt.place(x=700, y=20)
    assi = Button(sc, text="Receive Assignments", font=("Comic Sans MS", 45), command=receive_assignments_stud)
    take = Button(sc, text="Receive Message", font=("Comic Sans MS", 50), padx=30, command=receive_message_stud)

    assi.place(x=0, y=100)
    take.place(x=0, y=300)
    # give.place(x=0, y=500)
    sc.mainloop()


def give_assignment():
    c = Tk()
    c.geometry("1600x800+30+30")
    c.title("Assignment")
    time_the_assignment_given = datetime.now().strftime("Date %Y/%m/%d     time %H:%M:%S")
    def ne():
        def save_text():
            nam = nae.get().strip()
            grade = gd.get().strip()
            subjec = sb.get().strip()
            dead = deadline_entry.get().strip()
            save = text.get("1.0", END)
            assi = ""
            if (nam =="" or grade =="" or save=="" or subjec =="" or dead==""):
                messagebox.showerror("ERROR", "There is unfilled space pleace check it !!!")
                return
            tup = [nam, subjec, save]
            for i in tup:
                assi += f'{i} \n'
            assi += f'      date given {time_the_assignment_given} \n'
            assi += f'      deadline  {dead} \n'
            assi += "------------------------------\n"
            filename = f"grade {grade} assignment.txt"
            with open(filename, 'a', newline='') as file:
                w = file.write(assi)
            messagebox.showinfo("SUBMITTED","your message is submitted successfuly")


        fr = Frame(c)
        fr.place(x=400, y=20)
        na = Label(fr, text="name", font=("Comic Sans MS", 15))
        nae = Entry(fr, font=("Comic Sans MS", 15))
        na.grid(row=1, column=1)
        nae.grid(row=1, column=2)
        grad = Label(fr, text="grade", font=("Comic Sans MS", 15))
        gd = Entry(fr, font=("Comic Sans MS", 15))
        grad.grid(row=2, column=1)
        gd.grid(row=2, column=2)
        subject = Label(fr, text="subject", font=("Comic Sans MS", 15))
        sb = Entry(fr, font=("Comic Sans MS", 15))
        subject.grid(row=3, column=1)
        sb.grid(row=3, column=2)
        text = Text(c, height=10, width=50, font=("Comic Sans MS", 20))
        text.place(x=200, y=120)
        but = Button(c, text="click here to submit", font=("Comic Sans MS", 20), command=save_text)
        but.place(x=200, y=500)
        deadline = Label(c,text="Deadline ",font=("ms Boli", 15))
        deadline_entry = Entry(c, font=("ms boli", 15))
        deadline_entry.place(x=700,y=510)
        deadline.place(x=600,y=510)

    ne()
    c.mainloop()


def sent_message_to_students():
    message_tk = Tk()
    message_tk.title("save message")
    message_tk.geometry("1000x1000+30+30")
    message_tk.config(bg="#DEB887")

    def save_message_for_student():
        subject = subject_entry.get().strip()
        grade = grade_entry.get().strip()
        save = text.get("1.0", END)
        assi = ""
        time_message_sent = datetime.now().strftime("Date %Y/%m/%d     time %H:%M:%S")
        collection = [f'grade {grade}', subject, save]
        for i in collection:
            assi += f'{i}\n'
            assi += f'            {time_message_sent}'

        filename = f"information from {grade} teachers.txt"
        with open(filename, 'a', newline='') as file:
            w = file.write(assi)
            w = file.write("-------------------------------------------")

    frame = Frame(message_tk)
    frame.pack()
    grade_lable = Label(frame, text="Grade", font=("Comic Sans Ms", 20))
    grade_entry = Entry(frame, font=("Comic Sans Ms", 20))
    subject_lable = Label(frame, text="Subject", font=("Comic Sans Ms", 20))
    subject_entry = Entry(frame, font=("Comic Sans Ms", 20))
    grade_lable.grid(row=1, column=1)
    grade_entry.grid(row=1, column=2)
    subject_lable.grid(row=2, column=1)
    subject_entry.grid(row=2, column=2)
    text = Text(message_tk, height=10, width=50, font=("Comic Sans Ms", 20))
    text.pack()
    submit = Button(message_tk, text="Submit", font=("Comic Sans Ms", 20), command=save_message_for_student)
    submit.place(x=300, y=400)
    message_tk.mainloop()


def receive_message():
    tc.destroy()
    receive = Tk()
    receive.geometry("1600x800+30+30")
    receive.title("Message")
    canvas = Canvas(receive)
    canvas.pack(side='left', fill='both', expand=True)

    # Add a scrollbar to the canvas
    scrollbar = ttk.Scrollbar(receive, orient='vertical', command=canvas.yview)
    scrollbar.pack(side='right', fill='y')

    # Configure the canvas to use the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set,bg="#CCFFFF")

    # Create a frame inside the canvas for scrollable content
    scrollable_frame = ttk.Frame(canvas)

    # Add the scrollable frame to the canvas
    canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
    information = ""
    with open(f'information for teachers.txt', 'r') as file:
        for i in file:
            information += i
    display_info = Label(scrollable_frame, text=information, font=("Comic Sans MS", 20))
    display_info.pack()
    scrollable_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))
    receive.mainloop()


def teachers():
    sc.destroy()
    global tc
    tc = Tk()
    tc.title("Teachers")
    tc.geometry("1600x1600")
    tc.config(bg="#E3F9A6")
    teach_image = PhotoImage(file="teachers.PNG")
    butt = Label(tc, image=teach_image, width=600)
    butt.place(x=700, y=50)
    assi = Button(tc, text="Give Assignments", font=("Comic Sans MS", 50), padx=10, command=give_assignment)
    take = Button(tc, text="Receive Message", font=("Comic Sans MS", 50), padx=20, command=receive_message)
    give = Button(tc, text="Sent message", font=("Comic Sans MS", 50), padx=70, command=sent_message_to_students)
    assi.place(x=0, y=100)
    take.place(x=0, y=300)
    give.place(x=0, y=500)
    tc.mainloop()


def search():
    global sea
    teach.destroy()
    sea = Tk()
    sea.title("searching for Teachers")
    sea.geometry("1200x1200")
    background_image = PhotoImage(file="6img.PNG")
    teach_lable = Label(sea, text="In which way do you want to find the teacher/s", image=background_image,
                        bg="#CD853F", fg="white",
                        font=("Algerian", 30), relief=SUNKEN, bd=10)
    teach_lable.pack()
    name_search = Button(sea, text="search here using name", font=("Lucida Calligraphy", 30), bg="#808080", fg="white",
                         padx=10,
                         relief=RAISED, bd=10, command=search_name)
    name_search.place(x=100, y=100)
    grade_search = Button(sea, text="search here using grade", font=("Lucida Calligraphy", 30), bg="#808080",
                          fg="white", padx=7,
                          relief=RAISED, bd=10, command=search_grade)
    grade_search.place(x=100, y=250)
    subject_search = Button(sea, text="search here using subject", font=("Lucida Calligraphy", 30), bg="#808080",
                            fg="white", relief=RAISED, bd=10, command=search_subject)
    subject_search.place(x=100, y=400)
    sea.mainloop()


def pin_teachers():
    global pin
    pin = Tk()
    pin.attributes("-fullscreen", True)
    pin.attributes("-alpha", 0.8)
    pin.config(bg="black")
    pin.title("Password")
    pin.resizable(width=False, height=False)

    def code():
        x = pr.get().strip()
        if x == "0000":
            teacher_management()
            return
        messagebox.showerror("Invalid password", "please try again the input is not correct")
        pr.delete(0, END)

    def key_event(event):
        teacher_management()

    p = Label(pin, text="Please input the TM System entry password", font=("Algerian", 30), fg="green", bg="black")
    p.pack()
    pr = Entry(pin, font=("Comic Sans MS", 15), bg="white", fg="green", show="*")
    pr.pack()
    pas = Button(pin, text="Enter", font=("Comic Sans MS", 20), bg="red", fg="black", command=code)
    pas.place(x=650, y=120)
    pin.bind("<Return>", key_event)
    pin.mainloop()

def messages_to_teachers():
    message_tk = Tk()
    message_tk.title("message to teachers")
    message_tk.geometry("1000x1000+30+30")
    message_tk.config(bg="#DEB887")

    def save_message_teach():
        save = text.get("1.0", END)
        assi = ""
        for i in save:
            assi += i
        filename = "information for teachers.txt"
        with open(filename, 'a', newline='') as file:
            w = file.write(assi)
            w = file.write("-------------------------------------------")

    text = Text(message_tk, height=10, width=50, font=("Comic Sans Ms", 20))
    text.pack()
    submit = Button(message_tk, text="Submit", font=("Comic Sans Ms", 20), command=save_message_teach)
    submit.place(x=300, y=400)
    message_tk.mainloop()


def teacher_management():
    global teach

    system.destroy()
    pin.destroy()
    teach = Tk()
    teach.title("Teacher management system")
    teach.geometry("1200x1200")
    teach.config(bg="#F5DEB3")
    upper_bg = Label(teach,text="Wellcome to Teachers management system",font=("mv Boli",30),bg="#CCFFFF",width=200,height=2)
    upper_bg.pack()
    new_teach = Button(teach, width=30, height=2, text="New Teacher",
                       font=("Algerian", 20),
                       bd=20, relief=RAISED, bg="black", fg="white", command=new_teacher
                       )
    teach_status = Button(teach, width=30, height=2,
                          text="Messages",
                          font=("Algerian", 20),
                          bd=20, relief=RAISED, bg="black", fg="white", command=messages_to_teachers)

    teach_search = Button(teach, width=30, height=2,
                          text="teacher search ",
                          font=("Algerian", 20),
                          bd=20, bg="black", fg="white", relief=RAISED, command=search)

    new_teach.place(x=50, y=200)
    teach_status.place(x=50, y=350)
    teach_search.place(x=50, y=500)

    def back4():
        teach.destroy()
        main()

    a = Button(teach, text="back", command=back4, font=("Algerian", 20), bg="black", fg="green")
    a.place(x=800, y=650)
    teach.mainloop()


def mai():
    tk.destroy()
    global system
    system = Tk()
    system.title("STEM Management System")
    x = (system.winfo_screenwidth() / 2) + 400
    y = (system.winfo_screenheight() / 2) + 200
    system.geometry("%dx%d" % (x, y))

    menu_bar = Menu(system)
    system.config(menu=menu_bar)
    filemenu = Menu(menu_bar, font=("Lucida Calligraphy", 20))
    menu_bar.add_cascade(label="Info", menu=filemenu)
    filemenu.add_command(label="Help", command=help_me)
    filemenu.add_command(label="Quit", command=quit)
    background_image = PhotoImage(file="7img.PNG")
    background_label = Label(system, image=background_image)
    background_label.place(x=0, y=0)
    studen = Button(system, text="STEM Students", font=("Comic Sans MS", 30), relief=RAISED, bd=10, bg="#95B9C7",
                    command=pin_students)
    studen.place(x=100, y=250)
    teache = Button(system, text="STEM Teachers", font=("Comic Sans MS", 30), bg='#95B9C7', relief=RAISED, bd=10,
                    command=pin_teachers)
    teache.place(x=600, y=250)
    system.mainloop()


def teacher_login():
    tk.destroy()
    global sc
    sc = Tk()
    sc.title("Teachers")
    sc.geometry("1150x550+100+50")
    sc.config(background="white")
    sc.resizable(width=False, height=False)
    teach_image = PhotoImage(file="login2.PNG")
    butt = Label(sc, image=teach_image)
    butt.pack(side=LEFT)

    def checker():
        found = False
        for grade in range(9, 13):
            filename = f"grade {grade} teachers.csv"
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == nm.get().strip():
                        if row[6] == login.get().strip():
                            found = True
        if found:
            teachers()

        else:
            messagebox.showerror("message", "Teacher not found or fill all blanks!")

    label = Label(sc, text="Welcome to the teachers login section",bg="white" ,font=("Ink Free", 20, "bold"))
    label.place(x=650, y=170)
    name = Label(sc, text="Username", font=("ms Boli", 20), fg="#2554C7", bg="white")
    name.place(x=650, y=250)
    nm = Entry(sc, font=("Comic Sans MS", 15), bd=2, fg="#3A3B3C")
    nm.place(x=850, y=250)
    nm.insert(0, "Username")
    logi = Label(sc, text="Password", font=("ms Boli", 20), fg="#2554C7", bg="white")
    logi.place(x=650, y=350)
    login = Entry(sc, font=("Comic Sans MS", 15), bd=2, fg="#3A3B3C", show="*")
    login.place(x=850, y=350)
    login.insert(0, "Password")
    en = Button(sc, text="Login", font=("Comic Sans MS", 18), fg="white", bg="blue", padx=10, command=checker)
    en.place(x=850, y=450)
    sc.mainloop()

def main():
    global tk
    tk = Tk()
    tk.title("STEM management system")
    x = (tk.winfo_screenwidth()/2)+150
    y = (tk.winfo_screenheight()/2)+100
    tk.geometry("%dx%d"%(x,y))
    tk.config(bg="#C9DFEC")
    icon = PhotoImage(file="icon.PNG")
    tk.iconphoto(True,icon)
    background_image = PhotoImage(file="8img.PNG")
    background_label = Label(tk, image=background_image)
    background_label.place(x=0, y=65, relwidth=1, relheight=1)
    log = Button(tk, text="Login as a Student", bg="blue", fg="white", font=("Comic Sans MS", 15),
                 command=login_as_student)
    log.place(x=400, y=10)
    log_t = Button(tk, text="Login as a Teacher", bg="black", fg="white", font=("Comic Sans MS", 15),
                   command=teacher_login)
    log_t.place(x=600, y=10)
    admin = Button(tk, text="Administrator", bg="#DADBDD", relief=RAISED, bd=10, font=("Lucida Calligraphy", 30),
                   command=mai)
    admin.place(x=250, y=200)
    tk.mainloop()


main()

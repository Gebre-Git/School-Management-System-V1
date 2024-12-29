import re


def main():
    print('''
                ****************************************
                   #                                 #
                   #  Welcome to Teachers system     #
                   #                                 #
                ****************************************   

         ''')
    print("1. Record new Teacher")
    print("2. Search the Teacher")
    print("3. Search Teacher of grades")
    print("4. Give Assignment")
    choose = input(":- ")

    def new_teacher_record():
        print("              Welcome to teachers record section")
        print("                  you can record any teacher")
        print("******************************************************")
        name = input("Name: ")
        name = name.replace(' ', '_')

        def new_teacher_record(teacher_name):
            age = input("Age: ")
            grade = input("Teaching grade: ")
            # kebele = input("Kebele: ")
            # phon_num = input("Phon_num: ")
            # emergency_name = input("Emergency _name: ")
            # emergency_phone_num = input("Emergency_phon_num: ")
            teacher_data_list = [teacher_name, age, grade]  # , kebele, phon_num, emergency_name, emergency_phone_num
            teacher_data_string = ""
            for i in teacher_data_list:
                teacher_data_string = teacher_data_string + i + "--------"  # to convert the list to string and add ---
            teacher_data_string = re.sub(r'--------' + '$', '', teacher_data_string)  # to delete the end of underscore
            with open("C:\\Users\\FISHERY\\PycharmProjects\\Projects\\Payroll system\\teacher.txt", "a") as file:
                file.write(teacher_data_string + '\n')
                print("The new teacher recorded successfully! ")

        with open('C:\\Users\\FISHERY\\PycharmProjects\\Projects\\Payroll system\\teacher.txt', 'r') as file:
            lines = file.readlines()  # to read sing line from the file
        for line in lines[1:]:
            line = re.sub('\n', '', line)  # to remove any /n character substitute by ""
            if name in line:
                print("The teacher already exist! ")
                break
            else:
                new_teacher_record(name)
                break

    def search_teacher():
        print("            Welcome to search option     ")
        print("          You can search the name of teacher ")
        print("*********************************************")
        search = input("Name: ")
        search = search.replace(' ', '_')
        item = ["Name: ", "Age: ", "Grade: "]
        with open('C:\\Users\\FISHERY\\PycharmProjects\\Projects\\Payroll system\\teacher.txt', 'r') as file:
            lines = file.readlines()  # to read sing line from the file

        for line in lines[1:]:
            line = re.sub('\n', '', line)  # to remove any /n character substitute by ""
            if search in line:
                processed_data = re.sub(r'[-]+', ' ', line)  # to substitute the  underscore by 1 space " "
                value = processed_data.split()  # to make it list
                output = '\n'.join([f'{item[i]}{value[i]}' for i in range(len(item))])  # concatenation

        if processed_data:
            print(output)
        else:
            print("The teacher not registered!")

    def search_teacher_grade():
        print("                    Welcome to Grade of teaching search ")
        print("                  you can search the grade between 9 - 12")
        print("***************************************************************************")
        grade_input = input("Enter Grade: ")
        print("1. Only name of teacher")
        print("2. Data of teacher")
        option_input = input("Enter your option: ")
        grade_of_teacher = []
        grade_of_teacher_name = []
        grade = [9, 10, 11, 12]

        def search_all_data():
            with open('C:\\Users\\FISHERY\\PycharmProjects\\Projects\\Payroll system\\teacher.txt', 'r') as file:
                for line in file:
                    name, age, grade = line.strip().split("--------")  # to delete the remaining space by strip()...
                    if grade.strip() == grade_input:  # ...and to cut the underscore by split("---")
                        grade_of_teacher.append((name.strip(), age.strip(),grade.strip()))  # add the grade_input value to the grade_of _students list
            return grade_of_teacher

        def search_grade_name():
            with open('C:\\Users\\FISHERY\\PycharmProjects\\Projects\\Payroll system\\teacher.txt', 'r') as file:
                data = [line.strip().split('--------') for line in file]
            for i in data:
                if i[2] == grade_input:
                    grade_of_teacher_name.append(i[0])
            grade_of_teacher_name.sort()
            return grade_of_teacher_name

        if option_input == "2" and search_all_data():
            print(f"Grade {grade_input} teachers are:- ")
            for student in grade_of_teacher:
                print("Name:", student[0])
                print("Age:", student[1])
                print("Grade:", student[2])
                print()
        elif search_grade_name() and option_input == "1":
            print(f"Grade {grade_input} teachers are:- ")
            for student in grade_of_teacher_name:
                print(student)
        elif option_input != "1" and option_input != "2":
            print("Please read the instructions ,options are 1 and 2!")
        elif grade_input not in grade:
            print(f"No Grade {grade_input} teacher found.")
        elif grade_input not in grade and option_input != "1" and option_input != "2":
            print("Please read the instruction, you got tow error in grad input and option input!")

    def give_assignment():
        print("**********welcome to giving assignment section.")
        name = input("Enter name")
        #with open():
    if choose == "1":
        new_teacher_record()
    elif choose == "2":
        search_teacher()
    elif choose == "3":
        search_teacher_grade()
    elif choose == "4":
        give_assignment()
    else:
        print("Incorrect input. Please read the instructions!")


main()
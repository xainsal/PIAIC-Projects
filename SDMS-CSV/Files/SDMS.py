import csv


def create_Student(name, fname, roll, Class, Subjects=[]):
    lsub = Subjects
    '''Class = int(Class)
    t = True
    while t == True:
        name = input("Enter Your Name: ").title()
        for x in range(100):
            if name and x in name:
                print("Name Is Empty or Contains Numbers")
            else:
                t = False
    if Class >= 4:
        Class = str(Class + "Th")
    elif Class == 3:
        Class = str(Class + "rd")
    elif Class == 2:
        Class = str(Class + "nd")
    elif Class == 1:
        Class = str(Class + "st")
    else:
        print("Invalid Input")'''
    try:
        with open("students.csv", "a", newline="") as stud:
            DataHandler = csv.writer(stud, delimiter=",")
            DataHandler.writerow(
                [
                    roll,
                    name.title(),
                    fname.title(),
                    Class.title(),
                    " ",
                    lsub[0],
                    lsub[1],
                    lsub[2],
                    lsub[3],
                    lsub[4],
                    lsub[5],
                    lsub[6],
                    " ",
                ]
            )
    except PermissionError:
        print("File Cannot be Saved Because It's Already Open In Another Program")
    except FileNotFoundError:
        print("Unable To Find 'students.csv' File")


def get_StudentsByClass(Class):
    try:
        with open("students.csv", "r") as RS:
            x = csv.reader(RS)
            for line in x:
                if Class in line:
                    print(line)
    except FileNotFoundError:
        print("Unable To Find Students.txt")


def update_Student(roll, name):
    newline = []
    lineNo = 0
    LR = []

    new_Name = input("Enter New Name: ").title()
    new_Fname = input("Enter New Father Name: ").title()
    new_Class = input("Enter New Class: ").title()
    # opening File and saving it in a list
    try:
        with open("students.csv", "r") as rf:
            # x = csv.reader(rf)
            for line in rf:
                newline.append(line)
    except FileNotFoundError:
        print("unable to find 'students.txt'")
    else:
        for x in newline:
            if roll in x and name in x:
                LR = x.split(",")
                if new_Name != "":  # and new_Name != str([x for x in range[0, 100]]):
                    LR[1] = new_Name
                else:
                    print("Name Contain Numbers or Is Empty")
                if new_Fname != "":  # and new_Fname != str([x for x in range[0, 100]]):
                    LR[2] = new_Fname
                else:
                    print("Name Contain Numbers or Is Empty")
                LR[3] = new_Class
                newline[lineNo] = ",".join(LR)
            lineNo += 1

    try:
        with open("students.csv", "w", newline="") as rf:
            data_Handler = csv.writer(rf)
            for line in newline:
                data_Handler.writerow(line.split(","))
    except PermissionError:
        print("File Cannot be Saved Because It's Already Open In Another Program")
    except FileNotFoundError:
        print("Unable To Find 'students.csv' File")


def delete_Student(roll, Class):
    newline = []
    lineNo = 0
    # opening File and saving it in a list and preventing it from Crashing
    try:
        # This line will open 'students' csv in read-only mode
        with open("students.csv", "r") as rf:
            # looping through student.csv line by line and saving it 'newline' list
            for line in rf:
                newline.append(line)
    except FileNotFoundError:
        print("unable to find 'students.txt'")
    else:
        # This will now check 'newline' list index by index
        for x in newline:
            # Finding roll and Class in 'newline' index [x]
            if roll in x and Class in x:
                # This will delete index [lineNo] from 'newline'
                del newline[lineNo]
            # this will add 1 to lineNo until roll and class is Found
            lineNo += 1

    try:
        # Opening 'students' csv file for writing. newline will remove line space
        with open("students.csv", "w", newline="") as rf:
            data_Handler = csv.writer(rf)
            # looping in newline list index by inndex and writing it to file
            for line in newline:
                # Writing to csv file and using split function to split list elements
                data_Handler.writerow(line.split(","))
    except PermissionError:
        print("File Cannot be Saved Because It's Already Open In Another Program")
    except FileNotFoundError:
        print("Unable To Find 'students.csv' File")


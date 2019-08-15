import json
import Files.FileCheck as FC


def fileWrite(Roll, Name, Fname, Class, Subjects):
    dictfile = ''
    SID = FC.lastIDCheck()
    StudentID = ''
    rollno = int(Roll[-1]) + 1
    rollno = str(rollno)
    try:
        with open('students.json') as RF:
            dictfile = json.load(RF)
    except Exception as e:
        with open('students.json', 'w') as WF:
            json.dump({'Student_10': {}}, WF)
        print(f'{e} ')
    else:
        SID += 1
        StudentID = "Student_" + str(SID)
    with open('students.json', 'w') as WF:
        dictfile[StudentID] = {"Roll No: ": rollno, "Name: ": Name, "Fathers Name: ": Fname, "Class: ": Class, "Subjects": Subjects}
        json.dump(dictfile, WF, indent=4)

def getStudentInClass(Class):
    found = 0
    try:
        with open("students.json", "r") as RS:
            x = json.load(RS)
    except FileNotFoundError:
        print("Unable To Find Students.csv")
    else:
        for line in x.values():
            for k, v in line.items():
                if Class == v:
                    print(f'{line}')
                    found += 1
        if found < 1:
            print(f'There is no Students in Class {Class}')
        else:
            return True

def updateStudentData(name, fname, Class, index):
    try:
        with open("students.json", "r") as RS:
            dic = json.load(RS)
    except FileNotFoundError:
        print("Unable To Find Students.csv")
    else:
        import copy
        tempdic = copy.deepcopy(dic)
        tempdic[index]["Name: "] = name
        tempdic[index]["Fathers Name: "] = fname
        tempdic[index]["Class: "] = Class

    with open('students.json', 'w') as WF:
        json.dump(tempdic, WF, indent=4)

def deleteStudentData(roll, Class):
    try:
        with open("students.json", "r") as RS:
            dic = json.load(RS)
    except FileNotFoundError:
        print("Unable To Find Students.csv")
    else:
        import copy
        indexr = ''
        indexc = ''
        tempdic = copy.deepcopy(dic)
        for line,val in tempdic.items():
            for keys,vals in val.items():
                if roll == vals:
                    indexr = line
                elif Class == vals:
                    indexc = line
        if indexc == indexr:
            del tempdic[indexc]
            with open('Students.json', 'w') as WF:
                json.dump(tempdic, WF, indent=4)
        else:
            print(f'"Roll No: {roll} and Class: {Class}" one of these values are incorrect')

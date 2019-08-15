import json
import Files.FileRW as FRW

def createFile():
    with open("students.json", 'w') as WF:
        json.dump(["Student ID", "Roll No.", "Name", "Father Name", "Subjects"], WF)

def duplicateCheck(dicFile):
    with open('students.json') as RF:
        file = json.load(RF)
        if file:
            for K in file.keys():
                if file[K]['Roll No: '] == dicFile['Roll No: ']:
                    print(f'{file[K]} already exsist in file')
                    break
            else:
                return dicFile


def lastIDCheck():
    lastKey = ""
    with open('students.json', 'r') as RF:
        file = json.load(RF)
        for student in file.keys():
            lastKey = student
    lastKey = lastKey[-2:]
    return int(lastKey.strip())

def checkStudentData(roll, name):
    rvalid = 0
    nvalid = 0
    try:
        with open("students.json", "r") as RS:
            x = json.load(RS)
    except FileNotFoundError:
        print("Unable To Find Students.csv")
    else:
        for linek, linev in x.items():
            for k, v in linev.items():
                if roll == v:
                    rvalid = 1
                elif name == v:
                    nvalid = 1
                    name = linek
    if rvalid == nvalid:
        return True, name
    else:
        return False

def createStudentData(Name, Fname, Class, Subjects):
    last = []
    rollno = []
    with open('students.json', 'r') as F:
        file1 = json.load(F)
        for studnt in file1.values():
            last.append(studnt["Roll No: "])
    FRW.fileWrite(last, Name, Fname, Class, Subjects)

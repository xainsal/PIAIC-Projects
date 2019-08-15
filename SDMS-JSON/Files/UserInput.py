import Files.InputCheck as IC
import Files.FileRW as FRW
import Files.FileCheck as FC

def createStudent():
    in_Name = True
    in_FName = True
    in_class = True

    while in_Name == True:
        in_Name = IC.nameCheck(str(input("Enter Student's Name: ")).title())

    while in_FName == True:
        in_FName = IC.nameCheck(str(input("Enter Father's Name: ")).title())

    #in_roll = IC.rollClassCheck(input("Enter Roll No. of Student: "))

    while in_class == True:
        in_class = IC.rollClassCheck(str(input("Enter Class: ")))

    in_class = IC.ClassFormating(in_class)

    listSub = IC.subListCheck()

    FC.createStudentData(in_Name, in_FName, in_class, listSub)

def getStudentByClass():
    valid = ''
    in_class = True
    while in_class == True:
        in_class = IC.rollClassCheck(str(input("Enter Class to View Students: ")))

    in_class = IC.ClassFormating(in_class)
    if in_class:
        valid = FRW.getStudentInClass(in_class)
    elif valid == True:
        print(f'Class {in_class} Does not exist')

def updateStudent():
    in_oldName = True
    in_FName = True
    in_class = True
    in_roll = True

    while in_oldName == True:
        in_oldName = IC.nameCheck(str(input("Enter Student's Name: ")).title())

    while in_roll == True:
        in_roll = IC.rollClassCheck(input("Enter Roll No. of Student: "))

    in_class = IC.ClassFormating(in_class)
    valid, index = FC.checkStudentData(in_roll, in_oldName)

    if valid:
        in_newname = True
        in_newfname = True
        in_newclass = True
        print("Enter New Details\n")

        while in_newname == True:
            in_newname = IC.nameCheck(str(input("Enter Student's Name: ")).title())

        while in_newfname == True:
            in_newfname = IC.nameCheck(str(input("Enter Father's Name: ")).title())

        while in_newclass == True:
            in_newclass = IC.rollClassCheck(str(input("Enter Class: ")))

        in_newclass = IC.ClassFormating(in_newclass)
        FRW.updateStudentData(in_newname, in_newfname, in_newclass, index)
    else:
        print("Name or Roll no. Does not Exist")

def deleteStudent():
    in_roll = True
    in_class =True

    while in_roll == True:
        in_roll = IC.rollClassCheck(input("Enter Roll No. of Student: "))

    while in_class == True:
        in_class = IC.rollClassCheck(str(input("Enter Class: ")))

    in_class = IC.ClassFormating(in_class)
    FRW.deleteStudentData(in_roll,in_class)

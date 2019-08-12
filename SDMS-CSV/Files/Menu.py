import Files.SDMS as SDMS

def subjects_List():
    listSub = ["English", "Urdu", "Islamiat", "Pakistan Studies", "", "", ""]
    print("\nCompulsary Subjects Are Already Selected.")
    print(
        f"\tSubjects List:\n\t\t1. {listSub[0]}\n\t\t2. {listSub[1]}\n\t\t3. {listSub[2]}\n\t\t4. {listSub[3]}\n"
    )
    x = 4
    while x < 7:
        tempSub = str(input("Enter " + str(x + 1) + " Subject Name: ")).title()
        if tempSub in listSub:
            print("This Subject Already Exists")
            x -= 1
            tempSub = ""
        else:
            for no in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                if no in tempSub:
                    print(
                        "Invalid Subject Name, Subject Name Can not Contain Numbers or Symbols."
                    )
                    x -= 1
                    tempSub = ""
        if tempSub != "":
            listSub[x] = tempSub
        x += 1
    return listSub


def programMenu():
    x = 0
    while x == 0:
        print("\n\n")
        print(f"[=====================================================]")
        print(f'[ Enter "1" To Create Student                         ]')
        print(f'[ Enter "2" To View Students of a Class               ]')
        print(f'[ Enter "3" To Update Student Information Enter       ]')
        print(f'[ Enter "4" To Delete a Student Enter                 ]')
        print(f'[ To Exit Enter "X"                                   ]')
        print(f"[=====================================================]")
        Choice = str(input("Please Input a Choice: "))
        print("\n\n")

        if Choice == "1":
            in_Name = str(input("Enter Student's Name: ")).title()
            in_FName = str(input("Enter Father's Name: ")).title()
            in_roll = input("Enter Roll No. of Student: ").title()
            in_class = str(input("Enter Class: ")).title()
            listSub = subjects_List()
            SDMS.create_Student(in_Name, in_FName, in_roll, in_class, listSub)
        elif Choice == "2":
            Class = str(input("Enter Class to View Students List: ")).title()
            SDMS.get_StudentsByClass(Class)
        elif Choice == "3":
            in_roll = str(input("Enter Roll No. of Student: "))
            in_Name = str(input("Enter Student's Name: ")).title()
            SDMS.update_Student(in_roll, in_Name)
        elif Choice == "4":
            in_roll = input("Enter Roll No. of Student: ")
            in_class = str(input("Enter Class: ")).title()
            SDMS.delete_Student(in_roll, in_class)
        elif Choice == "X" or Choice == "x":
            x = 1
        else:
            print(f"{Choice} is a Incorrect Option")

import Files.UserInput as UI


def programMenu():
    while True:
        print("\n\n")
        print(f'[=====================================================]')
        print(f'[==========[Student Data Management System]===========]')
        print(f'[=====================================================]')
        print(f'[ Enter "1" To Create Student                         ]')
        print(f'[ Enter "2" To View Students of a Class               ]')
        print(f'[ Enter "3" To Update Student Information Enter       ]')
        print(f'[ Enter "4" To Delete a Student Enter                 ]')
        print(f'[ To Exit Enter "X"                                   ]')
        print(f"[=====================================================]")
        Choice = str(input("Please Input a Choice: "))
        print("\n\n")

        if Choice == "1":
            UI.createStudent()
        elif Choice == "2":
            UI.getStudentByClass()
        elif Choice == "3":
            UI.updateStudent()
        elif Choice == "4":
            UI.deleteStudent()
        elif Choice == "X" or Choice == "x":
            break
        else:
            print(f"{Choice} is a Incorrect Option")

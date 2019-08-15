import string
import Files.FileRW as FRW

#Check if 'name' contains any number or alphabets
def nameCheck(name):
    if name:
        #numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        #symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=', '~', '`', '[', ']', '{', '}', '(', ')', '|',
        #        ';', ':', '"', "'", ',', '<', '>', '.', '?', '/']
        for word in name:
            if word:
                #if word in numbers or word in symbols:
                if word in string.digits:
                    print(f'{name} Contains Number {word}\n')
                    return True
                elif word in string.punctuation:
                    print(f'{name} Contains Symbol {word}\n')
                    return True
        else:
            return name

#check if 'roll no.' or 'class' contains symbols or alphabets
def rollClassCheck(rollNo):
    if rollNo:
        '''symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=', '~', '`', '[', ']', '{', '}', '(', ')', '|',
                  ';', ':', '"', "'", ',', '<', '>', '.', '?', '/']
        Alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']'''
        for word in rollNo:
            # This Works to But it you have to create a whole list of symbols and alphabets
            #if word in_Alphabets or word in symbols:
            if word in string.ascii_letters:
                print(f'{rollNo} Contains Alphabets {word}')
                return True
            elif word in string.punctuation:
                print(f'{rollNo} Contains Symbol {word}')
                return True
        else:
            return rollNo

#check Subject list for numbers or alphabets or duplicate subject
def subListCheck():
        listSub = ["English", "Urdu", "Islamiat", "Pakistan Studies", "", "", ""]
        print("\nCompulsary Subjects Are Already Selected.")
        print(
            f"\tSubjects List:\n\t\t1. {listSub[0]}\n\t\t2. {listSub[1]}\n\t\t3. {listSub[2]}\n\t\t4. {listSub[3]}\n"
        )
        x = 4
        while x < 7:
            tempSub = str(input("Enter " + str(x + 1) + " Subject Name: ")).title()
            if tempSub:
                if tempSub in listSub:
                    print("This Subject Already Exists")
                    x -= 1
                    tempSub = ""
                else:
                    for no in tempSub:
                        if no in string.punctuation:
                            print(f'Invalid Subject Name {tempSub}, Subject Name Contain Symbol. {no}')
                            x -= 1
                            tempSub = ""
                        elif no in string.digits:
                            print(f'Invalid Subject Name {tempSub}, Subject Name Contain Number. {no}')
                            x -= 1
                            tempSub = ""
                            break
                if tempSub:
                    listSub[x] = tempSub
                x += 1
        return listSub

def ClassFormating(Class):
    int_class = int(Class)
    if int_class == 1:
        in_class = str(int_class) + str('st')
        return in_class
    elif int_class == 2:
        in_class = str(int_class) + str('nd')
        return in_class
    elif int_class == 3:
        in_class = str(int_class) + str('rd')
        return in_class
    elif int_class >= 4 and int_class < 21:
        in_class = str(int_class) + str('th')
        return in_class
    elif int_class < 1 or int_class > 20:
        print('Invalid Input! Class can not be Greater than 20 or Smaller than 0')
    found = FRW.getStudentInClass(in_class)
    return found

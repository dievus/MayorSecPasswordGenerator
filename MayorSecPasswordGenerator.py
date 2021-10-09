#!/usr/bin/python
import random
import os
import sys
import pyperclip

LC = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
UC = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
NUM = "0 1 2 3 4 5 6 7 8 9"
SYM = "! @ # $ % ? # ^ & * ( ) [ ] { } \ ; : / . , < > ?"

LC_A = LC.split(' ')
UC_A = UC.split(' ')
NUM_A = NUM.split(' ')
SYM_A = SYM.split(' ')

print("-" * 50)
print("MayorSec Password Generator")
print("A project by The Mayor")
print("-" * 50)
    
def main():

    PASS_LENGTH = int(input("Password length: "))
    if PASS_LENGTH < 12:
        print("Password should be at least 12 characters long.")
        main()
    elif PASS_LENGTH > 36:
        print("Please enter a password less than 36 characters.")
        main()        
    else:    
        password = ""
        for i in range(0, int(PASS_LENGTH)):
            ARRAY = random.randint(0, 3)

            if ARRAY == 0:
                Choice = random.randint(0, len(LC_A))

                password += str(LC_A[(int(Choice)-1)])
                continue
            elif ARRAY == 1:
                Choice = random.randint(0, len(UC_A))

                password += str(UC_A[(int(Choice)-1)])
                continue
            elif ARRAY == 2:
                Choice = random.randint(0, len(NUM_A))

                password += str(NUM_A[(int(Choice)-1)])
                continue
            else:
                Choice = random.randint(0, len(SYM_A))

                password += str(SYM_A[(int(Choice)-1)])
                continue
        print("Printing a secure password at your selected length")
        print("-" * 50)
        print(password)
        print("Password has been copied to your clipboard.\n")
        pyperclip.copy(password)
        file = open("passwordsDELETEME.txt", "w")
        file.write("   TCM Security Secure Password Generator      ")
        file.write("\n[!]Do not store this file on your computer[!]\n")
        file.write("-" * 50 + "\n")
        file.write(password + "\n")
        file.close
        password = ""    
    
def results():
    openResults = input("Do you want to view the generated passwords in a text document? (Y/N) ")
    if openResults == 'Y' or openResults == 'y':
        os.system("notepad.exe passwordsDELETEME.txt")
        sys.exit()
    elif openResults == 'N' or openResults == 'n':
        print("Results are stored in passwordsDELETEME.txt. Goodbye!")
        sys.exit()
    else:
        print("Please answer Y or N")
        results()
    results()        
    
    
if __name__ == '__main__':
    main()
    results()

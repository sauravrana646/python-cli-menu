import os
from welcome import welcome


def aws():
    while True:
        os.system("clear")
        print(welcome("AWS"))
        print("""Select from below : 
        1. 
        9. Go back""")
        choice = int(input("\nEnter your choice : "))
        if choice == 9:
            return
        os.system("clear")

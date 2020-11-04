import aws
import os
from welcome import welcome


def main():
    while True:
        print(welcome("ARTH TASK"))
        print("\nChoose service you want to use : ")
        print("""
        1 : AWS 
        0 : Exit"""
              )
        choice = int(input("\nEnter your choice : "))

        if choice == 1:
            aws.aws()
        elif choice == 0:
            exit()
        os.system("clear")


if __name__ == "__main__":
    main()

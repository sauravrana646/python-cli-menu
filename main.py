import os
import date
import calender
import Web_Server
import yum_config


print(" Test Menu ".center(120, "="))


def main():
    while True:
        print("\nChoose from option ")
        print("""
        1 : Date
        2 : Calender
        3 : yum configuration (Recommended to do first..!)
        4 : Web server
        5 : Docker
        0 : Exit"""
              )
        choice = int(input("Enter your choice : "))

        if choice == 1:
            date.date()
        elif choice == 2:
            calender.cal()
        elif choice == 3:
            yum_config.yum()
        elif choice == 4:
            Web_Server.ws()
        elif choice == 0:
            exit()
        input("Press Enter to continue.....")
        os.system("clear")


main()

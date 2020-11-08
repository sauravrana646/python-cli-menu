from AWS import aws
import os
from Partitions.partiton import partition
from Partitions.lvm import lvm
from welcome import welcome


def main():
    while True:
        print(welcome("ARTH TASK"))
        print("\nChoose service you want to use : ")
        print("""
        1 : AWS 
        2 : PARTITIONS
        3 : LVM
        0 : Exit"""
              )
        choice = input("\nEnter your choice : ")

        if choice == '1':
            aws.aws()
        elif choice == '2' :
            partition()
        elif choice == '3' :
            lvm()
        elif choice == '0':
            exit()
        os.system("clear")


if __name__ == "__main__":
    main()

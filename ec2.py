from subprocess import run,PIPE
from os import system 
from welcome import welcome
from colorama import Fore, Back, Style

def ec2():
    while True : 
        system("clear")
        print(welcome("AWS EC2"))
        print("""Select from below : 
        1. Launch Instance
        2. Create Key Pair
        3. Create Security Group
        4. Create EBS Volume
        5. Attach EBS Volume
        6. Create Snapshot of Volume
        9. Go back""")
        choice = input("\nEnter your choice : ")
        if choice == '1' : 
            pass
        elif choice == '9':
            return
        system("clear")
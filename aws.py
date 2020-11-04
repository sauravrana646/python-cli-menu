import os
from ec2 import ec2
from welcome import welcome
from colorama import Fore, Back, Style
from subprocess import run, PIPE


def aws():
    os.system("clear")
    print(welcome("AWS"))
    print("First you need to login to aws\n")
    auth = run("aws configure", stderr=PIPE)
    authout = run("aws sts get-caller-identity", capture_output=True)
    if auth.returncode == 0:
        print(Fore.GREEN + f"\nAuthentication succcess\n\n{authout.stdout.decode()}")
        print(Style.RESET_ALL)
        input("Press ENTER to continue....")
    else:
        print(Fore.RED + f"\nCouldn't authenticate\n\nError : \n{authout.stderr.decode()}")
        print(Style.RESET_ALL)
        input("Press ENTER to continue....")

    while True:
        os.system("clear")
        print(welcome("AWS"))
        print("""Select from below : 
        1. EC2
        2. S3
        3. Cloundfront
        4. 
        9. Go back""")
        choice = input("\nEnter your choice : ")
        if choice == '1' : 
            ec2()
        elif choice == '9':
            return
        os.system("clear")

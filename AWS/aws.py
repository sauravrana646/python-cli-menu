import os
from AWS.ec2 import ec2
from AWS.s3 import  s3
from AWS.cloudfront import cloudfront
from welcome import welcome
from colorama import Fore, Back, Style
from subprocess import run, PIPE


def aws():
    os.system("clear")
    print(welcome("AWS"))
    aws_out = run(f"aws help",shell=True,capture_output=True)
    if aws_out.returncode != 0 :
        print(Fore.RED + f"AWS CLI is not installed on the machine\nError : \n{aws_out.stderr.decode()}")
        print(Style.RESET_ALL)
        print("Exiting...\n\nPress ENTER to continue...")
        input()
        return 
    else:
        pass
    print("\nChecking User Authentication\n")
    authcheck = run("aws sts get-caller-identity",shell=True,capture_output=True)
    if authcheck.returncode == 0:
        print(Fore.GREEN + f"\nAlready Authenticated\n\n{authcheck.stdout.decode()}")
        print(Style.RESET_ALL)
    else:
        print("First you need to login to aws\n")
        auth = run("aws configure",shell=True,stderr=PIPE)
        authout = run("aws sts get-caller-identity", shell=True , capture_output=True)
        if auth.returncode == 0 and authout.stdout.decode() not in [" ",' ','',""]:
            print(Fore.GREEN + f"\nAuthentication succcess\n\n{authout.stdout.decode()}")
            print(Style.RESET_ALL)
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
        9. Go back""")
        choice = input("\nEnter your choice : ")
        if choice == '1' : 
            ec2()
        if choice == '2' : 
            s3()
        if choice == '3' :
            cloudfront()
        elif choice == '9':
            return
        os.system("clear")

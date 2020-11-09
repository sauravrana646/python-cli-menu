from os import system
from welcome import welcome
from subprocess import run,PIPE
from colorama import Fore, Back, Style

def additonal_repo():
    print(Fore.YELLOW + "\nInstalling additonal Repos for redhat.......\n")
    print(Style.RESET_ALL)

    epel_out = run("dnf install  -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm",shell=True,text=True,stderr=PIPE)
    if epel_out.returncode != 0 :
        print(Fore.RED + f"\nWe encountered some error : \n{epel_out.stderr}")
        print(Style.RESET_ALL)

    rpmfusion_out = run("dnf install -y --nogpgcheck https://download1.rpmfusion.org/free/el/rpmfusion-free-release-8.noarch.rpm https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-8.noarch.rpm",shell=True,text=True,stderr=PIPE)
    if rpmfusion_out.returncode != 0 :
        print(Fore.RED + f"\nWe encountered some error : \n{rpmfusion_out.stderr}")
        print(Style.RESET_ALL)
    

def yum():
    system("clear")
    print(welcome("YUM CONFIGURATION"))
    print(Fore.YELLOW + "Please ensure that optical drive is attached before proceeding......")
    print(Style.RESET_ALL)
    input("Press enter to proceed.....")

    run("mkdir /dvd",shell=True)
    print("\n\n")
    run("mount /dev/sr0 /dvd/",shell=True)
    print("\n\n")
    run("lsblk",shell=True)
    print("\n")

    datafile = f"""[dvd1]\nbaseurl=file:///dvd/AppStream\ngpgcheck=0\n\n[dvd2]\nbaseurl=file:///dvd/BaseOS\ngpgcheck=0"""

    print(Fore.GREEN + "\nCreating Repo FIle for yum")
    print(Style.RESET_ALL)

    yumfile = open("/etc/yum.repos.d/new_repo.repo" , "w")
    if yumfile:
        print(Fore.GREEN + "\nFile created succesfully.....\nNow writing in file.....\n")
        print(Style.RESET_ALL)
        yumfile.writelines(datafile) 
        print(Fore.GREEN + "File written successfully.....\n")
        print(Style.RESET_ALL)
        yumfile.close()

    additonal_repo()

    print(Fore.GREEN + "\nListing repos : \n")
    print(Style.RESET_ALL)
    run("yum repolist",shell=True)

    print(Fore.GREEN + "\nYum has been successfully configured on your system.......")
    print(Style.RESET_ALL)
    input("Press ENTER to return")
    return

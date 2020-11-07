from subprocess import Popen,PIPE,run
# from welcome import welcome
import sys
from os import system
from colorama import Fore, Back, Style

def create_pv(devices):
    pvout = run(f"pvcreate {' '.join(devices)}",shell=True,input='y\n',encoding='ascii',stderr=PIPE)
    if pvout.returncode != 0 :
        print(Fore.RED + f"\n We encountered an error :\n{pvout.stderr.decode()}\n")
        print(Style.RESET_ALL)
        print("Exiting...\n")
        exit()
    print(Fore.GREEN + "\n\n Physical Volume Details :\n")
    print(Style.RESET_ALL)
    run(f"pvdisplay {' '.join(devices)}",shell=True)    
    input("Press ENTER to continue ...")

def create_vg(vgname,pvname):
    vgout = run(f"vgcreate {vgname} {' '.join(pvname)}",input='y\n',encoding='ascii',shell=True,stderr=PIPE,text=True)

    if vgout.returncode != 0 :
        print(Fore.RED + f"\n We encountered an error :\n{vgout.stderr}\n")
        print(Style.RESET_ALL)
        print("Exiting...\n")
        exit()
    print(Fore.GREEN + "\n\n Volume Group Details :\n")
    print(Style.RESET_ALL)
    run(f"vgdisplay {vgname}",shell=True , stderr=PIPE)
    input("\nPress ENTER to continue ...")

def partition():    
    while True:
        system("clear")
        # print(welcome("LVM PARTITION"))
        print("""Select from below : 
        1. Create Physical Volume
        2. Create Volume Group
        3. Create Logical Volume
        4. Extend Volume Group
        5. Extend Logical Volume
        6. Delete Logical Volume
        7. Delete Volume Group
        8. Delete Physical Volume
        9. Go back""")
        choice = input("\nEnter your choice : ")
        if choice == '1' : 
            devices = input("Enter the name of device for PV (if multiple give space separated values) : ").split()
            print(f"Total {len(devices)} entered : " , *devices)
            create_pv(devices)
        if choice == '2' :
            vgname = input("Enter the name of VG to create : ")
            pvname = input("Enter Physical Volume device name to make VG : ").split()
            create_vg(vgname,pvname)
        elif choice == '9' :
            return
        system("clear")

partition()
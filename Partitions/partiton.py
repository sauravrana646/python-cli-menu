from subprocess import Popen,PIPE,run
from welcome import welcome
import sys
from os import system
from colorama import Fore, Back, Style

def create_partition(device,part_type="",part_number="",start="",end="") :
    part_out = run(f"fdisk {device}",capture_output=True,shell=True,input=f"n\n{part_type}\n{part_number}\n{start}\n{end}\ny\nw\n",text=True,encoding='ascii')
    if part_out.returncode == 0:
        for line in part_out.stdout.split("\n"):
            if line.startswith("Created") : 
                    print()
                    print(Fore.GREEN + line)
                    print(Style.RESET_ALL)
        print(Fore.GREEN + f"Succcessfully Created the partition\n")
        print(Style.RESET_ALL)
    else :
        print(Fore.RED + f"\nCouldn't create partition\n\nError : \n{part_out.stderr.decode()}")
        print(Style.RESET_ALL)

    input("\nPress ENTER to continue...")

def delete_partition(device,part_number):
    delpart_out = run(f"fdisk {device}",capture_output=True,shell=True,input=f"d\n{part_number}\nw",text=True,encoding='ascii')
    if delpart_out.returncode == 0:
        for line in delpart_out.stdout.split("\n"):
            if line.startswith("Partition") : 
                    print()
                    print(Fore.GREEN + line)
                    print(Style.RESET_ALL)
        print(Fore.GREEN + f"Succcessfully deleted the partition\n")
        print(Style.RESET_ALL)
    else :
        print(Fore.RED + f"\nCouldn't delete partition\n\nError : \n{delpart_out.stderr.decode()}")
        print(Style.RESET_ALL)
    input("\nPress ENTER to continue...")
def partition():    
    while True:
        system("clear")
        print(welcome("LINUX PARTITIONS"))
        print("""Select from below : 
        1. Create new partition
        2. Delete a partion
        3. List all partions
        9. Go back""")
        choice = input("\nEnter your choice : ")
        if choice == '1' : 
            device = input("Enter Device Name : ")

            print("\n\nPrinting Already Created Partitions\n")
            print_out = run(f"fdisk {device}",capture_output=True,shell=True,input=b'p\nq\n')
            print_out = print_out.stdout.decode(sys.stdout.encoding)
            for line in print_out.split("\n"):
                if line.startswith("/") or line.startswith("Device"): 
                    print(line)
                else : 
                    continue
            part_type = input("\n\nEnter partition type [primary p \ extended e] : ")
            part_number = input("Enter partition number (leave empty for default): ")
            start = input("Enter start sector (leave empty for default) : ")
            end = input("Enter last sector (leave empty for default or can give size as +5G) : ")
            create_partition(device,part_type,part_number,start,end)
        if choice == '2' : 
            device = input("Enter Device Name : ")

            print("\n\nPrinting Partitions\n")
            print_out = run(f"fdisk {device}",capture_output=True,shell=True,input=b'p\nq\n')
            print_out = print_out.stdout.decode(sys.stdout.encoding)
            total_parts = None
            for line in print_out.split("\n"):
                if line.startswith("/") or line.startswith("Device"): 
                    total_parts = total_parts + line + "\n"
                    print(line)
                else : 
                    continue
                print(f'This is the total : {total_parts}')
            if total_parts is None : 
                print(Fore.RED + "No partiton to delete.\n")
                print(Style.RESET_ALL)
                input("Press Enter to continue...")
                partition()
                   
            part_number = input("\nEnter partition number to delete (leave empty for default): ")
            delete_partition(device,part_number)
            
        if choice == '3' :
            print(Fore.GREEN + "\n\nPrinting Partitions")
            print(Style.RESET_ALL)
            print_out = run(f"fdisk -l",capture_output=True,shell=True,input=b'p\nq\n')
            print_out = print_out.stdout.decode(sys.stdout.encoding)
            for line in print_out.split("\n"):
                if line.startswith("Device") : 
                    print(f"\n{line}")
                elif line.startswith("/") : 
                    print(line)
            input("\nPress Enter to continue...")
        elif choice == '9' :
            return

        system("clear")


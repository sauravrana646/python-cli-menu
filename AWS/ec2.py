from subprocess import run,PIPE
from os import system 
from welcome import welcome
from colorama import Fore, Back, Style

def attach_ebs(instance_id,volume_id,device):
    attach_out = run(f"aws ec2 attach-volume --device {device} --instance-id {instance_id} --volume-id {volume_id}",shell=True,capture_output=True)
    if attach_out.returncode == 0 :
        print(Fore.GREEN + f"\nSuccess\n{attach_out.stdout.decode()}")
        print(Style.RESET_ALL)
    else :
        print(Fore.RED + f"Failed\nError :\n{attach_out.stderr.decode()}")
        print(Style.RESET_ALL)

    input("Enter to continue....")

def create_ebs_volume(availability_zone,size,volume_type) : 
    ebs_out = run(f"aws ec2 create-volume --availability-zone {availability_zone} --size {size} --volume-type {volume_type}",shell=True,capture_output=True)
    if ebs_out.returncode == 0 :
        print(Fore.GREEN + f"\nSuccess\n{ebs_out.stdout.decode()}")
        print(Style.RESET_ALL)
    else :
        print(Fore.RED + f"Failed\nError :\n{ebs_out.stderr.decode()}")
        print(Style.RESET_ALL)

    input("Enter to continue....")


def add_ingress_rule(sg_id,protocol,toport,cidr):
    ingress_out = run(f"aws ec2 authorize-security-group-ingress --group-id {sg_id} --protocol {protocol} --port {toport} --cidr {cidr}",shell=True,capture_output=True)
    if ingress_out.returncode == 0 :
        print(Fore.GREEN + f"\nSuccessfully Added Rule")
        print(Style.RESET_ALL)
    else :
        print(Fore.RED + f"Failed\nError :\n{ingress_out.stderr.decode()}")
        print(Style.RESET_ALL)

    input("Enter to continue....")

def create_security_group(sg_name,description):
    sg_out = run(f"aws ec2 create-security-group --group-name {sg_name} --description \"{description}\"",shell=True,capture_output=True)
    if sg_out.returncode == 0 :
        print(Fore.GREEN + f"\n\nSuccess\n{sg_out.stdout.decode()}")
        print(Style.RESET_ALL)
    else :
        print(Fore.RED + f"Failed\nError :\n{sg_out.stderr.decode()}")
        print(Style.RESET_ALL)
    
    print(Fore.YELLOW + "\n\nADD INGRESS OPTION IS RECOMMENDED TO DO NEXT\n")
    print(Style.RESET_ALL)
    input("Enter to continue....")

def create_key_pair(key_name):
    key_out = run(f"aws ec2 create-key-pair --key-name {key_name}",shell=True,capture_output=True)
    if key_out.returncode == 0 :
        print(Fore.GREEN + f"\n\nSuccess\n{key_out.stdout.decode()}")
        print(Style.RESET_ALL)
    else :
        print(Fore.RED + f"Failed\nError :\n{key_out.stderr.decode()}")
        print(Style.RESET_ALL)
    input("Enter to continue....")

def launch_instance(image_id,security_group,key_pair,count,instance_type):
    print("Launching Container")
    cmd = f"aws ec2 run-instances --image-id {image_id} --key-name {key_pair} --security-group-ids {security_group} --count {count} --instance-type {instance_type}"
    launch_out = run(f"{cmd}",shell=True,capture_output=True)
    if launch_out.returncode == 0 :
        print(Fore.GREEN + f"\n\nSuccess\n{launch_out.stdout.decode()}")
        print(Style.RESET_ALL)
    else :
        print(Fore.RED + f"Failed\nError :\n{launch_out.stderr.decode()}")
        print(Style.RESET_ALL)
    input("Enter to continue....")

def ec2():
    while True : 
        system("clear")
        print(welcome("AWS EC2"))
        print("""Select from below : 
        1. Launch Instance
        2. Create Key Pair
        3. Create Security Group
        4. Add ingress rule
        5. Create EBS Volume
        6. Attach EBS Volume
        9. Go back""")
        choice = input("\nEnter your choice : ")
        if choice == '1' :
            image_id = input("\nEnter Image ID : ")
            count = input("Enter no. of instances to launch : ")
            security_group = input("Enter the security group ids : ")
            key_pair = input("Enter name of key-pair : ")
            instance_type = input("Enter the instance type : ")
            launch_instance(image_id,security_group,key_pair,count,instance_type)
        elif choice == '2':
            key_name = input("Enter your Key name : ")
            create_key_pair(key_name)
        elif choice == '3' : 
            sg_name = input("Enter the Secrity Group name : ")
            description = input("Enter Security Group Descrition : ")
            create_security_group(sg_name,description)
        elif choice == '4' :
            sg_id = input("Enter Security Group ID : ")
            protocol = input("Enter Protcol : ")
            toport = input("Enter Port : ")
            cidr = input("Enter CIDR block [x.x.x.x/x]: ")
            add_ingress_rule(sg_id,protocol,toport,cidr)
        elif choice == '5' :
            availability_zone = input("Enter the Availability Zone : ")
            size = input("Enter the size (in GiB) : ")
            volume_type = input("Enter the Volume type : ")
            create_ebs_volume(availability_zone,size,volume_type)
        elif choice == '6' :
            instance_id = input("Enter Instance ID : ")
            volume_id = input("Enter Volume ID : ")
            device = input("Enter Device name : ")
            attach_ebs(instance_id,volume_id,device)
        elif choice == '9':
            return
        system("clear")
from subprocess import run,PIPE
from os import system 
from welcome import welcome
from colorama import Fore, Back, Style

def put_object(bucket_name,key,body,acl) :
    put_out = run(f"aws s3api put-object --bucket {bucket_name} --acl {acl} --key {key} --body \"{body}\"",shell=True,capture_output=True)
    if put_out.returncode == 0 :
        print(Fore.GREEN + f"\nSuccess\n{put_out.stdout.decode()}")
        print(Style.RESET_ALL)
    else :
        print(Fore.RED + f"\n\nFailed\nError :\n{put_out.stderr.decode()}")
        print(Style.RESET_ALL)

    input("Enter to continue....")

def public_acess_block(bucket_name,new_acl,any_acl,app,caa):
    block_out = run(f"aws s3api put-public-access-block --bucket {bucket_name} --public-access-block-configuration \"BlockPublicAcls={new_acl},IgnorePublicAcls={any_acl},BlockPublicPolicy={app},RestrictPublicBuckets={caa}\"",shell=True,capture_output=True)
    if block_out.returncode == 0 :
        print(Fore.GREEN + f"\nSuccess\n{block_out.stdout.decode()}")
        print(Style.RESET_ALL)
    else :
        print(Fore.RED + f"\n\nFailed\nError :\n{block_out.stderr.decode()}")
        print(Style.RESET_ALL)

    input("Enter to continue....")

def create_bucket(bucket_name,region_name):
    bucket_out = run(f"aws s3api create-bucket --bucket {bucket_name} --region {region_name} --create-bucket-configuration LocationConstraint={region_name}",shell=True,capture_output=True)
    if bucket_out.returncode == 0 :
        print(Fore.GREEN + f"\nSuccess\n{bucket_out.stdout.decode()}")
        print(Style.RESET_ALL)
    else :
        print(Fore.RED + f"\n\nFailed\nError :\n{bucket_out.stderr.decode()}")
        print(Style.RESET_ALL)

    input("Enter to continue....")


def s3():
    while True : 
        system("clear")
        print(welcome("AWS S3"))
        print("""Select from below : 
        1. Create S3 Bucket
        2. Block Public Access of Bucket
        3. Put Object in Bucket
        9. Go back""")
        choice = input("\nEnter your choice : ")
        if choice == '1' :
            bucket_name = input("Enter Bucket name : ")
            region_name = input("Enter Region name : ")
            create_bucket(bucket_name,region_name)
        if choice == '2' :
            bucket_name = input("Enter Bucket name : ")
            new_acl = input("Do you want to Block public access to buckets and objects granted through new access control lists (ACLs) [true/false] : ") 
            any_acl = input("Do you want to Block public access to buckets and objects granted through any access control lists (ACLs) [true/false] : ")
            app = input("Do you want to Block public access to buckets and objects granted through new public bucket or access point policies [true/false] : ")
            caa = input("Do you want to Block public and cross-account access to buckets and objects through any public bucket or access point policies [true/false] : ")
            public_acess_block(bucket_name,new_acl,any_acl,app,caa)
        if choice == '3' :
            print(Fore.GREEN + "Available Buckets : \n")
            run("aws s3api list-buckets --query \"Buckets[].Name\"",shell=True,text=True)
            print(Style.RESET_ALL)
            bucket_name = input("Enter Bucket name : ")
            key = input("Enter file/folder name where to save object in S3 : ")
            body = input("Enter the local path of the object you wish to add to Bucket : ")
            acl = input("Enter Access Control [private/public-read] : ")
            put_object(bucket_name,key,body,acl)
        if choice == '9' :
            return
        system("clear")
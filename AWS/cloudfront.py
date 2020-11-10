from subprocess import run,PIPE
from os import system,path
from AWS.conf import modify_conf
from AWS.update_policy import update_policy
from welcome import welcome
from colorama import Fore, Back, Style

def create_cloudfront_dist(origin_name,root_object="",oai_id=""):
    modify_conf(origin_name,root_object,oai_id)
    path_dir = path.abspath(r"AWS\new_conf.json")
    cldf_out = run(f"aws cloudfront create-distribution --distribution-config file://{path_dir} ",shell=True, capture_output=True)
    if cldf_out.returncode == 0:
        print(Fore.GREEN + f"\nSuccess\n\n{cldf_out.stdout.decode()}")
        print(Style.RESET_ALL)
    else :
        print(Fore.RED + f"\nCouldn't do it\n\nError : \n{cldf_out.stderr.decode()}")
        print(Style.RESET_ALL)
    run(f"rm -f {path_dir}",shell=True)

    up_policy = input(Fore.YELLOW + "Do you want to update bucket policy for s3? (Recommended if s3 is origin) [y/n]: ")
    print(Style.RESET_ALL)
    if up_policy.lower() == 'y' :
        update_policy(origin_name,oai_id)
        bpath_dir = path.abspath(r"AWS\new_bucket_policy.json")
        up_pol_out = run(f"aws s3api put-bucket-policy --bucket {origin_name} --policy file://{bpath_dir}",shell=True,capture_output=True)
        if up_pol_out.returncode == 0:
            print(Fore.GREEN + f"\nSucccess\n\n{up_pol_out.stdout.decode()}")
            print(Style.RESET_ALL)
        else :
            print(Fore.RED + f"\nCouldn't update\n\nError : \n{up_pol_out.stderr.decode()}")
            print(Style.RESET_ALL)
        run(f"rm -f {bpath_dir}",shell=True)
    else : 
        print("\nAll Done\n")

    input("Press ENTER to continue....")


def create_OAI(caller_reference,comment):
    oai_out = run(f"aws cloudfront create-cloud-front-origin-access-identity --cloud-front-origin-access-identity-config CallerReference=\"{caller_reference}\",Comment=\"{comment}\"",shell=True,capture_output=True)
    if oai_out.returncode == 0 :
        print(Fore.GREEN + f"\n\nSuccess\n{oai_out.stdout.decode()}")
        print(Style.RESET_ALL)
    else :
        print(Fore.RED + f"Failed\nError :\n{oai_out.stderr.decode()}")
        print(Style.RESET_ALL)
    input("Enter to continue....")

def cloudfront():
    while True : 
        system("clear")
        print(welcome("AWS CLOUDFRONT"))
        print("""Select from below : 
        1. Create Origin Access Identity (Recommended if making s3 as Origin)
        2. Create Cloudfront Distribution
        9. Go back""")
        choice = input("\nEnter your choice : ")
        if choice == '1' :
            caller_reference = input("Enter Caller Reference : ")
            comment = input("Enter Comment : ")
            create_OAI(caller_reference,comment)
        if choice == '2' : 
            print(Fore.GREEN + "Available Buckets : \n")
            run("aws s3api list-buckets --query \"Buckets[].Name\"",shell=True,text=True)
            print(Style.RESET_ALL)
            origin_name = input("Enter your Origin (if s3 use <bucket name>) : ")
            print(Fore.GREEN + "Available Cloundfront OAIs : \n")
            run("aws cloudfront list-cloud-front-origin-access-identities --query \"CloudFrontOriginAccessIdentityList.Items[*].[Comment,Id]\" --output text",shell=True,text=True)
            print(Style.RESET_ALL)
            oai_id = input("Enter Origin Access Identity (if using s3 as origin): ")
            root_object = input("Enter Default Root Object (if any) : ")
            create_cloudfront_dist(origin_name,root_object,oai_id)
        if choice == '9' :
            return
        system("clear")
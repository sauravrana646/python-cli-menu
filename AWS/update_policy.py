from subprocess import run,PIPE
from os import system,path
from colorama import Fore, Back, Style

def update_policy(bucket_name,OAI):
    with open('bucket-policy.json', 'r') as f:
        data = f.read()

    data = data.replace('BUCKET_NAME_HERE', bucket_name)
    data = data.replace('ORIGIN_ACCESS_IDENTITY_HERE', OAI)
    # print(data)
   
    with open("AWS/new_bucket_policy.json" , "w") as f:
        f.write(data)



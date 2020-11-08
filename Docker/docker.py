import subprocess # for  running the os level commands
import platform #for finding the name of the os
from welcome import welcome
def pull_image(): #Method for pulling/downloading the docker image form the docker hub

    image=input("Enter the image name[also specify the version if you want]-:")
    o=subprocess.run("dokcer pull {}".image,shell=True)
    if o.returncode ==0:
        print("Image download succesfully..:)")
    else:
        print("Some error happened..:(")

def launch_container(): #Method for launching the docker container 

    image_name=input("Enter the image name-:")
    os_name=input("Enter the name you want to give[else just press enter]-:")
    if len(os_name) !=0:
        subprocess.run("docker run -it --name {} {}".format(os_name,image_name),shell=True)
    else:
        subprocess.run("docker run -it {}".format(image_name),shell=True)

def remove_image(): #Method for removing the image

    image_name=input("Enter the image name you want to delete-:")
    o=subprocess.run("doker rmi -f {}".format(image_name),shell=True)
    if o.returncode ==0:
        print("Image deleted Successfully...:)")
    else:
        print("Some error happened..:(")


def remove_container(): #method for removing the container

    image_or_id_of_os=input("Enter the image or id of the container/os you want to delete-:")
    o=subprocess.run("docker rm {}".format(image_or_id_of_os),shell=True)
    if o.returncode ==0:
        print("Conatiner/os remove successfully..:)")
    else:
        print("Some error happened..:(")

def see_logs(): # Method for seeing the logs of a container

    image_or_id_of_os=input("Enter the name or id of the conatiner/os whose logs you want to see-:")
    subprocess.run("docker logs {}".format(image_or_id_of_os),shell=True)
    
 
def cp_base_to_cont(): #Method for copying the content from the base os to the conatiner

    content=input("Enter the path of the content you want to copy from os to container-:")
    os=input("Enter the os name or id-:")
    path_in_os=input("Enter the location in the conatiner where you want to store the content-:")
    o=subprocess.run("docker cp {} {}:{}".format(content,os,path_in_os),shell=True)
    if o.returncode ==0:
        print("The file conetent has been copied to the respective docker conatiner successfully..:)")
    else:
        print("Some error happened..:(")

def cp_cont_to_base(): #Method for copying the content  from container to the base os

    content=input("Enter the path of the content you want to copy from container  to base os-:")
    os=input("Enter the os name or id-:")
    path_in_base=input("Enter the loaction where you want to copy the content in the base os-;")
    o=subprocess.run("docker cp {}:{}  {}".format(os,content,path_in_base),shell=True)
    if o.returncode ==0:
        print("The file conetent has been copied to the respective docker conatiner successfully..:)")
    else:
        print("Some error happened..:(")


def see_the_running_cont(): #Method for seeing the currently running container

    subprocess.run("docker ps ",shell=True)


def see_all_cont(): #Method for seeing the all [active+inactive] containers

    subprocess.run("docker ps -a",shell=True)





def start_exist_cont(): #Method for starting the existing container..

    name_id_os=input("Enter the name/id of the conatiner/os-:")
    code=subprocess.run("docker start {}".format(name_id_os),shell=True)
    if code.returncode==0:
     print("Conatiner start Successfully..:)")
     choice=input("Do you want to to get the terminal of this conatiner [y/n]? ")
     if choice=="y":
        get_terminal(name_id_os)
    else:
        print("Something wrong happenmed....:(")

def get_terminal(os="none"): #method for getting the terminal of the launched container

    if os=="none":
        os=input("Enter the name/id of the conatiner/os -:")
    subprocess.run("docker attach {}".format(os),shell=True)


def start_docker_service(): # Method for starting the docker service

    code=subprocess.run("systemctl start docker",shell=True)
    if code.returncode==0:
        print("Service start Successfully...:)")
    else:
        print("Something wrong happened..:(")

def stop_docker_services(): #method for stopping the docker service
    code=subprocess.run("systemctl stop docker",shell=True)
    if code.returncode==0:
        print("Service stop Successfully...:)")
    else:
        print("Something wrong happened..:(")

def stop_running_docker():  #method for stopping the running container

    os=input("Enter the os/container name/id -:")
    code=subprocess.run("docker stop {}".format(os),shell=True)
    if code.returncode==0:
        print("Conatiner stopped Successfully..:)")
    else:
        print("Something wrong happpened..:(")



def docker():
  while True:
    os_name=platform.system().lower()
    if os_name=="linux":
        subprocess.run("clear",shell=True)
    elif os_name=="windows":
        subprocess.run("cls",shell=True)

    print(welcome("Docker"))
    print("""    
    1. Launch a new Conatiner
    2. Pull/Download image
    3. Remove image
    4. Remove Container
    5. See Logs of a Container
    6. Copy Content   from Base OS to Container
    7. Copy Content from Conatiner to Base OS
    8. See the list of all running Containers
    9. See list of all Containers[active and inactive]
   10. Start existing Container
   11. Get terminal of Existing Container
   12. Start Docker Services
   13. Stop running  Container
   14. Stop Docker Services.
   15. Go Back

    
""")
    choice=input("Enter your choice : ")
    if choice =='1':
        launch_container()
    elif choice=='2':
        pull_image()
    elif choice =='3':
        remove_image()
    elif choice=='4':
        remove_container()
    elif choice=='5':
        see_logs()
    elif choice=='6':
        cp_base_to_cont()
    elif choice=='7':
        cp_cont_to_base()
    elif choice =='8':
        see_the_running_cont()
    elif choice=='9':
        see_all_cont()
    elif choice =='10':
        start_exist_cont()
    elif choice=='11':
        get_terminal()
    elif choice=='12':
        start_docker_service()
    elif choice =='13':
        stop_running_docker()
    elif choice=='14':
        stop_docker_services()
    elif choice=='15':
        return

    input("\n\nPress any key to continue...")
    os_name=platform.system().lower()
    if os_name=="linux":
        subprocess.run("clear",shell=True)
    elif os_name=="windows":
        subprocess.run("cls",shell=True)


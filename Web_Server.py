import os
def config():
    while True:
        os.system("clear")
        print("""What you want to change in configuration file
        1. Change default port for http service
        2. Change default folder for webpages
        9. Go back""")
        choice = int(input("\nEnter your choice : "))
        if choice == 9:
            return
        input("\nPress enter to continue.....")
        os.system("clear")
        
def ws():
    os.system("clear")
    print("\n========================================================    Welcome to Web Server    =====================================================================")
    while True:

        print('''Menu :
        1. Install Webserver
        2. Conifgure Webserver
        3. Start and enable Webserver 
        9. Go back'''
        )
        choice = int(input("Enter your choice : "))

        if choice == 1:
            os.system("dnf install httpd")
        elif choice == 2:
            config()
        elif choice == 3:
            os.system("systemctl start httpd && systemctl enable httpd")
            print("Web Services enabled successfully")
        elif choice == 9:
            return
        input("\nPress enter to continue.....")
        os.system("clear")
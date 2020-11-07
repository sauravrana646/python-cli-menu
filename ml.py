
def check_for_pandas():
        import platform #For checking the base-os type like windows ,linux etc
        import subprocess # for running the os level command wih=th the help of the python
        os_name=platform.system().lower() #finding the type of os
        if os_name =="linux":
            print("installing pandas  for you...")
            output=subprocess.run("pip3 install pandas") #installing the corresponding libraries..
            if output.returncode !=0:
                return 1
        elif os_name=="windows":
            print("installing pandas for you...")
            output=subprocess.run("pip install pandas")
            if output.returncode !=0:
                return 1
        return 0

def check_for_scikit_learn():
    import platform
    import subprocess
    os_name=platform.system().lower()
    if os_name =="linux":
        print("Installing scikit-learn  for you..")
        output=subprocess.run("pip3 install scikit-learn")
        if output.returncode !=0:
            return 1
    elif os_name=="windows":
        print("Installing scikit-learn for you..")
        output=subprocess.run("pip install scikit-learn")
        if output.returncode !=0:
            return 1
    return 0


    



def predict():
    from welcome import welcome
    print(welcome("ML World"))
    path=input("Enter the path of the csv file..") #absolute path of the csv file
    try:
     import pandas    #trying for importing the pandas if we got error which means moudle is not present then we will download it
    except ModuleNotFoundError:
      return_value=check_for_pandas()
      if return_value ==0:
        print("Importing  pandas for you")
        import site 
        from importlib import reload
        reload(site) #for refreshing the sys.path value  if we do not do so then we will get error saying module not found..:(
        import pandas
      else:
        print("Unable to install pandas for you..:(")
        return 1
    dataset=pandas.read_csv(path) #retreiving the data from the csv file with the help of the pandas..
    column1=dataset[dataset.columns[0]] #column/filed/infomation/dimension 1
    column2=dataset[dataset.columns[1]] #column/filed/infomation/dimension 2
    column1=column1.values.reshape(-1,1) # for converting the panda's series data-type to numpy 2-D array
    column2=column2.values.reshape(-1,1) #--------------------------------------------------------------#
    try:
        from  sklearn.linear_model import LinearRegression 
    except ModuleNotFoundError:       #same as above if we the LinearRegression is not present we will download it
        output_value=check_for_scikit_learn()
        if output_value ==0:
            print("Importing required library for you..")
            import site
            from importlib import reload
            reload(site)
            from  sklearn.linear_model import LinearRegression
        else:
            print("Unable to download scikit-learn for you..:(")
            return 1
    model=LinearRegression() #for now it is hardcoded that whatever data-set we are gettng from the user is linear(means increses lineary) nand continuous(regression) in nature
    predict=input("Which column you want to predict-:") #The column(Target) which we want to predict
    if predict ==dataset.columns[0]: #if user enter column 1 then the order will be column2(x),column1(y) vice-versa
        model.fit(column2,column1)
    else:
        model.fit(column1,column2)


    while(True):
       predictor_value=float(input("What is the value of the predictor[what is the value of x]?"))
       output=model.predict([[predictor_value]])
       print("The esitimated prediction is -:{}".format(output))
       choice=input("Do you want to predcit more [y/n]?")
       if choice =="n":
           break



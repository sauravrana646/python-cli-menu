def modify_conf(origin,root_object="",OAI=""):
    origin_name = origin
    root_obj = root_object
    if OAI == "":
        oai = OAI
    else : 
        oai = f"origin-access-identity/cloudfront/{OAI}"
    with open('conf.json', 'r') as f:
        data = f.read()

    data = data.replace('BUCKET_NAME_HERE', origin_name)
    data = data.replace('ORIGIN_ACCESS_IDENTITY_HERE', oai)
    data = data.replace('ROOT_OBJECT_HERE', root_obj)
    print(data)
   
    with open("AWS/new_conf.json" , "w") as f:
        f.write(data)

modify_conf("testname")
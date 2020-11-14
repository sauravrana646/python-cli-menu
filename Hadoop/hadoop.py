import subprocess  #for  running the os level commands
import platform #for finding the name of the os
from welcome import welcome



def putFiles(FILE , ip_) : 
  
   sc = subprocess.run(f'ssh {ip_} rm /etc/hadoop/{FILE}.xml',shell=True, capture_output=True)
   sc = subprocess.run(f'scp {FILE}.xml {ip_}:/etc/hadoop',shell=True, capture_output=True)
   sc = subprocess.run(f'rm {FILE}.xml',shell=True)


def buildNode(mode , IP , PORT , IP2 = 'none', file_='none' , filem_ = 'none') : 

    # hadoop = 'hadoop-1.2.1-1.x86_64.rpm'
    # jdk = 'jdk-8u171-linux-x64.rpm'
   
    # installations = [
    #                  f'scp /root/{jdk} {IP}:/root' ,
    #                  f'scp /root/{hadoop} {IP}:/root',
    #                  f'ssh {IP} rpm -i {jdk}' ,
    #                  f'ssh {IP} rpm -i {hadoop} --force'
    #                 ]

    # for op in installations :installation = subprocess.run(op,shell=True, capture_output=True)
    # print('Hadoop installed successfully!' if installation.returncode == 0 else 'Failed to install Hadoop!')
    
    #Building the file
    if mode == 'datanode' : 

        filestatus = subprocess.run(f'ssh {IP} mkdir /{file_}',shell=True, capture_output=True)

        lv_status = input('Do you want to configure storage as logical volume?[Y/N] ')
        if lv_status == 'Y': 
              
            vg_status = input('Want to create volume group?[Y/N] ')
            
            if vg_status == 'Y':
               
               vg_name = input('Enter your VG name -> ')
               
               vg = f'vgcreate {vg_name}'
               no_of_hdd = int(input('Enter number of hard disks -> '))

               for a in range(no_of_hdd) : 
                    hd_n = input('Enter name of hard disk -> ')
                    status = spb.run(f'ssh {IP} pvcreate {hd_n}')
                    vg += ' ' + hd_n
               
               status = subprocess.run(f'ssh {IP} {vg}',shell=True, capture_output=True)

            else : vg_name = input('Enter your VG name -> ')
            
            lv_name = input('Enter your logical volume name -> ')
            lv_size = int(input('Enter logical volume size in GiB -> '))
            lv_path = f'/dev/{vg_name}/{lv_name}'
           
            status = subprocess.run(f'ssh {IP} lvcreate --size {lv_size}G --name {lv_name} {vg_name}',shell=True, capture_output=True)
            
            print(f'logical volume {lv_name} created!' if status.returncode == 0 else 'Failed to create logical volume!')
             
            status = subprocess.run(f'ssh {IP} mkfs.ext4 {lv_path}',shell=True)
            status = subprocess.run(f'ssh {IP} mount {lv_path} /{file_}',shell=True,capture_output=True)
            print('Partition -> Format -> Mount Done!' if status.returncode == 0 else 'Error!')

            size_up = input('Want to add any further space to LV?[Y/N] ')
            
            if size_up == 'Y' : 
             
                s_u = int(input('Enter space in GiB -> '))
                
                status = subprocess.run(f'ssh {IP} lvextend --size +{s_u}G {lv_path}')
                status = subprocess.run(f'ssh {IP} resize2fs {lv_path}',shell=True,capture_output=True)
                
                print(f'logical volume {lv_name} extented by {s_u}GiB' if status.returncode == 0 else 'Failed to extend logical volume!')
            
            

    #Creating core-site file
    #core-site file configuration is same for client , master , slave
    ip = IP2 if mode in ('datanode' , 'client') else IP

    core_ins = [
                '\<configuration\> ',

                '',

                '\<property\> ',

                '\<name\>fs.default.name\</name\> ',

                f'\<value\>hdfs://{ip}:{PORT}\</value\> ',

                '\</property\> ',

                '',

                '\</configuration\> '
               ]

    cs = subprocess.run('cp /root/core-site.xml /var/www/cgi-bin',shell=True,capture_output=True)

    for ins in core_ins : 
           cs = subprocess.run('echo ' + ins + '>> core-site.xml',shell=True,capture_output=True)

    
    #creating hdfs-site file
    if mode in ('datanode' , 'namenode') : 

       X = 'data' if mode == 'datanode' else 'name'
       F =  file_ if mode == 'datanode' else filem_ 

       hdfs_ins = [
                   '\<configuration\> ',

                   '',

                   '\<property\> ',

                   f'\<name\>dfs.{X}.dir\</name\> ',

                   f'\<value\>/{F}\</value\> ',

                   '\</property\> ',

                   '',

                   '\</configuration\> '
                  ]
       cs =  subprocess.run('cp /root/hdfs-site.xml /var/www/cgi-bin',shell=True,capture_output=True)
     
       for ins_ in hdfs_ins : 
          
            cs = subprocess.run('echo ' + ins_ + '>> hdfs-site.xml',shell=True)
       
       putFiles('hdfs-site' , IP)


    else : 
       
       c_d = input('Do you want to change default replication factor and block size?[Y/N]')
       if c_d == 'Y' : 

          cs = subprocess.run(f'cp /root/hdfs-site.xml /var/www/cgi-bin',shell=True,capture_output=True)
          rp = int(input('Enter replication factor -> '))
          bs = int(input('Enter block size in bytes -> '))
          
          client_ins=['\<configuration\>' , '' , '\<property\>' , 
                      '\<name\>dfs.replication\</name\>' , f'\<value\>{rp}\</value\>','\</property\>' , '' , '\<property\>' ,  
                      '\<name\>dfs.block.size\</name\>' , f'\<value\>{bs}\</value\>','\</property\>' , '' , '\</configuration\>']

          for c_li in client_ins : 
                write =  subprocess.run('echo ' + c_li + '>> hdfs-site.xml',shell=True)
          

          putFiles('hdfs-site' , IP)

    #deleting and sending new files

    putFiles('core-site' , IP)

    print('core-site.xml and hdfs-site.xml configured successfully!')
  
     
    if mode == 'namenode' : 
           
           filestatus = subprocess.run(f'ssh {IP} mkdir /{filem_}',shell=True,capture_output=True)
           filestatus = input('Want to format[Y/N]?')
    if filestatus == 'Y':       
           filestatus = subprocess.run(f'ssh {IP} hadoop namenode -format',shell=True,capture_output=True)
    
    if mode in ('namenode' , 'datanode') : 

       runService = input('''
                          ---------------------------------------------
                          Do you want to start the service?[Y/N]
                          ---------------------------------------------
                          '''
                         )
    
       if runService == 'Y' :
   
            sc =  subprocess.run(f'ssh {IP} hadoop-daemon.sh start {mode}',shell=True,capture_output=True)
            print(f'{mode} launched!' if sc[0] == 0 else 'Failed to launch!')
            sc =  subprocess.run('ssh {IP} jps',shell=True,capture_output=True)

    else : print(f'{mode} launched!')       
   
################################################################################
def hadoop():
  while True:
    os_name=platform.system().lower()
    if os_name=="linux":
        subprocess.run("clear",shell=True)
    elif os_name=="windows":
        subprocess.run("cls",shell=True)

    print(welcome("Hadoop"))
    print("""    
   
    1. Setup a Name Node
    2. Setup a Data Node
    3. Setup a Client
    5. Go Back
""")
    choice=input("Enter your choice : ")
    if choice =='1':
        IP = input("Enter the IP of remote system -> ")
        master_file_name = input('Enter your file name -> ')
        port = input('Enter service port number -> ')
        buildNode('namenode' , IP , port , 'none' , 'none' , master_file_name)  
        
    elif choice =='2':
        ip_master = input('Enter ip of master -> ')
        file_name = input('Enter your file name -> ')
        port = input('Enter service port number -> ')
        buildNode('datanode' , IP , port , ip_master , file_name , 'none')
    elif choice =='3':
        ip_master = input('Enter ip of master -> ')
        port = input('Enter ip of service port -> ')
        buildNode('client' , IP , port , ip_master , 'none' , 'none')
    elif choice =='5':
        return    
    input("\n\nPress any key to continue...")
    os_name=platform.system().lower()
    if os_name=="linux":
        subprocess.run("clear",shell=True)
    elif os_name=="windows":
        subprocess.run("cls",shell=True)

       

import paramiko
from paramiko.client import AutoAddPolicy, SSHClient

mfsClientVM = SSHClient()



def copyFile1(dict):

    mfsClientVM.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    mfsClientVM.load_system_host_keys()

    # mfsClientVM.connect(hostname=dict['client']['client1'], username='ubuntu', key_filename='/home/centos/cs6620Key101.pem')

    connectVM = list(dict['client'])[0]
    mfsClientVM.connect(hostname=connectVM, username='admin_user', key_filename='./ssh_scp/real_key.pem')

    sftp_client = mfsClientVM.open_sftp()

    sftp_client.put("./ssh_scp/sample1.sh", "/home/admin_user/sample1.sh")
    # sftp_client.put("sample1.sh", "/home/admin_user/sample1.sh")

    mfsClientVM.exec_command('sh sample1.sh')

    print("Success copy file1 to client1")
    mfsClientVM.close()

def copyFile2(dict):

    mfsClientVM.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    mfsClientVM.load_system_host_keys()

    # mfsClientVM.connect(hostname=dict['client']['client1'], username='ubuntu', key_filename='/home/centos/cs6620Key101.pem')

    connectVM = list(dict['client'])[1]

    mfsClientVM.connect(hostname=connectVM, username='admin_user', key_filename='./ssh_scp/real_key.pem')


    sftp_client = mfsClientVM.open_sftp()
    sftp_client.put("./ssh_scp/sample2.sh", "/home/admin_user/sample2.sh")
    #sftp_client.put("sample2.sh", "/home/admin_user/sample2.sh")


    mfsClientVM.exec_command('sh sample2.sh')

    print("Success copy file2 to client2")
    mfsClientVM.close()


def copyFile3(dict):

    mfsClientVM.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    mfsClientVM.load_system_host_keys()

    # mfsClientVM.connect(hostname=dict['client']['client1'], username='ubuntu', key_filename='/home/centos/cs6620Key101.pem')
    connectVM = ''
    connectVM = list(dict['client'])[2]



    mfsClientVM.connect(hostname=connectVM, username='admin_user', key_filename='./ssh_scp/real_key.pem')

    sftp_client = mfsClientVM.open_sftp()
    sftp_client.put("./ssh_scp/sample3.sh", "/home/admin_user/sample3.sh")
    #sftp_client.put("sample3.sh", "/home/admin_user/sample3.sh")


    mfsClientVM.exec_command('sh sample3.sh')

    print("Success copy file3 to client3")
    mfsClientVM.close()

# if __name__ == '__main__':
#     copyFile(hostname)

#git pull
#intelij commit
#git push



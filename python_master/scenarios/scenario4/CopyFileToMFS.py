import paramiko
from paramiko.client import AutoAddPolicy, SSHClient

mfsClientVM = SSHClient()

list = []


def copyFile1(dict):
    list.append(dict['client']['client1'])
    list.append(dict['client']['client2'])
    list.append(dict['client']['client3'])


    mfsClientVM.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    mfsClientVM.load_system_host_keys()

    # mfsClientVM.connect(hostname=dict['client']['client1'], username='ubuntu', key_filename='/home/centos/cs6620Key101.pem')

    connectVM = list[0]
    # connectVM = list(dict['client'])[0]
    mfsClientVM.connect(hostname=connectVM, username='admin_user', key_filename='cs6620Key101.pem')

    sftp_client = mfsClientVM.open_sftp()

    #sftp_client.put("./ssh_scp/sample1.sh", "/home/admin_user/sample1.sh")
    # sftp_client.put("sample1.sh", "/home/admin_user/sample1.sh")
    sftp_client.put("sample1.sh", "/home/admin_user/sample1.sh")

    mfsClientVM.exec_command('sh sample1.sh')

    print("Success copy file1 to client1")
    mfsClientVM.close()

def copyFile2(dict):

    mfsClientVM.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    mfsClientVM.load_system_host_keys()

    # mfsClientVM.connect(hostname=dict['client']['client1'], username='ubuntu', key_filename='/home/centos/cs6620Key101.pem')

    # connectVM = list(dict['client'])[1]
    connectVM = list[1]

    mfsClientVM.connect(hostname=connectVM, username='admin_user', key_filename='cs6620Key101.pem')


    sftp_client = mfsClientVM.open_sftp()
    # sftp_client.put("./ssh_scp/sample2.sh", "/home/admin_user/sample2.sh")
    sftp_client.put("sample2.sh", "/home/admin_user/sample2.sh")
    #sftp_client.put("sample2.sh", "/home/admin_user/sample2.sh")


    mfsClientVM.exec_command('sh sample2.sh')

    print("Success copy file2 to client2")
    mfsClientVM.close()


def copyFile3(dict):

    mfsClientVM.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    mfsClientVM.load_system_host_keys()

    # mfsClientVM.connect(hostname=dict['client']['client1'], username='ubuntu', key_filename='/home/centos/cs6620Key101.pem')
    connectVM = ''
    #connectVM = list(dict['client'])[2]
    connectVM = list[2]



    mfsClientVM.connect(hostname=connectVM, username='admin_user', key_filename='cs6620Key101.pem')

    sftp_client = mfsClientVM.open_sftp()
    #sftp_client.put("./ssh_scp/sample3.sh", "/home/admin_user/sample3.sh")
    #sftp_client.put("sample3.sh", "/home/admin_user/sample3.sh")
    sftp_client.put("sample3.sh", "/home/admin_user/sample3.sh")


    mfsClientVM.exec_command('sh sample3.sh')

    print("Success copy file3 to client3")
    mfsClientVM.close()

# if __name__ == '__main__':
#     copyFile(hostname)

#git pull
#intelij commit
#git push
dict = {'master': {'master1': '10.0.0.200'},
        'metalogger': {'mettalogger1': '10.0.0.154'},
        'chunkserver': {'chunkserver1': '10.0.0.62',
                        'chunkserver2': '10.0.0.107',
                        'chunkserver3': '10.0.0.162'},
        'client': {'client1': '10.0.0.151',
                   'client2': '10.0.0.131',
                   'client3': '10.0.0.123'}}

copyFile1(dict)
copyFile2(dict)
copyFile3(dict)


import paramiko
from paramiko.client import AutoAddPolicy, SSHClient
import sys
mfsClientVM = SSHClient()



def copyFile(dict):

    mfsClientVM.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    mfsClientVM.load_system_host_keys()

    # mfsClientVM.connect(hostname=dict['client']['client1'], username='ubuntu', key_filename='/home/centos/cs6620Key101.pem')
    connectVM = ''
    for key in dict['client']:
        connectVM = dict['client'][key]



    mfsClientVM.connect(hostname=connectVM, username='admin_user', key_filename='./ssh_scp/real_key.pem')
    sftp_client = mfsClientVM.open_sftp()
    sftp_client.put("./ssh_scp/bash", "./home/ubuntu/bash")


    mfsClientVM.exec_command('sh sample.sh')

    print("Success copy to MFS")

# if __name__ == '__main__':
#     copyFile(hostname)

#git pull
#intelij commit
#git push



import paramiko
from paramiko.client import AutoAddPolicy, SSHClient
import sys
mfsClientVM = SSHClient()
hostname='cl1'


def copyFile():

    mfsClientVM.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    mfsClientVM.load_system_host_keys()

    mfsClientVM.connect(hostname=hostname, username='ubuntu', key_filename='/home/centos/cs6620Key101.pem')

    sftp_client = mfsClientVM.open_sftp()
    sftp_client.put("/home/centos/bash", "/home/ubuntu/bash")


    mfsClientVM.exec_command('sh bash')

    print("Success copy to MFS")

if __name__ == '__main__':
    copyFile()

#git pull
#intelij commit
#git push



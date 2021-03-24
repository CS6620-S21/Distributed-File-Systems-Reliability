import paramiko
from paramiko.client import AutoAddPolicy, SSHClient
import sys
mfsClientVM = SSHClient()
hostname=sys.argv[1]

#1. connect to mfs client vm
mfsClientVM.set_missing_host_key_policy(paramiko.AutoAddPolicy())
mfsClientVM.load_system_host_keys()

mfsClientVM.connect(hostname=hostname, username='ubuntu', key_filename='/home/centos/cs6620Key101.pem')

#2. copy file bash script from local to clientVM
sftp_client = mfsClientVM.open_sftp()
sftp_client.put("/home/centos/bash", "/home/ubuntu/bash")


# execute bash script on clientVM
mfsClientVM.exec_command('sh bash')

print("Success copy to MFS")


#git pull
#intelij commit
#git push



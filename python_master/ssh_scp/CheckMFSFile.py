import paramiko
from paramiko.client import AutoAddPolicy, SSHClient
import sys

mfsClientVM = SSHClient()


hostname=sys.argv[1]

mfsClientVM.set_missing_host_key_policy(paramiko.AutoAddPolicy())
mfsClientVM.load_system_host_keys()
mfsClientVM.connect(hostname=hostname, username='ubuntu', key_filename='/home/centos/cs6620Key101.pem')

print("File name is:")
stdin, stdout, stderr = mfsClientVM.exec_command('cd ..; cd ..; cd mnt; cd mfs; ls')
outlines = stdout.readlines()
stdin.close()
resp = ''.join(outlines)
print(resp)





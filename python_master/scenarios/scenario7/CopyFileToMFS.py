import paramiko
from paramiko.client import AutoAddPolicy, SSHClient
import sys
mfsClientVM = SSHClient()



def copy_and_execute(dict, file_name):

    mfsClientVM.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    mfsClientVM.load_system_host_keys()

    # mfsClientVM.connect(hostname=dict['client']['client1'], username='ubuntu', key_filename='/home/centos/cs6620Key101.pem')
    connectVM = dict['client']['client1']

    mfsClientVM.connect(hostname=connectVM, username='admin_user', key_filename='cs6620Key101.pem')

    stdin, stdout, stderr = mfsClientVM.exec_command('pwd')
    outlines = stdout.readlines()
    stdin.close()
    resp = ''.join(outlines)
    print(resp)


    sftp_client = mfsClientVM.open_sftp()
    source = file_name
    dest = "/home/admin_user/" + file_name
    # printf("source %s copied to MFS and executed", file_name)
    sftp_client.put(source, dest)


    mfsClientVM.exec_command('sh ' + file_name)

    print("File copied to MFS and executed")

# if __name__ == '__main__':
#     copyFile(hostname)

#git pull
#intelij commit
#git push



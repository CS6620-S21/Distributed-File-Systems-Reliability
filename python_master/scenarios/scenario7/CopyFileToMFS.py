import paramiko
from paramiko.client import AutoAddPolicy, SSHClient
import sys
mfsClientVM = SSHClient()



def copy_and_execute(dict, file_name):

    mfsClientVM.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    mfsClientVM.load_system_host_keys()

    # mfsClientVM.connect(hostname=dict['client']['client1'], username='ubuntu', key_filename='/home/centos/cs6620Key101.pem')
    connectVM = ''
    for key in dict['client']:
        connectVM = dict['client'][key]

    mfsClientVM.connect(hostname=connectVM, username='admin_user', key_filename='./ssh_scp/real_key.pem')

    stdin, stdout, stderr = mfsClientVM.exec_command('pwd')
    outlines = stdout.readlines()
    stdin.close()
    resp = ''.join(outlines)
    print(resp)


    sftp_client = mfsClientVM.open_sftp()
    source = "./scenarios/scenario7/" + file_name
    dest = "/home/admin_user/" + file_name
    sftp_client.put(source, dest)


    mfsClientVM.exec_command('sh ' + file_name)

    printf("File %s copied to MFS and executed", file_name)

# if __name__ == '__main__':
#     copyFile(hostname)

#git pull
#intelij commit
#git push



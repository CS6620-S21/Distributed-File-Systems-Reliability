import paramiko
from paramiko.client import AutoAddPolicy, SSHClient
import sys



clients = ['10.0.0.214', '10.0.0.241', 'cl3']

resultList = []
def check():

    for client in clients:
        mfsClientVM = SSHClient()


        hostname=client

        mfsClientVM.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        mfsClientVM.load_system_host_keys()
        mfsClientVM.connect(hostname=hostname, username='ubuntu', key_filename='/home/centos/cs6620Key101.pem')

        print("File name is:")
        stdin, stdout, stderr = mfsClientVM.exec_command('cd ..; cd ..; cd mnt; cd mfs; ls')
        outlines = stdout.readlines()
        stdin.close()
        resp = ''.join(outlines)
        print(resp)
        resultList.append(resp)

    for i in range(1,2):
        if resultList[i-1] != resultList[i]:
            print("Test failure")

    print("Test success")


if __name__ == '__main__':
    check()





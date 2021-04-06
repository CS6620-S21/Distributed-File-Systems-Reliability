import paramiko
from paramiko.client import AutoAddPolicy, SSHClient
import sys



# clients = ['cl1', '10.0.0.241', 'cl3']

clients = []
resultList = []
def check(dict):
    for key in dict['client']:
        clients.append(dict['client'][key])


    for client in clients:
        mfsClientVM = SSHClient()

        hostname=client

        mfsClientVM.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        mfsClientVM.load_system_host_keys()

        #.ssh/cs6620Key101.pem
        # mfsClientVM.connect(hostname=hostname, username='ubuntu', key_filename='/home/centos/cs6620Key101.pem')
        mfsClientVM.connect(hostname=hostname, username='admin_user', key_filename='cs6620Key101.pem')
        # if client == '10.0.0.241':
        #     print("The client ip/name is: cl2")
        # else:
        #     print("The client ip/name is: ", client)
        print("Test result:")
        stdin, stdout, stderr = mfsClientVM.exec_command('cd /mnt/mfs/test7; grep -c "A" testfile.txt')
        outlines = stdout.readlines()
        stdin.close()
        resp = ''.join(outlines)
        print(resp)
        # resultList.append(resp)

    # for i in range(0,len(resultList) - 1):
        if resp == '0':
            print("Test failure")
            return

    print("Test success")
    return


# if __name__ == '__main__':
#     check()







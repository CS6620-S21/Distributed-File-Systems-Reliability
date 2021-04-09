import paramiko
from paramiko.client import AutoAddPolicy, SSHClient




list = []
def check(dict):

    list.append(dict['client']['client1'])
    list.append(dict['client']['client2'])
    list.append(dict['client']['client3'])
    # for key in dict['client']:
    #     clients.append(dict['client'][key])


    # for client in clients:

    client = list[2]
    mfsClientVM = SSHClient()

    mfsClientVM.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    mfsClientVM.load_system_host_keys()

    #.ssh/cs6620Key101.pem
    # mfsClientVM.connect(hostname=hostname, username='ubuntu', key_filename='/home/centos/cs6620Key101.pem')
    mfsClientVM.connect(hostname=client, username='admin_user', key_filename='cs6620Key101.pem')
    # if client == '10.0.0.241':
    #     print("The client ip/name is: cl2")
    # else:
    #     print("The client ip/name is: ", client)
    print("File names are:")
    stdin, stdout, stderr = mfsClientVM.exec_command('cd ..; cd ..; cd mnt; cd mfs; ls')
    outlines = stdout.readlines()
    stdin.close()
    resp = ''.join(outlines)
    print(resp)




    print("Destroy client 1 and client2 manually now")


    if "test1" in resp and "test2" in resp and "test3" in resp:
        print("Test Success")
        return
    print("Test Failure")

    # resultList.append(resp)

    # for i in range(1,len(resultList)):

    # if resultList[i-1] != resultList[i]:
    #     print("Test failure")
    #     return


    # print("Test success")
    # return


# if __name__ == '__main__':
#     check()

#
# dict = {'master': {'master1': '10.0.0.200'},
#         'metalogger': {'mettalogger1': '10.0.0.154'},
#         'chunkserver': {'chunkserver1': '10.0.0.62',
#                         'chunkserver2': '10.0.0.107',
#                         'chunkserver3': '10.0.0.162'},
#         'client': {'client1': '10.0.0.151',
#                    'client2': '10.0.0.131',
#                    'client3': '10.0.0.123'}}







from CheckMFSFile import *
from CopyFileToMFS import *

# combined three copyFiles in one method
# scaniro1:  script_copy_execute_remote_vm
#https://github.com/CS6620-S21/Distributed-File-Systems-Reliability/blob/scenario1/python_master/scenarios/abstract_scenario_driver.py

# from python_master.terraform.driver import *
#from python_master.ansible.ansible_driver import *

import json
import time

# Opening Input config JSON file
# with open('input_config.json') as json_file:
#     data = json.load(json_file)
#
# num_masterservers = data['mfs_num_master_servers']
# num_metaloggers = data['mfs_num_metalogger_servers']
# num_chunkservers = data['mfs_num_chunk_servers']
# num_clientservers = data['mfs_num_client_servers']

# Terraform VM Creation
# Create infratructure
# createInfrastructure(num_masterservers, num_chunkservers,
#                      num_metaloggers, num_clientservers)


# Fetch the dictionary of type
hosts_inventory_dict = {'master': {'master1': '10.0.0.200'},
                        'metalogger': {'mettalogger1': '10.0.0.154'},
                        'chunkserver': {'chunkserver1': '10.0.0.62',
                                        'chunkserver2': '10.0.0.107',
                                        'chunkserver3': '10.0.0.162'},
                        'client': {'client1': '10.0.0.151',
                                   'client2': '10.0.0.131',
                                   'client3': '10.0.0.123'}}
# hosts_inventory_dict = getIPs()



# Wait for VMs to boot up
# time.sleep(120)

# Performs setup of configuration of the different vms that has been created by terraform.
# It creates a dynamic inventory hosts file to be used by ansible, which contains the server types
# and IP address details.
# It then executes the different ansible playbooks for Moose FS setup across different group of servers.
# ansible_conf = MFSAnsibleSetupVMs(data['ansible_basepath'])
# ansible_conf.create_inventory(hosts_inventory_dict)
# ansible_conf.execute_ansible_playbook()


# Testing framework execution using SSH_SCP

# files:
list = ['sample1.sh', 'sample2.sh', 'sample3.sh']

listForClientsVM = []
# copy file from managementVM to clients
for key in hosts_inventory_dict['client']:
    remote_host_ip = dict['client'][key]
    listForClientsVM.append(remote_host_ip)
    username = 'admin_user'
    script_copy_execute_remote(list[0], '/home/admin_user/' + list[0], remote_host_ip, username)
    list.remove(list[0])

# destroy listForClientsVM[0] and listForClientsVM[1]


# fetch file content on client3 vm
resultDict = dict()
resultDict = fetch_moosefs_drive_content(listForClientsVM[2])

# verify file content and file name
verify_file_name_content(resultDict)





# copyFile1(hosts_inventory_dict)
# copyFile2(hosts_inventory_dict)
# copyFile3(hosts_inventory_dict)

# destroy one client

# check if file still there
#check(hosts_inventory_dict)

# Terraform Destroys
# destroyInfrastructure()
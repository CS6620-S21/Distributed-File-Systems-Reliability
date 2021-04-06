
# Read form Config / Default Values

# /Users/aksha/OneDrive/Documents/projects/git/Distributed-File-Systems-Reliability

from CopyFileToMFS import *
from CheckMFSFile import *
# from terraform.driver import *
# from ansible.ansible_driver import *

import json
import time

# # Opening Input config JSON file
# with open('input_config.json') as json_file:
#     data = json.load(json_file)

# num_masterservers = data['mfs_num_master_servers']
# num_metaloggers = data['mfs_num_metalogger_servers']
# num_chunkservers = data['mfs_num_chunk_servers']
# num_clientservers = data['mfs_num_client_servers']


# # Terraform VM Creation
# # Create infratructure
# createInfrastructure(num_masterservers, num_chunkservers,
#                      num_metaloggers, num_clientservers)


# # Fetch the dictionary of type
# # hosts_inventory_dict = {'master': {'master1': '10.0.0.200'},
# #                         'metalogger': {'mettalogger1': '10.0.0.154'},
# #                         'chunkserver': {'chunkserver1': '10.0.0.62',
# #                                         'chunkserver2': '10.0.0.107',
# #                                         'chunkserver3': '10.0.0.162'},
# #                         'client': {'client1': '10.0.0.190',
# #                                    'client2': '10.0.0.223',
# #                                    'client3': '10.0.0.79'}}
# hosts_inventory_dict = getIPs()

# print(hosts_inventory_dict)

# # Wait for VMs to boot up
# time.sleep(120)


# # Performs setup of configuration of the different vms that has been created by terraform.
# # It creates a dynamic inventory hosts file to be used by ansible, which contains the server types
# # and IP address details.
# # It then executes the different ansible playbooks for Moose FS setup across different group of servers.
# ansible_conf = MFSAnsibleSetupVMs(data['ansible_basepath'])
# ansible_conf.create_inventory(hosts_inventory_dict)
# ansible_conf.execute_ansible_playbook()


# Copy and execute first and second part of script
copyFile(hosts_inventory_dict, "test7_1.sh")
copyFile(hosts_inventory_dict, "test7_2.sh")

# Kill client1
# TODO

# # Check the status of the file
# hosts_inventory_dict = getIPs()
# check(hosts_inventory_dict)

# # Terraform Destroys
# destroyInfrastructure()

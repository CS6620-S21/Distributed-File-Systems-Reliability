
# Read form Config / Default Values

# /Users/aksha/OneDrive/Documents/projects/git/Distributed-File-Systems-Reliability

from ssh_scp.CopyFileToMFS import *
from ssh_scp.CheckMFSFile import *
from terraform.driver import *
from ansible.ansible_driver import *
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


# Terraform
# createInfrastructure(num_masterservers, num_chunkservers,
#                      num_metaloggers, num_clientservers)
hosts_inventory_dict = getIPs()
# print(hosts_inventory_dict)
#
# time.sleep(120)


# Performs setup of configuration of the different vms that has been created by terraform.
# It creates a dynamic inventory hosts file to be used by ansible, which contains the server types
# and IP address details.
# It then executes the different ansible playbooks for Moose FS setup across different group of servers.
# ansible_conf = MFSAnsibleSetupVMs(data['ansible_basepath'])
# ansible_conf.create_inventory(hosts_inventory_dict)
# ansible_conf.execute_ansible_playbook()


# SSH_SCP
copyFile(hosts_inventory_dict)
check(hosts_inventory_dict)


# Terraform Destroys
# destroyInfrastructure()


# hosts_inventory_dict = {'master': {'master1': '10.0.0.200'},
#                         'metalogger': {'mettalogger1': '10.0.0.154'},
#                         'chunkserver': {'chunkserver1': '10.0.0.62',
#                                         'chunkserver2': '10.0.0.107',
#                                         'chunkserver3': '10.0.0.162'},
#                         'client': {'client1': '10.0.0.190',
#                                    'client2': '10.0.0.223',
#                                    'client3': '10.0.0.79'}}

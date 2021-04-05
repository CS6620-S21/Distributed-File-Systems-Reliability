
# Read form Config / Default Values

# /Users/aksha/OneDrive/Documents/projects/git/Distributed-File-Systems-Reliability

from ssh_scp.CopyFileToMFS import *
from ssh_scp.CheckMFSFile import *
from terraform.terraformDriver import *
from ansible.ansible_driver import *
from terraform.terraformShell import *
from terraform.stateModifier import *


import json
import time

# Opening Input config JSON file
with open('input_config.json') as json_file:
    data = json.load(json_file)

num_masterservers = data['mfs_num_master_servers']
num_metaloggers = data['mfs_num_metalogger_servers']
num_chunkservers = data['mfs_num_chunk_servers']
num_clientservers = data['mfs_num_client_servers']


# Terraform VM Creation
# Create infratructure

# print("STARTING TERRAFORM CREATION")
# createInfrastructure(num_masterservers, num_chunkservers,num_metaloggers, num_clientservers)


# Fetch the dictionary of type
# hosts_inventory_dict = {'master': {'master1': '10.0.0.200'},
#                         'metalogger': {'mettalogger1': '10.0.0.154'},
#                         'chunkserver': {'chunkserver1': '10.0.0.62',
#                                         'chunkserver2': '10.0.0.107',
#                                         'chunkserver3': '10.0.0.162'},
#                         'client': {'client1': '10.0.0.190',
#                                    'client2': '10.0.0.223',
#                                    'client3': '10.0.0.79'}}

# hosts_inventory_dict = getIPs()
# print(hosts_inventory_dict)
# print("TERRAFORM CREATION COMPLETE")

# Wait for VMs to boot up
# time.sleep(120)


# Performs setup of configuration of the different vms that has been created by terraform.
# It creates a dynamic inventory hosts file to be used by ansible, which contains the server types
# and IP address details.
# It then executes the different ansible playbooks for Moose FS setup across different group of servers.
# print("STARTING ANSIBLE CONFIGURATION")
# ansible_conf = MFSAnsibleSetupVMs(data['ansible_basepath'])
# ansible_conf.create_inventory(hosts_inventory_dict)
# ansible_conf.execute_ansible_playbook()
# print("ANSIBLE CONFIGURATION COMPLETE")

# time.sleep(120)

# Testing framework execution using SSH_SCP
# print("EXECUTING A SANITY TEST")
# copyFile(hosts_inventory_dict)
# check(hosts_inventory_dict)
# print("SANITY TEST COMPLETE")





removeClientInstance()
init()
run()



# removeChunkServer()

# time.sleep(120)
# Terraform Destroys
# print("DESTROYING THE INFRASTRUCTURE")
# destroyInfrastructure()
# print("DESTRUCTION COMPLETE")



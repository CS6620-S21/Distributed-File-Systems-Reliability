
# Read form Config / Default Values

# /Users/aksha/OneDrive/Documents/projects/git/Distributed-File-Systems-Reliability

# from ssh_scp.CopyFileToMFS import *
# from ssh_scp.CheckMFSFile import *
from terraform.terraformDriver import *
from ansible.ansible_driver import *
from terraform.terraformShell import *
from terraform.stateModifier import *




import json
import time




# Terraform VM Creation
# Create infratructure

# print("STARTING TERRAFORM CREATION")
# createInfrastructure(num_masterservers, num_chunkservers,num_metaloggers, num_clientservers)

createInfrastructure(1, 2, 2, 2)


# Fetch the dictionary of type
# hosts_inventory_dict = {'master': {'master1': '10.0.0.200'},
#                         'metalogger': {'mettalogger1': '10.0.0.154'},
#                         'chunkserver': {'chunkserver1': '10.0.0.62',
#                                         'chunkserver2': '10.0.0.107',
#                                         'chunkserver3': '10.0.0.162'},
#                         'client': {'client1': '10.0.0.190',
#                                    'client2': '10.0.0.223',
#                                    'client3': '10.0.0.79'}}

hosts_inventory_dict = getIPs()
print(hosts_inventory_dict)

# print(hosts_inventory_dict)
print("TERRAFORM CREATION COMPLETE")






# time.sleep(120)

# Testing framework execution using SSH_SCP
# print("EXECUTING A SANITY TEST")
# copyFile(hosts_inventory_dict)
# check(hosts_inventory_dict)
# print("SANITY TEST COMPLETE")



# removeChunkServer()

# time.sleep(120)
# Terraform Destroys
print("DESTROYING THE INFRASTRUCTURE")
destroyInfrastructure()
print("DESTRUCTION COMPLETE")



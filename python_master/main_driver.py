
# Read form Config / Default Values


from python_master.ssh_scp.CopyFileToMFS import *
from python_master.ssh_scp.CheckMFSFile import *
from python_master.terraform.driver import createInfrastructure, getIPs
from python_master.ansible.ansible_driver import MFSAnsibleSetupVMs
import json

# Opening Input config JSON file
with open('input_config.json') as json_file:
    data = json.load(json_file)

num_masterservers = data['mfs_num_master_servers']
num_metaloggers = data['mfs_num_metalogger_servers']
num_chunkservers = data['mfs_num_chunk_servers']
num_clientservers = data['mfs_num_client_servers']


# hosts_inventory_dict = {'master': {'master1': '10.0.0.200'},
#                         'metalogger': {'mettalogger1': '10.0.0.154'},
#                         'chunkserver': {'chunkserver1': '10.0.0.62',
#                                         'chunkserver2': '10.0.0.107',
#                                         'chunkserver3': '10.0.0.162'},
#                         'client': {'client1': '10.0.0.190',
#                                    'client2': '10.0.0.223',
#                                    'client3': '10.0.0.79'}}


# Terraform
createInfrastructure(num_masterservers, num_chunkservers,
                     num_metaloggers, num_clientservers)
hosts_inventory_dict = getIPs()

# Ansible
ansible_conf = MFSAnsibleSetupVMs(data['ansible_basepath'])
ansible_conf.create_inventory(hosts_inventory_dict)
ansible_conf.execute_ansible_playbook()

# SSH_SCP
# copyFile(hosts_inventory_dict['client']['client1'])
# check(hosts_inventory_dict['client']['client1'], hosts_inventory_dict['client']['client2'],
#       hosts_inventory_dict['client']['client3'])


# Terraform Destroys
# destroyInfrastructure()

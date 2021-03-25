
# Read form Config / Default Values
from python_master.ssh_scp.CopyFileToMFS import copyFile
from python_master.ssh_scp.CheckMFSFile import *
from python_master.terraform.driver import createInfrastructure, getIPs

masterservers = 5
chunkservers = 5
metaloggers = 5
clientservers = 5

hosts_inventory_dict = {'master': {'master1': '10.0.0.200'},
                        'metalogger': {'mettalogger1': '10.0.0.154'},
                        'chunkserver': {'chunkserver1': '10.0.0.62',
                                        'chunkserver2': '10.0.0.107',
                                        'chunkserver3': '10.0.0.162'},
                        'client': {'client1': '10.0.0.190',
                                   'client2': '10.0.0.223',
                                   'client3': '10.0.0.79'}}


# Terraform
createInfrastructure(masterservers, chunkservers, metaloggers, clientservers)
hosts_inventory_dict = getIPs()

# Ansible
ansible_conf = AnsibleConfigVMs()
ansible_conf.create_inventory(hosts_inventory_dict)
ansible_conf.execute_ansible_playbook()

# SSH_SCP
copyFile(hosts_inventory_dict)
check(hosts_inventory_dict)



# Terraform Destroys
destroyInfrastructure()

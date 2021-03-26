from abc import ABC, abstractmethod
import subprocess
import json

"""
This is an Abstract class which outlines the overall flow & methods required for configuring & setting up any Distributed file system. 

It consists of two major abstract methods, as follows:
1. creating_inventory - This method is used to dynamically create the inventory hosts file.
2. executing_ansible_playook - This method is used to execute the file system specific ansible playbook for installing & configuring.

Any class implementing this Abstract class has to override it's method and provide implementation specific to that file system.
"""


class AbstractFSAnsibleSetupVM(ABC):

    """
    This method is used to create the dynamic runtime inventory file, form the provided input dictionary of IP addresses & different server types.

    Parameters:
    hosts_inventory - takes a dictionary object that specifies the different types of server VMs and it's corresponding IP addresses.
    """
    @abstractmethod
    def create_inventory(self, hosts_inventory: dict):
        pass

    """
    This method is used to execute the ansible playbooks for installing & configuring the different server types in the file system.
    """
    @abstractmethod
    def execute_ansible_playbook(self):
        pass


"""
This class is used for installing & configuring Moose FS & its servers. It provides an implementation for the abstract class 
- AbstractFSAnsibleSetupVM & its methods. 

It creates a dynamic runtime inventory file - hosts.json, that stores the IP details and the different types of servers.

It configures the following four different type of servers with the help of respective ansible playbook:
1. master server
2. metalogger server
3. chunk servers
4. client servers 

"""


class MFSAnsibleSetupVMs(AbstractFSAnsibleSetupVM):

    """
    Initializes the class with following two instance variable:
    1. ansible_basepath -  A string which stores the absolute path of the ansible directory.
    2. ansible_playbooks - A dictionary which stores the playbook details such as the location of ansible playbook on the management VM & corresponding playbook name.
    """

    def __init__(self, ansible_basepath) -> None:
        super().__init__()
        self.ansible_basepath = ansible_basepath
        self.ansible_playbooks = {self.ansible_basepath + '/playbooks/mfsmaster': 'install_master.yml',
                                  self.ansible_basepath + '/playbooks/mfsmetalogger': 'install_metalogger.yml',
                                  self.ansible_basepath + '/playbooks/mfschunkserver': 'install_chunkserver.yml',
                                  self.ansible_basepath + '/playbooks/mfsclient': 'install_client.yml'}

    """
    This method executes the ansible playbooks in sequence, across the respective servers, for its configuration & setup.
    """

    def execute_ansible_playbook(self):
        for playbook_dir, playbook_name in self.ansible_playbooks.items():
            subprocess.run(["ansible-playbook", playbook_name],
                           cwd=playbook_dir)

    """
    This method creates the formatted host inventory file, that is to be used while executing the ansible playbooks. 
    It creates a json format file - hosts.json, which stores details about the group variables or instance variables along with IP addresses.
    """

    def create_inventory(self, input_inventory: dict) -> None:
        formatted_inventory = self.__create_inventory_structure(
            input_inventory)
        self.__write_to_file(formatted_inventory)

    """
    A helper method that writes the formatted dictionary object to a json file on the management vm.
    """

    def __write_to_file(self, formatted_inventory: dict):
        print("Creating JSON hosts file")
        hosts_filepath = self.ansible_basepath + '/hosts.json'
        with open(hosts_filepath, "w") as outfile:
            json.dump(formatted_inventory, outfile)

        print("Done Creating")

    """
    A helper method that creates the formatted inventory structure and stores it a dictionary object.
    """

    def __create_inventory_structure(self, input_inventory: dict) -> dict:
        inventory = dict()
        inventory['all'] = dict()
        inventory['all']['vars'] = self.__prepare_inventory_vars()
        inventory['all']['children'] = self.__prepare_inventory_children(
            input_inventory)
        inventory['all']['vars']['mfsmaster'] = list(input_inventory['master'].values())[
            0]
        return inventory

    """
    A helper method that prepares the common inventory variables.
    """

    def __prepare_inventory_vars(self) -> dict:
        all_vars = dict()
        all_vars['AnsibleUser'] = 'admin_user'
        all_vars['AnsiblePass'] = 'Password1234'
        all_vars['ansible_python_interpreter'] = '/usr/bin/python3'
        return all_vars

    """
    A helper method that prepares the inventory children with the different kinds of servers such as master, metalogger, chunk & client.
    """

    def __prepare_inventory_children(self, input_inventory: dict) -> dict:
        all_children = dict()
        all_children['control'] = self.__prepare_inventory_localhost()
        all_children['master'] = self.__prepare_inventory_mfs(
            input_inventory, 'master')
        all_children['metalogger'] = self.__prepare_inventory_mfs(
            input_inventory, 'metalogger')
        all_children['chunkserver'] = self.__prepare_inventory_mfs(
            input_inventory, 'chunkserver')
        all_children['client'] = self.__prepare_inventory_mfs(
            input_inventory, 'client')
        return all_children

    """
    A helper method to define instance variables for the management vm i.e, localhost vm.
    """

    def __prepare_inventory_localhost(self) -> dict:
        localhost_inventory = dict()
        localhost_inventory['hosts'] = dict()
        localhost_inventory['vars'] = dict()
        localhost_inventory['hosts']['localhost'] = None
        localhost_inventory['vars']['ansible_conection'] = 'local'
        return localhost_inventory

    """
    A helper method that adds the IP address mapping for the different kinds of server. 
    """

    def __prepare_inventory_mfs(self, input_inventory: dict, mfs_server_type: str) -> dict:
        mfs_server_inventory = dict()
        mfs_server_inventory['hosts'] = dict()

        input_servers = input_inventory[mfs_server_type]
        for host_ip in input_servers.values():
            mfs_server_inventory['hosts'][host_ip] = None

        return mfs_server_inventory


# Format of Input host inventory
# hosts_inventory_dict = {'master': {'master1': '10.0.0.200'},
#                         'metalogger': {'mettalogger1': '10.0.0.154'},
#                         'chunkserver': {'chunkserver1': '10.0.0.62',
#                                         'chunkserver2': '10.0.0.107',
#                                         'chunkserver3': '10.0.0.162'},
#                         'client': {'client1': '10.0.0.190',
#                                    'client2': '10.0.0.223',
#                                    'client3': '10.0.0.79'}}

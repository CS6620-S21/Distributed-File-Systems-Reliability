from abc import ABC, abstractmethod
import subprocess
import json

hosts_inventory_dict = {'master': {'master1': '10.0.0.66'},
                        'metalogger': {'mettalogger1': '10.0.0.67'},
                        'chunkserver': {'chunkserver1': '10.0.0.114',
                                        'chunkserver2': '10.0.0.186',
                                        'chunkserver3': '10.0.0.211'},
                        'client': {'client1': '10.0.0.214',
                                   'client2': '10.0.0.241',
                                   'client3': '10.0.0.17'}}


class AbstractAnsibleWorkflow(ABC):

    @abstractmethod
    def create_inventory(self, hosts_inventory: dict):
        pass

    @abstractmethod
    def execute_ansible_playbook(self, ansible_playbook: str):
        pass


class AnsibleConfigVMs(AbstractAnsibleWorkflow):
    def __init__(self) -> None:
        super().__init__()
        self.ansible_basepath = '/home/admin_user/Distributed-File-Systems-Reliability/ansible_master_new'
        self.ansible_playbooks = {self.ansible_basepath + '/playbooks/mfsmaster': 'install_master.yml',
                                  self.ansible_basepath + '/playbooks/mfsmetalogger': 'install_metalogger.yml',
                                  self.ansible_basepath + '/playbooks/mfschunkserver': 'install_chunkserver.yml',
                                  self.ansible_basepath + '/playbooks/mfsclient': 'install_client.yml'}

    def execute_ansible_playbook(self):
        for playbook_dir, playbook_name in self.ansible_playbooks.items():
            # subprocess.run(["pwd"], cwd=dir)
            # subprocess.run(["ls", "-l"], cwd=dir)
            subprocess.run(["ansible-playbook", playbook_name],
                           cwd=playbook_dir)

    def create_inventory(self, input_inventory: dict) -> None:
        formatted_inventory = self.__create_inventory_structure(
            input_inventory)
        self.__write_to_file(formatted_inventory)

    def __write_to_file(self, formatted_inventory: dict):
        print("Creating JSON hosts file")
        hosts_filepath = self.ansible_basepath + '/hosts_temp.json'
        with open(hosts_filepath, "w") as outfile:
            json.dump(formatted_inventory, outfile)

        print("Done Creating")

    def __create_inventory_structure(self, input_inventory: dict) -> dict:
        inventory = dict()
        inventory['all'] = dict()
        inventory['all']['vars'] = self.__prepare_inventory_vars()
        inventory['all']['children'] = self.__prepare_inventory_children(
            input_inventory)
        inventory['all']['vars']['mfsmaster'] = list(input_inventory['master'].values())[
            0]
        return inventory

    def __prepare_inventory_vars(self) -> dict:
        all_vars = dict()
        all_vars['AnsibleUser'] = 'admin_user'
        all_vars['AnsiblePass'] = 'Password1234'
        all_vars['ansible_python_interpreter'] = '/usr/bin/python3'
        return all_vars

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

    def __prepare_inventory_localhost(self) -> dict:
        localhost_inventory = dict()
        localhost_inventory['hosts'] = dict()
        localhost_inventory['vars'] = dict()
        localhost_inventory['hosts']['localhost'] = None
        localhost_inventory['vars']['ansible_conection'] = 'local'
        return localhost_inventory

    def __prepare_inventory_mfs(self, input_inventory: dict, mfs_server_type: str) -> dict:
        mfs_server_inventory = dict()
        mfs_server_inventory['hosts'] = dict()

        input_servers = input_inventory[mfs_server_type]
        for host_ip in input_servers.values():
            mfs_server_inventory['hosts'][host_ip] = None

        return mfs_server_inventory


ansible_conf = AnsibleConfigVMs()
ansible_conf.create_inventory(hosts_inventory_dict)
ansible_conf.execute_ansible_playbook()

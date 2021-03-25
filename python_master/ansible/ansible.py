from abc import ABC, abstractmethod
import subprocess

hosts_inventory_dict = {'master': {'master1': '10.0.0.66'},
                        'metalogger': {'mettalogger1': '10.0.0.67'},
                        'chunkserver': {'chunkserver1': '10.0.0.101',
                                        'chunkserver2': '10.0.0.102',
                                        'chunkserver3': '10.0.0.103'},
                        'client': {'client1': '10.0.0.201',
                                   'client2': '10.0.0.202',
                                   'client3': '10.0.0.203'}}


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
        self.ansible_playbooks_basepath = '/home/admin_user/Distributed-File-Systems-Reliability/ansible_master_new/playbooks/'
        self.ansible_playbooks = {self.ansible_playbooks_basepath + 'mfsmaster': 'install_master',
                                  self.ansible_playbooks_basepath + 'mfsmetalogger': 'install_metalogger',
                                  self.ansible_playbooks_basepath + 'mfschunkserver': 'install_chunkserver',
                                  self.ansible_playbooks_basepath + 'mfsclient': 'install_client'}

    def create_inventory(self, input_inventory: dict, output_inventory_filepath: str) -> None:
        self.__format_inventory(input_inventory)
        self.__write_to_file(output_inventory_filepath)
        print("Hello")

    def execute_ansible_playbook(self):
        # list_run_results = list()
        # index = 0

        # subprocess.run(["cd", self.ansible_playbooks_basepath])
        # subprocess.run(["pwd"], cwd=self.ansible_playbooks_basepath)
        # subprocess.run(["ansible", "--version"],
        #                cwd=self.ansible_playbooks_basepath)

        # list_files = subprocess.run(
        #     ["ls", "-l"], cwd=self.ansible_playbooks_basepath)
        # print("The exit code was: %d" % list_files.returncode)

        for dir, playbook in self.ansible_playbooks.items():
            subprocess.run(["pwd"], cwd=dir)
            subprocess.run(["ls", "-l"], cwd=dir)
            subprocess.run(["ansible", "--version"], cwd=dir)

        print("Hello")

    def __format_inventory(self, input_inventory: dict):
        print("Hello")

    def __write_to_file(self, formatted_inventory: dict, output_inventory_filepath: str):
        print("Hello")


conf = AnsibleConfigVMs()
conf.execute_ansible_playbook()

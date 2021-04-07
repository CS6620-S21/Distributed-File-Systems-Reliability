from abc import ABC, abstractmethod
from paramiko.client import AutoAddPolicy, SSHClient
import paramiko
import sys


class AbstractScenarioDriver(ABC):

    def __init__(self) -> None:
        super().__init__()
        self.num_masterservers = 0
        self.num_metaloggers = 0
        self.num_chunkservers = 0
        self.num_clientservers = 0
        self.ansible_basepath = ''
        self.hosts_inventory_dict = dict()

    @abstractmethod
    def read_config_file(self, config_file_path: str) -> None:
        pass

    @abstractmethod
    def create_infrastructure(self, num_masterservers: int, num_chunkservers: int, num_metaloggers: int, num_clientservers: int) -> None:
        pass

    @abstractmethod
    def get_cluster_ips(self) -> dict:
        pass

    @abstractmethod
    def config_cluster_vms(self) -> None:
        pass

    @abstractmethod
    def scenario_execution(self) -> bool:
        pass

    @abstractmethod
    def clear_infrastructure(self) -> None:
        pass


class Scenario1Driver(AbstractScenarioDriver):

    def __init__(self, hosts_inventory_dict: dict, remote_host_ip: str, local_source_filepath: str, remote_dest_filepath: str) -> None:
        super().__init__()
        self.mfs_ssh_client = SSHClient()
        self.hosts_inventory_dict = hosts_inventory_dict
        self.remote_primary_client_host_ip = list(
            hosts_inventory_dict['client'].values())[0]
        self.remote_secondary_client_host_ips_list = list(
            hosts_inventory_dict['client'].values())[1:]
        self.remote_host_username = 'admin_user'
        self.ssh_key_filepath = '~/.ssh/cs6620Key101.pem'
        self.local_source_filepath = local_source_filepath
        self.remote_dest_filepath = remote_dest_filepath

    def scenario_execution(self) -> bool:
        # Perform Script copying & then execution on client 1 to create dummy file on the mounted moosefs drive
        run_result = self.script_copy_execute_remote_vm(self.local_source_filepath,
                                                        self.remote_dest_filepath,
                                                        self.remote_primary_client_host_ip)

        # A sample result dictionary
        # file_name_content_dict = {
        #                   'files': ['temp_file101', 'temp_file102'],
        #                   'cotent': [file 1 content here', 'file 2 content here' ]
        # }
        file_name_content_dict = dict()
        file_name_content_dict['files'] = list()
        file_name_content_dict['content'] = list()

        # fetch file and its content from primary client vm
        primary_client_details = self.__fetch_moosefs_drive_content(
            self.remote_primary_client_host_ip)

        file_name_content_dict['files'].extend(primary_client_details['files'])
        file_name_content_dict['content'].extend(
            primary_client_details['content'])

        # Perform hard shutdown of client 1 VM

        # fetch file and its content from secondary client vms
        for ip in self.remote_secondary_client_host_ips_list:
            secondary_client_details = self.__fetch_moosefs_drive_content(ip)
            file_name_content_dict['files'].extend(
                secondary_client_details['files'])
            file_name_content_dict['content'].extend(
                secondary_client_details['content'])

        # Verify the file still exists across mounted drive from client 2 & client 3

        return False

    def script_copy_execute_remote_vm(self,
                                      source_filepath: str,
                                      dest_filepath: str,
                                      remote_host_ip: str,
                                      remote_host_username: str,
                                      ssh_key_filepath: str) -> bool:
        try:
            self.__establish_ssh_connection_to_remote(remote_host_ip,
                                                      remote_host_username,
                                                      ssh_key_filepath)
            self.__verify_ssh_connection_established()
            self.__sftp_file_transfer(source_filepath, dest_filepath)
            self.mfs_ssh_client.exec_command('sh ' + dest_filepath)
            print("Remote Script Execution Done")
            return True
        except:
            print("Exception occurred while executing script on remote VM")
            return False

    def __sftp_file_transfer(self, source_filepath, dest_filepath):
        sftp_client = self.mfs_ssh_client.open_sftp()
        sftp_client.put(source_filepath, dest_filepath)

    def __establish_ssh_connection_to_remote(self, remote_host_ip: str,
                                             remote_host_username: str, ssh_key_filepath: str) -> None:
        self.mfs_ssh_client.set_missing_host_key_policy(
            paramiko.AutoAddPolicy())
        self.mfs_ssh_client.load_system_host_keys()
        self.mfs_ssh_client.connect(hostname=remote_host_ip,
                                    username=remote_host_username,
                                    key_filename=ssh_key_filepath)

    def __verify_ssh_connection_established(self):
        stdin, stdout, stderr = self.mfs_ssh_client.exec_command('pwd')
        outlines = stdout.readlines()
        stdin.close()
        resp = ''.join(outlines)
        print(resp)

    def __fetch_moosefs_drive_content(self, remote_host_ip: str) -> dict:
        # A sample result dictionary
        # result_dict = {
        # 'files': ['temp_file101', 'temp_file102'],
        # 'cotent': [file 1 content here', 'file 2 content here' ]
        # }

        result_dict = dict()
        result_dict['files'] = list()
        result_dict['content'] = list()

        mfsClientVM = SSHClient()
        mfsClientVM.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        mfsClientVM.load_system_host_keys()

        mfsClientVM.connect(hostname=remote_host_ip,
                            username=self.remote_host_username,
                            key_filename=self.ssh_key_filepath)

        # Fetch file name on client VM
        stdin, stdout, stderr = mfsClientVM.exec_command(
            'cd /mnt/mfs/; ls')
        outlines = stdout.readlines()
        stdin.close()
        file_name = ''.join(outlines)
        result_dict['files'].append(file_name)
        print('File name is: ' + file_name)

        # Fetch file content on client VM
        stdin, stdout, stderr = mfsClientVM.exec_command(
            'cd /mnt/mfs/; cat ' + file_name)
        outlines = stdout.readlines()
        stdin.close()
        file_content = ''.join(outlines)
        result_dict['content'].append(file_content)
        print('File Content is: ' + file_content)

        return result_dict

    def __verify_file_name_content(seld, file_name_content_dict: dict) -> bool:
        # A sample result dictionary
        # result_dict = {
        # 'files': ['temp_file101', 'temp_file102'],
        # 'cotent': [file 1 content here', 'file 2 content here' ]
        # }

        list_file_names = file_name_content_dict['files']
        list_file_contents = file_name_content_dict['content']

        for i in range(1, len(list_file_names)):
            if list_file_names[i-1] != list_file_names[i] or list_file_contents[i-1] != list_file_contents[i]:
                print("Test Failure")
                return False

        print("Test Success")
        return True

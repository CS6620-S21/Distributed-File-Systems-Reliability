from abc import ABC, abstractmethod
from paramiko.client import AutoAddPolicy, SSHClient
import paramiko
import sys

"""
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

    """


class Scenario1Driver():

    def __init__(self, hosts_inventory_dict: dict, local_source_filepath: str, remote_dest_filepath: str) -> None:
        super().__init__()
        self.mfs_ssh_client = SSHClient()
        self.hosts_inventory_dict = hosts_inventory_dict
        self.remote_primary_client_host_ip = list(
            hosts_inventory_dict['client'].values())[0]
        self.remote_secondary_client_host_ips_list = list(
            hosts_inventory_dict['client'].values())[1:]
        self.remote_host_username = 'admin_user'
        self.local_source_filepath = local_source_filepath
        self.remote_dest_filepath = remote_dest_filepath

    def scenario_execution(self) -> bool:
        # Perform Script copying & then execution on client 1 to create dummy file on the mounted moosefs drive
        run_result = self.__script_copy_execute_remote_vm(self.local_source_filepath,
                                                          self.remote_dest_filepath,
                                                          self.remote_primary_client_host_ip,
                                                          self.remote_host_username)
        if run_result == False:
            print("Unable to copy and execute script on primary client VM")
            return False

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
        # To-Do

        # fetch file and its content from secondary client vms
        for ip in self.remote_secondary_client_host_ips_list:
            secondary_client_details = self.__fetch_moosefs_drive_content(ip)
            file_name_content_dict['files'].extend(
                secondary_client_details['files'])
            file_name_content_dict['content'].extend(
                secondary_client_details['content'])

        # Verify the file still exists across mounted drive from client 2 & client 3
        return self.__verify_file_name_content(file_name_content_dict)

    def __script_copy_execute_remote_vm(self,
                                        source_filepath: str,
                                        dest_filepath: str,
                                        remote_host_ip: str,
                                        remote_host_username: str) -> bool:
        try:
            self.__establish_ssh_connection_to_remote(remote_host_ip,
                                                      remote_host_username)
            print("Established SSH connection to remote VM")
            self.__verify_ssh_connection_established()
            print("Verification of SSH connection complete")
            self.__sftp_file_transfer(source_filepath, dest_filepath)
            print("SFTP file transfer to remote VM done")
            self.mfs_ssh_client.exec_command('sh ' + dest_filepath)
            print("Remote Script Execution Done")
            self.mfs_ssh_client.close()
            return True
        except Exception as e:
            print("Exception occurred while executing script on remote VM")
            print("Error details: " + str(e))
            return False

    def __sftp_file_transfer(self, source_filepath, dest_filepath) -> None:
        sftp_client = self.mfs_ssh_client.open_sftp()
        sftp_client.put(source_filepath, dest_filepath)
        return

    def __establish_ssh_connection_to_remote(self, remote_host_ip: str,
                                             remote_host_username: str) -> None:
        self.mfs_ssh_client.set_missing_host_key_policy(
            paramiko.AutoAddPolicy())
        self.mfs_ssh_client.load_system_host_keys()
        self.mfs_ssh_client.connect(hostname=remote_host_ip,
                                    username=remote_host_username)
        return

    def __verify_ssh_connection_established(self) -> None:
        stdin, stdout, stderr = self.mfs_ssh_client.exec_command('pwd')
        outlines = stdout.readlines()
        stdin.close()
        resp = ''.join(outlines)
        print(resp)
        return

    def __fetch_moosefs_drive_content(self, remote_host_ip: str) -> dict:
        # A sample result dictionary
        # result_dict = {
        # 'files': ['temp_file101', 'temp_file102'],
        # 'cotent': [file 1 content here', 'file 2 content here' ]
        # }

        try:
            result_dict = dict()
            result_dict['files'] = list()
            result_dict['content'] = list()

            mfsClientVM = SSHClient()
            mfsClientVM.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            mfsClientVM.load_system_host_keys()

            mfsClientVM.connect(hostname=remote_host_ip,
                                username=self.remote_host_username)

            # Fetch file name on client VM
            stdin, stdout, stderr = mfsClientVM.exec_command(
                'cd /mnt/mfs/; ls')
            outlines = stdout.readlines()
            stdin.close()
            file_name = ''.join(outlines)
            file_name = str(file_name).rstrip('\n')
            result_dict['files'].append(file_name)
            print('File name is: ' + file_name)

            # Fetch file content on client VM
            stdin, stdout, stderr = mfsClientVM.exec_command(
                'cd /mnt/mfs/; cat ' + file_name)
            outlines = stdout.readlines()
            stdin.close()
            file_content = ''.join(outlines)
            file_content = str(file_content).rstrip('\n')
            result_dict['content'].append(file_content)
            print('File Content is: ' + file_content)

            mfsClientVM.close()
            return result_dict
        except Exception as e:
            print("Something went wrong while fetching the moosefs drive content")
            print("Error Details: " + str(e))
            return None

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


if __name__ == "__main__":
    hosts_inventory_dict = {'master': {'CLUSTER_1617744534_MASTER_1': '10.0.0.186'},
                            'metalogger': {'CLUSTER_1617744534_METALOGGER_1': '10.0.0.70'},
                            'chunkserver': {'CLUSTER_1617744534_CHUNKSERVER_1': '10.0.0.126',
                                            'CLUSTER_1617744534_CHUNKSERVER_2': '10.0.0.245',
                                            },
                            'client': {'CLUSTER_1617744534_CLIENT_1': '10.0.0.76',
                                       'CLUSTER_1617744534_CLIENT_2': '10.0.0.227',
                                       'CLUSTER_1617744534_CLIENT_3': '10.0.0.185'}}
    local_source_filepath = "/home/admin_user/Distributed-File-Systems-Reliability-Sameer/python_master/scenarios/scenario1/script_s1.sh"
    remote_dest_filepath = "/home/admin_user/script_s1.sh"

    s1 = Scenario1Driver(hosts_inventory_dict,
                         local_source_filepath,
                         remote_dest_filepath)
    result = s1.scenario_execution()

    if result:
        print("Scenario execution successfully passed")
    else:
        print("Something went wrong. Scenario execution failed")

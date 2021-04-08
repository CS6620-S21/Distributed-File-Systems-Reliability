from abc import ABC, abstractmethod
from paramiko.client import AutoAddPolicy, SSHClient
import paramiko


class AbstractScenarioDriver(ABC):

    def __init__(self) -> None:
        super().__init__()
        self.num_masterservers = 0
        self.num_metaloggers = 0
        self.num_chunkservers = 0
        self.num_clientservers = 0
        self.ansible_basepath = ''
        self.hosts_inventory_dict = dict()

    # @abstractmethod
    # def read_config_file(self, config_file_path: str) -> None:
    #     pass

    # @abstractmethod
    # def create_infrastructure(self, num_masterservers: int, num_chunkservers: int, num_metaloggers: int, num_clientservers: int) -> None:
    #     pass

    # @abstractmethod
    # def get_cluster_ips(self) -> dict:
    #     pass

    # @abstractmethod
    # def config_cluster_vms(self) -> None:
    #     pass

    # @abstractmethod
    # def scenario_execution(self) -> bool:
    #     pass

    # @abstractmethod
    # def clear_infrastructure(self) -> None:
    #     pass

    def script_copy_execute_remote_vm(self,
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
                                    username=remote_host_username,
                                    key_filename='cs6620Key101.pem')
        return

    def __verify_ssh_connection_established(self) -> None:
        stdin, stdout, stderr = self.mfs_ssh_client.exec_command('pwd')
        outlines = stdout.readlines()
        stdin.close()
        resp = ''.join(outlines)
        print(resp)
        return

    def fetch_moosefs_drive_content(self, remote_host_ip: str) -> dict:
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

            print("Fetching file and its content on VM with IP: " + remote_host_ip)

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

    def verify_file_name_content(seld, file_name_content_dict: dict) -> bool:
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



    def verify_moosefs_drive_content(self, remote_host_ip: str) -> list:
        # A sample result dictionary
        # result_dict = {
        # 'files': ['temp_file101', 'temp_file102'],
        # 'cotent': [file 1 content here', 'file 2 content here' ]
        # }

        try:
            result_list = list()

            mfsClientVM = SSHClient()
            mfsClientVM.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            mfsClientVM.load_system_host_keys()

            mfsClientVM.connect(hostname=remote_host_ip,
                                username=self.remote_host_username,
                                key_filename='cs6620Key101.pem')

            print("Verifying file content on VM with IP: " + remote_host_ip)

            # Count Bs in file on client VM
            stdin, stdout, stderr = mfsClientVM.exec_command(
                'cd /mnt/mfs/test7; grep -c "B" testfile.txt')
            outlines = stdout.readlines()
            stdin.close()
            count = ''.join(outlines)
            # count = int(count)
            result_list.append(count)
            printf('File contains %s Bs', count)

            mfsClientVM.close()
            return result_list

        except Exception as e:
            print("Something went wrong while verifying the moosefs drive content")
            print("Error Details: " + str(e))
            return None

    def verify_file_content(self, file_content_list: list) -> bool:
        for i in range(0, len(file_content_list) - 1):
            if int(file_content_list[i]) == 0:
                print("Test Failure")
                return False

        print("Test Success")
        return True

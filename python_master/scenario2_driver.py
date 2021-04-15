from abc import ABC, abstractmethod
from abstract_scenario_driver import AbstractScenarioDriver
from paramiko.client import AutoAddPolicy, SSHClient
import paramiko
import sys


class Scenario2Driver(AbstractScenarioDriver):

    def __init__(self, config_filepath: str, local_source_filepath: str, remote_dest_filepath: str) -> None:
        super().__init__(config_filepath)
        self.mfs_ssh_client = SSHClient()
        self.remote_primary_client_host_ip = ''
        self.remote_primary_chunk_server_ip = ''
        self.remote_secondary_client_host_ips_list = list()
        self.local_source_filepath = local_source_filepath
        self.remote_dest_filepath = remote_dest_filepath

    def scenario_execution(self) -> bool:
        # Perform Script copying & then execution on client 1 to create dummy file on the mounted moosefs drive
        run_result = self.script_copy_execute_remote_vm(self.local_source_filepath,
                                                        self.remote_dest_filepath,
                                                        self.remote_primary_client_host_ip,
                                                        self.remote_host_username)
        if run_result == False:
            print("Unable to copy and execute script on primary client VM")
            return False

        """
        A sample result dictionary: 
        file_name_content_dict = {
                          'files': ['temp_file101', 'temp_file102'],
                          'cotent': [file 1 content here', 'file 2 content here' ]
        }
        """
        file_name_content_dict = dict()
        file_name_content_dict['files'] = list()
        file_name_content_dict['content'] = list()

        # fetch file and its content from primary client vm
        primary_client_details = self.fetch_moosefs_drive_content(
            self.remote_primary_client_host_ip)

        file_name_content_dict['files'].extend(primary_client_details['files'])
        file_name_content_dict['content'].extend(
            primary_client_details['content'])

        # Perform hard shutdown of chunkserver 1 VM
        self.force_shutdown(self.remote_primary_chunk_server_ip)

        # fetch file and its content from secondary client vms
        for ip in self.remote_secondary_client_host_ips_list:
            secondary_client_details = self.fetch_moosefs_drive_content(ip)
            file_name_content_dict['files'].extend(
                secondary_client_details['files'])
            file_name_content_dict['content'].extend(
                secondary_client_details['content'])

        # Verify the file still exists across mounted drive from client 2 & client 3
        return self.verify_file_name_content(file_name_content_dict)

    def update_primary_secondary_client_hosts(self) -> None:
        self.remote_primary_client_host_ip = list(
            self.hosts_inventory_dict['client'].values())[0]

        self.remote_primary_chunk_server_ip = list(self.hosts_inventory_dict['chunkserver'])[0]

        self.remote_secondary_client_host_ips_list = list(
            self.hosts_inventory_dict['client'].values())

        return

    # To be ignored. For Testing purpose only.
    # def main():
    #     # hosts_inventory_dict = {'master': {'CLUSTER_1617744534_MASTER_1': '10.0.0.186'},
    #     #                         'metalogger': {'CLUSTER_1617744534_METALOGGER_1': '10.0.0.70'},
    #     #                         'chunkserver': {'CLUSTER_1617744534_CHUNKSERVER_1': '10.0.0.126',
    #     #                                         'CLUSTER_1617744534_CHUNKSERVER_2': '10.0.0.245',
    #     #                                         },
    #     #                         'client': {'CLUSTER_1617744534_CLIENT_1': '10.0.0.76',
    #     #                                    'CLUSTER_1617744534_CLIENT_2': '10.0.0.227',
    #     #                                    'CLUSTER_1617744534_CLIENT_3': '10.0.0.185'}}
    # 
    #     local_source_filepath = "/home/admin_user/Distributed-File-Systems-Reliability/python_master/scripts/script_s1.sh"
    #     remote_dest_filepath = "/home/admin_user/script_s1.sh"
    #     config_file_path = "config/s1_config.json"
    # 
    #     s1 = Scenario1Driver(config_file_path,
    #                          local_source_filepath,
    #                          remote_dest_filepath)
    # 
    #     s1.read_update_config(config_file_path)
    #     s1.create_infrastructure(s1.num_masterservers,
    #                              s1.num_chunkservers,
    #                              s1.num_metaloggers,
    #                              s1.num_clientservers)
    #     s1.update_hosts_inventory()
    #     s1.__update_primary_secondary_client_hosts(s1.hosts_inventory_dict)
    #     s1.config_cluster_vms()
    # 
    #     result = s1.scenario_execution()
    # 
    #     if result:
    #         print("Scenario execution successfully passed")
    #     else:
    #         print("Something went wrong. Scenario execution failed")
    # 
    #     s1.clear_infrastructure()
    # 
    #     return

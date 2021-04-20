from abc import ABC, abstractmethod
from abstract_scenario_driver import AbstractScenarioDriver
from paramiko.client import AutoAddPolicy, SSHClient
import paramiko
import sys


class Scenario4Driver(AbstractScenarioDriver):

    def __init__(self, config_filepath: str, local_source_filepath: dict, remote_dest_filepath: dict) -> None:
        super().__init__(config_filepath)
        self.mfs_ssh_client = SSHClient()
        self.client_host_ips_list = list()
        self.local_source_filepath = local_source_filepath
        self.remote_dest_filepath = remote_dest_filepath

    def scenario_execution(self) -> bool:
        # Perform Script copying & then execution on client 1 to create dummy file on the mounted moosefs drive
        for i in range(1, 4):
            run_result = self.script_copy_execute_remote_vm(self.local_source_filepath['client' + str(i)],
                                                            self.remote_dest_filepath['client' + str(i)],
                                                            self.client_host_ips_list[i - 1],
                                                            self.remote_host_username)
            if not run_result:
                print("Unable to copy and execute script on client " + str(i) + " VM")
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
            self.client_host_ips_list[0])

        file_name_content_dict['files'].extend(primary_client_details['files'])
        file_name_content_dict['content'].extend(
            primary_client_details['content'])

        self.force_shutdown(self.client_host_ips_list[0])
        self.force_shutdown(self.client_host_ips_list[1])

        # fetch file and its content from secondary client vms
        for ip in self.client_host_ips_list[2:]:
            secondary_client_details = self.fetch_moosefs_drive_content(ip)
            file_name_content_dict['files'].extend(
                secondary_client_details['files'])
            file_name_content_dict['content'].extend(
                secondary_client_details['content'])

        # Verify the file still exists across mounted drive from client 2 & client 3
        return self.verify_file_name_content(file_name_content_dict)

    def update_client_hosts(self) -> None:
        self.client_host_ips_list = list(
            self.hosts_inventory_dict['client'].values())
        return

    # # To be ignored. For Testing purpose only.
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
    #

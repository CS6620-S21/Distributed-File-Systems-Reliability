from abc import ABC, abstractmethod
from abstract_scenario_driver import AbstractScenarioDriver
from paramiko.client import AutoAddPolicy, SSHClient
import paramiko
import sys


class Scenario4Driver(AbstractScenarioDriver):

    def __init__(self, config_filepath: str,
                 local_source_filepath1: str, remote_dest_filepath1: str,
                 local_source_filepath2: str, remote_dest_filepath2: str,
                 local_source_filepath3: str, remote_dest_filepath3: str
                 ) -> None:
        super().__init__(config_filepath)
        self.mfs_ssh_client = SSHClient()
        #add 3 client host ip
        self.remote_primary_client_host_ip1 = ''
        self.remote_primary_client_host_ip2 = ''
        self.remote_primary_client_host_ip3 = ''

        # self.remote_secondary_client_host_ips_list = list()
        self.local_source_filepath1 = local_source_filepath1
        self.remote_dest_filepath1 = remote_dest_filepath1
        self.local_source_filepath2 = local_source_filepath2
        self.remote_dest_filepath2 = remote_dest_filepath2
        self.local_source_filepath3 = local_source_filepath3
        self.remote_dest_filepath3 = remote_dest_filepath3


    def scenario_execution(self) -> bool:
        # Perform Script copying & then execution on client 1 to create dummy file on the mounted moosefs drive
        run_result1 = self.script_copy_execute_remote_vm(self.local_source_filepath1,
                                                         self.remote_dest_filepath1,
                                                         self.remote_primary_client_host_ip1,
                                                         self.remote_host_username)
        run_result2 = self.script_copy_execute_remote_vm(self.local_source_filepath2,
                                                         self.remote_dest_filepath2,
                                                         self.remote_primary_client_host_ip2,
                                                         self.remote_host_username)
        run_result3 = self.script_copy_execute_remote_vm(self.local_source_filepath3,
                                                         self.remote_dest_filepath3,
                                                         self.remote_primary_client_host_ip3,
                                                         self.remote_host_username)
        if run_result1 == False:
            print("Unable to copy and execute script on primary client VM")
            return False
        if run_result2 == False:
            print("Unable to copy and execute script on primary client VM")
            return False

        if run_result3 == False:
            print("Unable to copy and execute script on primary client VM")
            return False
        #
        # """
        # A sample result dictionary:
        # file_name_content_dict = {
        #                   'files': ['temp_file101', 'temp_file102'],
        #                   'cotent': [file 1 content here', 'file 2 content here' ]
        # }
        # """
        # file_name_content_dict = dict()
        # file_name_content_dict['files'] = list()
        # file_name_content_dict['content'] = list()
        #
        # # fetch file and its content from primary client vm
        # primary_client_details = self.fetch_moosefs_drive_content(
        #     self.remote_primary_client_host_ip)
        #
        # file_name_content_dict['files'].extend(primary_client_details['files'])
        # file_name_content_dict['content'].extend(
        #     primary_client_details['content'])
        #
        # # Perform hard shutdown of client 1 VM
        # self.force_shutdown(self.remote_primary_client_host_ip)

        # fetch file and its content from secondary client vms
        # for ip in self.remote_secondary_client_host_ips_list:
        #     secondary_client_details = self.fetch_moosefs_drive_content(ip)
        #     file_name_content_dict['files'].extend(
        #         secondary_client_details['files'])
        #     file_name_content_dict['content'].extend(
        #         secondary_client_details['content'])

        # Verify the file still exists across mounted drive from client 3
        # return self.verify_file_name_content(file_name_content_dict)
        return True

    def update_primary_secondary_client_hosts(self) -> None:
        self.remote_primary_client_host_ip1 = list(
            self.hosts_inventory_dict['client'].values())[0]

        self.remote_primary_client_host_ip2 = list(
            self.hosts_inventory_dict['client'].values())[1]

        self.remote_primary_client_host_ip3 = list(
            self.hosts_inventory_dict['client'].values())[2]

        return










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
        print("TOTALALLL ---------->>>>>", self.hosts_inventory_dict)
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

        self.remote_primary_chunk_server_ip = list(self.hosts_inventory_dict['chunkserver'].values())[0]

        self.remote_secondary_client_host_ips_list = list(
            self.hosts_inventory_dict['client'].values())

        return

    # To be ignored. For Testing purpose only.
    # CLUSTER_1618450614_CHUNKSERVER_1 = "10.0.0.141"
    # CLUSTER_1618450614_CHUNKSERVER_2 = "10.0.0.50"
    # CLUSTER_1618450614_CLIENT_1 = "10.0.0.226"
    # CLUSTER_1618450614_MASTER_1 = "10.0.0.161"
    # CLUSTER_1618450614_METALOGGER_1 = "10.0.0.194"
    def main():
        hosts_inventory_dict = {'master': {'CLUSTER_1618450614_MASTER_1': '10.0.0.161'},
                                'metalogger': {'CLUSTER_1618450614_METALOGGER_1': '10.0.0.194'},
                                'chunkserver': {'CLUSTER_1618450614_CHUNKSERVER_1': '10.0.0.141',
                                                'CLUSTER_1618450614_CHUNKSERVER_2': '10.0.0.50',
                                                },
                                'client': {'CLUSTER_1618450614_CLIENT_1': '10.0.0.226'}}

        local_source_filepath = "/home/admin_user/Distributed-File-Systems-Reliability/python_master/scripts/script_s2.sh"
        remote_dest_filepath = "/home/admin_user/script_s2.sh"
        config_file_path = "config/s2_config.json"

        s2 = Scenario2Driver(config_file_path,
                             local_source_filepath,
                             remote_dest_filepath)

        s2.hosts_inventory_dict = hosts_inventory_dict

        s2.read_update_config(config_file_path)
        s2.create_infrastructure(s2.num_masterservers,
                                 s2.num_chunkservers,
                                 s2.num_metaloggers,
                                 s2.num_clientservers)
        # s2.update_hosts_inventory()
        s2.update_primary_secondary_client_hosts()
        # s2.config_cluster_vms()

        result = s2.scenario_execution()

        if result:
            print("Scenario execution successfully passed")
        else:
            print("Something went wrong. Scenario execution failed")

        # s1.clear_infrastructure()

        return
if __name__ == '__main__':
    Scenario2Driver.main()


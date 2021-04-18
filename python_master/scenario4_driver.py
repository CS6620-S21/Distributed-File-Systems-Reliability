from abc import ABC, abstractmethod
import paramiko
from abstract_scenario_driver import AbstractScenarioDriver
from paramiko.client import AutoAddPolicy, SSHClient
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

        # if self.compare_name_content_client3() == True:
        #     print("Success! Client3 includes all files")
        #
        # if self.compare_name_content_client3() == False:
        #     print("Failure! Client3 not includes all files")


        if self.compare_names_contents() == True:
            print("Success! Client3 includes all files")
            return True

        print("Failure! Client3 not includes all files")
        return False



    def compare_names_contents(self):
        names = ['s4_1_test_file.txt', 's4_2_test_file.txt', 's4_3_test_file.txt']
        file_name1 = self.file_name_compare_s4(self.remote_primary_client_host_ip1)
        print("client1 includes: " + file_name1)
        file_name2 = self.file_name_compare_s4(self.remote_primary_client_host_ip2)
        print("client2 includes: " + file_name2)


        file_c1 = self.content_in_client(self, self.remote_primary_client_host_ip1, names[0])
        file_c2 = self.content_in_client(self, self.remote_primary_client_host_ip2, names[1])

        #shutdown c1 and c2
        self.force_shutdown(self.remote_primary_client_host_ip1)
        self.force_shutdown(self.remote_primary_client_host_ip2)

        #check c3 names

        file_name3 = self.file_name_compare_s4(self.remote_primary_client_host_ip3)
        print("client3 includes: " + file_name3)

        if file_name1 not in file_name3:
            return False

        if file_name2 not in file_name3:
            return False

        #check c3 files
        check_file_c1 = self.content_in_client(self, self.remote_primary_client_host_ip3, names[0])
        check_file_c2 = self.content_in_client(self, self.remote_primary_client_host_ip3, names[1])

        if file_c1 != check_file_c1:
            return False
        if file_c2 != check_file_c2:
            return False


        return True


    # def compare_name_content_client3(self):
    #     # names = ['s4_1_test_file.txt', 's4_2_test_file.txt', 's4_3_test_file.txt']
    #     file_c1 = self.content_in_client(self, self.remote_primary_client_host_ip1, names[0])
    #     file_c2 = self.content_in_client(self, self.remote_primary_client_host_ip2, names[1])
    #
    #     check_file_c1 = self.content_in_client(self, self.remote_primary_client_host_ip3, names[0])
    #     check_file_c2 = self.content_in_client(self, self.remote_primary_client_host_ip3, names[1])
    #
    #     if file_c1 != check_file_c1:
    #         return False
    #     if file_c2 != check_file_c2:
    #         return False
    #
    #     return True


    def update_primary_secondary_client_hosts_s4(self) -> None:
        self.remote_primary_client_host_ip1 = list(
            self.hosts_inventory_dict['client'].values())[0]

        self.remote_primary_client_host_ip2 = list(
            self.hosts_inventory_dict['client'].values())[1]

        self.remote_primary_client_host_ip3 = list(
            self.hosts_inventory_dict['client'].values())[2]

        return










from abc import ABC, abstractmethod
from abstract_scenario_driver import AbstractScenarioDriver
from paramiko.client import AutoAddPolicy, SSHClient
import paramiko
import sys

ab = AbstractScenarioDriver("abc")
run_result1 = ab.script_copy_execute_remote_vm("/home/admin_user/Distributed-File-Systems-Reliability/python_master/scripts/script4_1.sh","/home/admin_user/script4_1.sh","10.0.0.250","admin_user")
# class Scenario4Driver(AbstractScenarioDriver):
#
#     def __init__(self, config_filepath: str,
#                  local_source_filepath1: str, remote_dest_filepath1: str,
#                  local_source_filepath2: str, remote_dest_filepath2: str,
#                  local_source_filepath3: str, remote_dest_filepath3: str
#             ) -> None:
#         super().__init__(config_filepath)
#         self.mfs_ssh_client = SSHClient()
#         #add 3 client host ip
#         self.remote_primary_client_host_ip1 = ''
#         self.remote_primary_client_host_ip2 = ''
#         self.remote_primary_client_host_ip3 = ''
#
#         self.remote_secondary_client_host_ips_list = list()
#         self.local_source_filepath1 = local_source_filepath1
#         self.remote_dest_filepath1 = remote_dest_filepath1
#         self.local_source_filepath2 = local_source_filepath2
#         self.remote_dest_filepath2 = remote_dest_filepath2
#         self.local_source_filepath3 = local_source_filepath3
#         self.remote_dest_filepath3 = remote_dest_filepath3
#
#     def scenario_execution(self) -> bool:
        # Perform Script copying & then execution on client 1 to create dummy file on the mounted moosefs drive
        # run_result1 = self.script_copy_execute_remote_vm(self.local_source_filepath1,
        #                                                 self.remote_dest_filepath1,
        #                                                 self.remote_primary_client_host_ip1,
        #                                                 self.remote_host_username)
        # run_result2 = self.script_copy_execute_remote_vm(self.local_source_filepath2,
        #                                                  self.remote_dest_filepath2,
        #                                                  self.remote_primary_client_host_ip2,
        #                                                  self.remote_host_username)
        # run_result3 = self.script_copy_execute_remote_vm(self.local_source_filepath3,
        #                                                  self.remote_dest_filepath3,
        #                                                  self.remote_primary_client_host_ip3,
        #                                                  self.remote_host_username)



        # run_result1 = self.script_copy_execute_remote_vm("/home/admin_user/Distributed-File-Systems-Reliability/python_master/scripts/script4_1.sh",
        #                                                  "/home/admin_user/script4_1.sh",
        #                                                  "10.0.0.250",
        #                                                 "admin_user")
        # if run_result1 == False:
        #     print("Unable to copy and execute script on primary client1 VM")
        #     return False
        # if run_result2 == False:
        #     print("Unable to copy and execute script on primary client2 VM")
        #     return False
        # if run_result3 == False:
        #     print("Unable to copy and execute script on primary client3 VM")
        #     return False

        #
        # """
        # A sample result dictionary:
        # file_name_content_dict = {
        #                   'files': ['temp_file101', 'temp_file102'],
        #                   'cotent': [file 1 content here', 'file 2 content here' ]
        # }
        # """
        #
        # list = ['s4_test_file1.txt', 's4_test_file2.txt']
        #
        #
        # preStr1 = self.fetch_moosefs_drive_content_s4(self.remote_primary_client_host_ip1, list[0])
        # preStr2 = self.fetch_moosefs_drive_content_s4(self.remote_primary_client_host_ip2, list[1])



        # result_dict1 = self.fetch_moosefs_drive_content(self.remote_primary_client_host_ip1)
        # result_dict2 = self.fetch_moosefs_drive_content(self.remote_primary_client_host_ip2)
        

        # self.force_shutdown(self.remote_primary_client_host_ip1)
        # self.force_shutdown(self.remote_primary_client_host_ip2)

        # result_dict3 = self.fetch_moosefs_drive_content(self.remote_primary_client_host_ip3)

        # check if content and title client1 in client3

        # client3TitleStr = self.fetch_moosefs_drive_title_s4(self.remote_primary_client_host_ip3)
        #
        # if list[0] not in client3TitleStr:
        #     return False
        #
        # if list[1] not in client3TitleStr:
        #     return False
        #
        #
        # str1 = self.fetch_moosefs_drive_content_s4(self.remote_primary_client_host_ip3, list[0])
        # if str1 != preStr1:
        #     print("not contain scenario4.1")
        #     return False
        #
        # str2 = self.fetch_moosefs_drive_content_s4(self.remote_primary_client_host_ip3, list[1])
        # if str2 != preStr2:
        #     print("not contain scenario4.2")
        #     return False
        #
        # return True


# driver = Scenario4Driver()














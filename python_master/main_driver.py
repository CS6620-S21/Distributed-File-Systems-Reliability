from abstract_scenario_driver import AbstractScenarioDriver
from scenario1_driver import Scenario1Driver
from scenario7_driver import Scenario7Driver

class main_driver:
    def __init__(self) -> None:
        self.scenario1_config_file_path = "config/s1_config.json"
        self.scenario2_config_file_path = "config/s2_config.json"
        self.scenario7_config_file_path = "config/s7_config.json"

    def common_setup_control_flow(self, ScenarioDriver: AbstractScenarioDriver, config_file_path: str) -> None:
        ScenarioDriver.read_update_config(config_file_path)
        ScenarioDriver.create_infrastructure(ScenarioDriver.num_masterservers,
                                             ScenarioDriver.num_chunkservers,
                                             ScenarioDriver.num_metaloggers,
                                             ScenarioDriver.num_clientservers)
        ScenarioDriver.update_hosts_inventory()
        ScenarioDriver.config_cluster_vms()
        return

    def execute_scenario1(self):
        local_source_filepath = "/home/admin_user/Distributed-File-Systems-Reliability/python_master/scripts/script_s1.sh"
        remote_dest_filepath = "/home/admin_user/script_s1.sh"

        try:
            print("Performing Scenario 1 execution...")
            scenario1 = Scenario1Driver(config_filepath=self.scenario1_config_file_path,
                                        local_source_filepath=local_source_filepath,
                                        remote_dest_filepath=remote_dest_filepath,
                                        server_kill_type='client')

            self.common_setup_control_flow(
                scenario1, self.scenario1_config_file_path)
            scenario1.update_primary_secondary_client_hosts()
            execution_result = scenario1.scenario_execution()

            if execution_result:
                print("Scenario execution successfully passed")
            else:
                print("Something went wrong. Scenario execution failed")

            scenario1.clear_infrastructure()
            print("Scenario 1 execution complete")

        except Exception as e:
            print("Error occurred in Scenario Execution: " + str(e))

    def execute_scenario7(self):
        local_source_filepath = "/home/admin_user/Distributed-File-Systems-Reliability/python_master/scripts/script_s7.sh"
        remote_dest_filepath = "/home/admin_user/script_s7.sh"

        try:
            print("Performing Scenario 7 execution...")
            scenario7 = Scenario7Driver(config_filepath=self.scenario7_config_file_path,
                                        local_source_filepath=local_source_filepath,
                                        remote_dest_filepath=remote_dest_filepath)

            self.common_setup_control_flow(
                scenario7, self.scenario7_config_file_path)
            scenario7.update_primary_secondary_client_hosts()
            execution_result = scenario7.scenario_execution()

            if execution_result:
                print("Scenario execution successfully passed")
            else:
                print("Something went wrong. Scenario execution failed")

            scenario7.clear_infrastructure()
            print("Scenario 7 execution complete")

        except Exception as e:
            print("Error occurred in Scenario Execution: " + str(e))

    def execute_scenario2(self):
        local_source_filepath = "/home/admin_user/Distributed-File-Systems-Reliability/python_master/scripts/script_s2.sh"
        remote_dest_filepath = "/home/admin_user/script_s2.sh"

        try:
            print("Performing Scenario 2 execution...")
            scenario2 = Scenario1Driver(config_filepath=self.scenario2_config_file_path,
                                        local_source_filepath=local_source_filepath,
                                        remote_dest_filepath=remote_dest_filepath,
                                        server_kill_type='chunkserver')

            self.common_setup_control_flow(
                scenario2, self.scenario2_config_file_path)
            scenario2.update_primary_secondary_client_hosts()
            execution_result = scenario2.scenario_execution()

            if execution_result:
                print("Scenario execution successfully passed")
            else:
                print("Something went wrong. Scenario execution failed")

            scenario2.clear_infrastructure()
            print("Scenario 2 execution complete")

        except Exception as e:
            print("Error occurred in Scenario Execution: " + str(e))

if __name__ == "__main__":
    driver = main_driver()
    # driver.execute_scenario1()
    driver.execute_scenario7()
    # driver.execute_scenario2()

from abstract_scenario_driver import AbstractScenarioDriver
from scenario1_driver import Scenario1Driver

from scenario4_driver import Scenario4Driver


class main_driver:
    def __init__(self) -> None:
        self.scenario1_config_file_path = "config/s1_config.json"
        self.scenario4_config_file_path = "config/s4_config.json"

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
                                        remote_dest_filepath=remote_dest_filepath)

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

    def execute_scenario4(self):
        local_source_filepath1 = "/home/admin_user/Distributed-File-Systems-Reliability/python_master/scripts/script4_1.sh"
        remote_dest_filepath1 = "/home/admin_user/script4_1.sh"
        local_source_filepath2 = "/home/admin_user/Distributed-File-Systems-Reliability/python_master/scripts/script4_2.sh"
        remote_dest_filepath2 = "/home/admin_user/script4_2.sh"
        local_source_filepath3 = "/home/admin_user/Distributed-File-Systems-Reliability/python_master/scripts/script4_3.sh"
        remote_dest_filepath3 = "/home/admin_user/script4_3.sh"

        try:
            print("Performing Scenario 1 execution...")
            scenario4 = Scenario4Driver(config_filepath=self.scenario4_config_file_path,
                                        local_source_filepath1=local_source_filepath1,
                                        remote_dest_filepath1=remote_dest_filepath1,
                                        local_source_filepath2=local_source_filepath2,
                                        remote_dest_filepath2=remote_dest_filepath2,
                                        local_source_filepath3=local_source_filepath3,
                                        remote_dest_filepath3=remote_dest_filepath3
                                        )

            self.common_setup_control_flow(
                scenario4, self.scenario4_config_file_path)
            #scenario1.update_primary_secondary_client_hosts()
            execution_result = scenario4.scenario_execution()

            if execution_result:
                print("Scenario execution successfully passed")
            else:
                print("Something went wrong. Scenario execution failed")

            scenario4.clear_infrastructure()
            print("Scenario 4 execution complete")

        except Exception as e:
            print("Error occurred in Scenario Execution: " + str(e))


if __name__ == "__main__":
    driver = main_driver()
    driver.execute_scenario4()

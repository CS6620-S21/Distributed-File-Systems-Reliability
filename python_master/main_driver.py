from abstract_scenario_driver import AbstractScenarioDriver
from scenario1_driver import Scenario1Driver


class main_driver:
    def __init__(self) -> None:
        self.scenario1_config_file_path = "config/s1_config.json"
        pass

    def common_setup_control_flow(self, ScenarioDriver: AbstractScenarioDriver, config_file_path: str) -> None:
        ScenarioDriver.read_update_config(config_file_path)
        ScenarioDriver.create_infrastructure(ScenarioDriver.num_masterservers,
                                             ScenarioDriver.num_chunkservers,
                                             ScenarioDriver.num_metaloggers,
                                             ScenarioDriver.num_clientservers)
        ScenarioDriver.update_hosts_inventory()
        ScenarioDriver.__update_primary_secondary_client_hosts(
            ScenarioDriver.hosts_inventory_dict)
        ScenarioDriver.config_cluster_vms()

    def execute_scenario1(self):
        local_source_filepath = "/home/admin_user/Distributed-File-Systems-Reliability/python_master/scripts/script_s1.sh"
        remote_dest_filepath = "/home/admin_user/script_s1.sh"

        try:
            print("Performing Scenario 1 execution...")
            scenario1 = Scenario1Driver(config_filepath=self.scenario1_config_file_path,
                                        local_source_filepath=local_source_filepath,
                                        remote_dest_filepath=remote_dest_filepath)

            self.common_setup_control_flow(scenario1)
            execution_result = scenario1.scenario_execution()

            if execution_result:
                print("Scenario execution successfully passed")
            else:
                print("Something went wrong. Scenario execution failed")

            scenario1.clear_infrastructure()
            print("Scenario 1 execution complete")

        except Exception as e:
            print("Error occurred in Scenario Execution: " + str(e))


if __name__ == "__main__":
    driver = main_driver()
    driver.execute_scenario1()

from abc import ABC, abstractmethod


class AbstractScenarioDriver(ABC):

    def __init__(self) -> None:
        super().__init__()
        self.num_masterservers = 0
        self.num_metaloggers = 0
        self.num_chunkservers = 0
        self.num_clientservers = 0
        self.ansible_basepath = ''
        self.hosts_inventory_dict = dict()

    @abstractmethod
    def read_config_file(self, config_file_path: str) -> None:
        pass

    @abstractmethod
    def create_infrastructure(self, num_masterservers: int, num_chunkservers: int, num_metaloggers: int, num_clientservers: int) -> None:
        pass

    @abstractmethod
    def get_cluster_ips(self) -> dict:
        pass

    @abstractmethod
    def config_cluster_vms(self) -> None:
        pass

    @abstractmethod
    def scenario_execution(self) -> bool:
        pass

    @abstractmethod
    def clear_infrastructure(self) -> None:
        pass

from pathlib import Path
from typing import Optional

from pydantic import BaseModel
from yaml import safe_load


class Host(BaseModel):
    hostname: str
    ip: str


class Config(BaseModel):
    """
    Configuration class for Nemo.

    Attributes:
        config_path (Path): Path to the configuration file.
        timeout (int): Timeout for network operations.
        __hosts (Optional[list[Host]]): List of hosts defined in the configuration file.
    """

    config_path: Path
    timeout: Optional[int] = None
    __hosts: Optional[list[Host]] = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        config_yaml = self.__load__(self.config_path)

        # Load hosts from configuration file
        try:
            self.__hosts = [Host(**host) for host in config_yaml["hosts"]]
        except KeyError:
            self.__hosts = []
            raise ValueError("No hosts found in configuration file")

    def __load__(self, file_path: Path) -> dict:
        """
        Load YAML configuration file and return as a Python dictionary.

        Args:
            file_path (Path): Path to the configuration file.

        Returns:
            dict: Configuration file as a dictionary.
        """
        with open(file_path, "r") as file:
            return safe_load(file)
            
    def get_hosts(self) -> Optional[list[Host]]:
        """
        Get the list of hosts defined in the configuration file.

        Returns:
            Optional[list[Host]]: List of hosts defined in the configuration file.
        """
        return self.__hosts

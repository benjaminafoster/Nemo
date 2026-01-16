from pydantic import BaseModel
from typing import Optional
from yaml import safe_load
from pathlib import Path

class Host(BaseModel):
    hostname: str
    ip: str


class Config(BaseModel):
    config_path: Path
    hosts: Optional[list[Host]] = None
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        config_yaml = self.__load__(self.config_path)
        self.hosts = [Host(**host) for host in config_yaml['hosts']]
    
    def __load__(self, file_path: Path) -> dict:
        with open(file_path, 'r') as file:
            return safe_load(file)
from yaml import safe_load
from pydantic import BaseModel
from pathlib import Path
from os import environ

environ['PYDANTIC_ERRORS_INCLUDE_URL'] = 'False'

print("Welcome to Nemo!")

CURRENT_DIRECTORY = Path(__file__).parent.resolve()
CONFIG_DIRECTORY = CURRENT_DIRECTORY / 'config'

TARGETS_FILE_PATH = CONFIG_DIRECTORY / 'Targets.yaml'

class Host(BaseModel):
    hostname: str
    ip: str

def load_config_yaml(file_path) -> dict:
    with open(file_path, 'r') as file:
        return safe_load(file)
        
config = load_config_yaml(TARGETS_FILE_PATH)

try:
    config_hosts = config['hosts']
    valid_hosts = [Host(**host) for host in config_hosts]
except ValueError as e:
    print(f"Invalid host configuration: {e}")
    exit(1)

for host in valid_hosts:
    print(host.hostname)
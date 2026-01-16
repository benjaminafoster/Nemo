from pathlib import Path
from os import environ
from configuration import Config

environ['PYDANTIC_ERRORS_INCLUDE_URL'] = 'False'

print("Welcome to Nemo!")

CURRENT_DIRECTORY = Path(__file__).parent.resolve()
CONFIG_DIRECTORY = CURRENT_DIRECTORY / 'config'
TARGETS_FILE_PATH = CONFIG_DIRECTORY / 'Targets.yaml'


        
config = Config(config_path=TARGETS_FILE_PATH)

if config.hosts:
    for host in config.hosts:
        print(host.hostname)
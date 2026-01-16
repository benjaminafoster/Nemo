from pathlib import Path
from os import environ
from Configuration import Config
from Scan import Scanner

environ['PYDANTIC_ERRORS_INCLUDE_URL'] = 'False'

print("Welcome to Nemo!")

CURRENT_DIRECTORY = Path(__file__).parent.resolve()
CONFIG_DIRECTORY = CURRENT_DIRECTORY / 'config'
TARGETS_FILE_PATH = CONFIG_DIRECTORY / 'Targets.yaml'


        
config = Config(config_path=TARGETS_FILE_PATH, timeout=3)

scanner = Scanner(config)

scanner.host_icmp_scan()
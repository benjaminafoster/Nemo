import sys
from pathlib import Path
from os import environ
from Configuration import Config
from Scan import Scanner

environ['PYDANTIC_ERRORS_INCLUDE_URL'] = 'False'

print("Welcome to Nemo!")

CURRENT_DIRECTORY = Path(__file__).parent.resolve()
CONFIG_DIRECTORY = CURRENT_DIRECTORY / 'config'
TARGETS_FILE_PATH = CONFIG_DIRECTORY / 'Targets.yaml'

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass
nemo_env = environ.get('NEMO_ENV', 'testing')

# Create config object based on environment
if nemo_env == "testing":
    config = Config(config_path=CONFIG_DIRECTORY / 'test-targets.yaml')
elif nemo_env == "development":
    print("No development hosts defined...yikes")
    sys.exit(1)
else:
    config = Config(config_path=TARGETS_FILE_PATH)

# test logic below
scanner = Scanner(config)

scanner.host_icmp_scan()
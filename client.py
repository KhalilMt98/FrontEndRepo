import yaml
import os

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), '../config.yaml')
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
        return config

config = load_config()
if config['run_localhost']:
    print("Running in localhost mode in frontend")

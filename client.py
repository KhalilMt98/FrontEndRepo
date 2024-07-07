import yaml

def load_config():
    with open('../config.yaml', 'r') as file:
        config = yaml.safe_load(file)
        return config

config = load_config()
if config['run_localhost']:
    print("Running in localhost mode in frontend")

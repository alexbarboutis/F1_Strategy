import yaml

def load_race_config(config_path: str):
    """
    Load race configuration from a YAML file.
    Returns a dictionary with race and car settings.
    """
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    return config

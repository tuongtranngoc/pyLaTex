import os
import re
import yaml


def load_config(file_path):
    """
    Load config from yml/yaml file.
    Args:
        file_path (str): Path of the config file to be loaded.
    Returns: config
    """
    ext = os.path.splitext(file_path)[1]
    assert ext in ['.yml', '.yaml'], "only support yaml files for now"
    with open(file_path, 'rb') as f:
        config = yaml.load(f, Loader=yaml.Loader)

    return config


def escape_special_symbols(text):
    special_symbols = ['_', '&']
    for s in special_symbols:
        text = text.replace(s, f'\{s}')
    return text
from pathlib import Path
import yaml

# Directories
BASE_DIR = Path(__file__).parent.parent.absolute()
CONFIG_DIR = Path(BASE_DIR, "config")
DATASET_DIR = Path(BASE_DIR, "dataset")
IMAGES_DIR = Path(BASE_DIR, "images")
DATASET_YAML = Path(CONFIG_DIR, "dataset.yaml")

# Editing paths in yaml configs
with open(DATASET_YAML, 'r') as read_file:
    contents = yaml.safe_load(read_file)

contents["path"] = DATASET_DIR.as_posix() # returns as string

with open(DATASET_YAML, 'w') as write_file:
    yaml.dump(contents, write_file, sort_keys=False)
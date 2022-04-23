from lib.configuration import Configuration
from lib.preprocessing.read.read_pheme.read_pheme_dataset import ReadPhemeDataset
from os import environ as env


Configuration().config()
ReadPhemeDataset(path=env['PHEME_DATASET_DIR'])
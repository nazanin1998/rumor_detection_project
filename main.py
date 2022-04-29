from lib.configuration import Configuration
from lib.preprocessing.pheme.preprocessing import PreProcessing
from lib.read_datasets.pheme.read_pheme_dataset import ReadPhemeDataset
from os import environ as env

Configuration().config()
# ----------------------------PHEME dataset
events = ReadPhemeDataset(path=env['PHEME_DATASET_DIR']).events
preprocessing = PreProcessing(events=events)
# preprocessing.preprocess()

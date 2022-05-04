from lib.configuration import Configuration
from lib.preprocessing.pheme.preprocessing import PreProcessing
from lib.read_datasets.pheme.read_pheme_dataset import ReadPhemeDataset
from os import environ as env
import lib.constants as constants

Configuration().config()
# ----------------------------PHEME dataset
dirs = ReadPhemeDataset.read_directories(constants.PHEME_CSV_DIR)
readPhemeDataset = ReadPhemeDataset(path=env['PHEME_DATASET_DIR'])

if dirs is None or not dirs.__contains__(constants.PHEME_CSV_NAME):
    readPhemeDataset.read_json_dataset()
else:
    readPhemeDataset.read_csv_dataset()

PreProcessing(df=readPhemeDataset.df).preprocess()




# from lib.configuration import Configuration
from lib.preprocessing.pheme.preprocessing import PreProcessing
from lib.read_datasets.pheme.read_pheme_ds import read_pheme_ds

# Configuration().config()
# ----------------------------PHEME dataset
dataframe = read_pheme_ds()

preprocessing = PreProcessing(df=dataframe)
import lib.constants as constants
import pandas as pd

from lib.read_datasets.pheme.file_dir_handler import FileDirHandler


class ReadPhemeCSVDataset:
    def __init__(self):
        self.df = None

    def read_csv_dataset(self):
        print("Read CSV Dataset ...", end=' => DIRECTORY is : ' + constants.PHEME_CSV_DIR+'\n')
        self.df = FileDirHandler.read_csv_file(path=constants.PHEME_CSV_PATH)

import os
from os import environ as env


class ReadPhemeDataset:
    def __init__(self):
        # self.name = name
        # self.age = age
        print(env['API_KEY'])
        entries = os.listdir(env['PHEME_DATASET_DIR'])
        print(entries)



import os
import json
import pandas as pd


class FileDirHandler:
    @staticmethod
    def read_directories(directory):
        try:
            dirs = os.listdir(directory)
            return dirs
        except:
            return None

    @staticmethod
    def read_json_file(path):
        try:
            with open(path) as jsonFile:
                json_object = json.load(jsonFile)
                jsonFile.close()
                return json_object
        except FileExistsError:
            return None
        except NotADirectoryError:
            return None

    @staticmethod
    def read_csv_file(path):
        return pd.read_csv(path, lineterminator='\n')

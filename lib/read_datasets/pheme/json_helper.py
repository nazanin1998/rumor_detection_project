import json


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

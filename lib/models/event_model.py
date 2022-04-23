class EventModel:
    def __init__(self, path, rumors, non_rumors):
        self.rumors = rumors
        self.non_rumors = non_rumors

    def from_dir(self):
        return
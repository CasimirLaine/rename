import os
import uuid


class NamingStrategy:
    def get_name(self, file):
        pass


class RandomNamingStrategy(NamingStrategy):
    def get_name(self, file):
        filename, file_extension = os.path.splitext(file)
        return str(uuid.uuid4()) + file_extension


class SequentialNamingStrategy(NamingStrategy):

    def __init__(self, min_char_count):
        self.min_char_count = min_char_count
        self.index = 0

    def get_name(self, file):
        filename, file_extension = os.path.splitext(file)
        index = self.index
        self.index += 1
        filename = str(index)
        if len(filename) < self.min_char_count:
            filename = ("0" * (self.min_char_count - len(filename))) + filename
        return filename + file_extension

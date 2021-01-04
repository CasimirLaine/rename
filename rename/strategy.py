import os
import uuid


class RandomNamingStrategy():
    def get_name(self, file):
        filename, file_extension = os.path.splitext(file)
        return str(uuid.uuid4()) + file_extension

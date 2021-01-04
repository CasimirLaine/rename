import os

import rename

CONFIG_FILE = "config.rename"


class Config:
    def __init__(self):
        try:
            with open(get_config_file_path(), "xt"):
                pass
        except FileExistsError:
            pass
        finally:
            with open(get_config_file_path(), "rt") as file:
                self.file_data = file.read()
        self.file_types_regex = filter(None, self.file_data.splitlines())


def get_config_file_path():
    return os.path.join(rename.get_file_context(), CONFIG_FILE)

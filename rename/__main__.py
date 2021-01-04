import glob
import os

import rename
from rename import strategy
from rename.file import config

config = config.Config()
files_to_rename = []
for file_type in config.file_types_regex:
    files_to_rename.extend(glob.glob(os.path.join(rename.get_file_context(), file_type), recursive=False))
naming_strategy = strategy.RandomNamingStrategy()
for file in files_to_rename:
    os.rename(file, os.path.join(rename.get_file_context(), naming_strategy.get_name(file)))

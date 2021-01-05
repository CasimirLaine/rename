import glob
import os
import sys

import rename
from rename import strategy
from rename.file import config

__ARG_RANDOM = "random"
__ARG_SEQUENTIAL = "sequential"
args = sys.argv
if len(args) < 2:
    print("Please provide a strategy!")
    sys.exit()
naming_strategy = None
if args[1] == __ARG_RANDOM:
    naming_strategy = strategy.RandomNamingStrategy()
elif args[1] == __ARG_SEQUENTIAL:
    naming_strategy = strategy.SequentialNamingStrategy(int(args[2]) if len(args) >= 3 else 0)
else:
    print("Unknown argument!")
    sys.exit()
config = config.Config()
files_to_rename = []
for file_type in config.file_types_regex:
    files_to_rename.extend(glob.glob(os.path.join(rename.get_file_context(), file_type), recursive=False))
for file in files_to_rename:
    try:
        os.rename(file, os.path.join(rename.get_file_context(), naming_strategy.get_name(file)))
    except FileExistsError:
        print("File already exists with name that name!")

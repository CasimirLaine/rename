import os
import pathlib
import sys

PROGRAM_NAME = "rename"
PROGRAM_VERSION = "1.0"


def get_file_context():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return str(pathlib.Path(__file__).parent.parent.parent.absolute())

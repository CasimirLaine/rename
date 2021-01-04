import os
import pathlib
import sys


def get_file_context():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return str(pathlib.Path(__file__).parent.parent.parent.absolute())

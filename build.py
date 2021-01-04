import os
import pathlib

import PyInstaller.__main__

__EXECUTABLE_NAME = "rename"
__SPEC_FILE = __EXECUTABLE_NAME + ".spec"
__DIST_PATH = "dist"

PyInstaller.__main__.run([
    "rename/__main__.py",
    "--onefile",
    "--noconsole",
    "--name",
    __EXECUTABLE_NAME,
    "--distpath",
    "." + os.sep + __DIST_PATH,
])
if os.path.exists(__SPEC_FILE):
    os.remove(__SPEC_FILE)
print(os.path.join(str(pathlib.Path(__file__).parent), __DIST_PATH))

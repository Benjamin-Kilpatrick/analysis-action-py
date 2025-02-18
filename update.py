from pathlib import Path
import sys
import os

root_dir = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else  os.getcwd()
print("looking in", root_dir)

files = list(Path(root_dir).glob('**/*.py'))
for path in files:
    print(path)
    # do ur stuff for each file here


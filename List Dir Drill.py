

import os

path = 'C:\\A\\'

dir = os.listdir(path)
print(dir)

os.stat(path)

thisdir = os.getcwd()
# Getting the current work directory (cwd)

mtime = os.path.getmtime(path)


# r=root, d=directories, f = files
for r, d, f in os.walk(thisdir):
    for file in f:
        if ".txt" in file:
            print(os.path.join(r, file), mtime)


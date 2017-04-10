from datetime import datetime
import os
import glob2

directory = os.scandir('.')
now = datetime.now()

for entry in directory:
    if entry.is_dir() & (entry.name == "Sample-Files"):
        dirpath = entry.path


os.chdir(dirpath)
filenames = glob2.glob("*file*")

with open(now.strftime('%Y-%m-%d-%H-%M-%S-%f' + '.txt'), 'a+') as mergedFile:
    for file in filenames:
        with open(file, 'r') as openedFile:
            contents = openedFile.readlines()
            for content in contents:
                mergedFile.write(str(content) +'\n')

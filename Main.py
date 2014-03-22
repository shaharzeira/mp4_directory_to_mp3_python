from findAllMp4Files import findFiles
from sys import argv
from saveToMp3 import save

for fileMp4 in findFiles(argv[1]):
    save(fileMp4)

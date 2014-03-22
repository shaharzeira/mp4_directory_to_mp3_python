from os import listdir
from parser import parse

def findFiles(dirFiles):
    print dirFiles
    a=[]
    for fileMp4 in listdir(dirFiles):
	if fileMp4.endswith(".mp4"):
	    print fileMp4
            a.append(parse(fileMp4, dirFiles))
    return a

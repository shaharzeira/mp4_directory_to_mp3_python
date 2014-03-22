import os

def parse(fileName, path):
    tmpSplit = os.path.splitext(fileName)
    return tmpSplit[0], tmpSplit[1], path

def getName(o):
    return o[0]

def getExt(o):
    return o[1]

def getPath(o):
    return o[2]

def getFull(o):
    return getPath(o)+"/"+getName(o)+getExt(o)

def getDirName(old):
    dirName=old+"_Converted_mp3_files/"
    if not os.path.exists(dirName):
	os.makedirs(dirName)
    return dirName

def getFullFromMp4(mp4):
    return getDirName(mp4[2])+mp4[0]+".mp3"

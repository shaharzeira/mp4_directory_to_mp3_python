from parser import getFull, getFullFromMp4
import os

def save(mp4):
    a=["ffmpeg -i","'"+getFull(mp4)+"'","-q:a 0 -map a", "'"+getFullFromMp4(mp4)+"'"]
    printData(mp4, a)
    os.system(" ".join(a))

def printData(mp4, a):
    print "******************"
    print getFull(mp4)
    print getFullFromMp4(mp4)
    print "******************"
    print " ".join(a)

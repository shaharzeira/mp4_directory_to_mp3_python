#!/usr/bin/python

'''
Copyright (C) 2014 by Shahar Zeira (shahar.zeira@gmail.com)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

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

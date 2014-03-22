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

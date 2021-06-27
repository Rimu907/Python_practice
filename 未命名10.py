# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 12:17:02 2021

@author: 90730
"""

class File :
    pass
class PlainFile(File) :
    def init(self,name) :
        self.name = name
class Directory(File) :
    def init(self,name,contents) :
        self.name = name
        self.contents = contents
class File :
    pass
class PlainFile(File) :
    def __init__(self,name) :
        self.name = name
class Directory(File) :
    def __init__(self,name,contents) :
        self.name = name
        self.contents = contents

fs = Directory("root",
[PlainFile("boot.exe"),
Directory("home",[
Directory("thor",
[PlainFile("hunde.jpg"),
PlainFile("quatsch.txt")]),
Directory("isaac",
[PlainFile("gatos.jpg")])])])

fs.contents[1].contents[0].contents[0].


type(fs.contents[1].contents[0].contents[0].name)

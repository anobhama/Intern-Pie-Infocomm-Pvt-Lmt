# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 00:43:02 2020

@author: Anobhama
"""

from gtts import gTTS
import os

filehandler = open("intro.txt","r")
myText= filehandler.read()
language='en'
output=gTTS(text=myText,lang=language,slow=False)
output.save("introduction.mp3")
os.system("start introduction.mp3")

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 00:10:15 2020

@author: Anobhama
"""

#converting text to audio

from gtts import gTTS
import os

myText="Hi Im Anobhama"
language='en'
output=gTTS(text=myText,lang=language,slow=False)
output.save("intro.mp3")
os.system("start intro.mp3")

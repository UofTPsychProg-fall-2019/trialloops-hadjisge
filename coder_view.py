import numpy as np
import pandas as pd
import os, sys
from psychopy import visual, core, event, gui, logging

win = visual.Window(fullscr=True, allowGUI=False, color='black', unit='height') 

myText = visual.TextStim(win,text='+',pos=(0,0), color = 'white')
myText.draw()
win.flip()

core.wait(1)

myPic = visual.ImageStim(win, image = 'T.png', pos=(0,0))
myPic.draw()
win.flip()

keys = event.waitKeys(keyList=('f','j'))

win.close()
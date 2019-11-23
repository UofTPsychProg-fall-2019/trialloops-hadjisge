import numpy as np
import pandas as pd
import os, sys
from psychopy import visual, core, event, gui, logging

win = visual.Window(fullscr=True, allowGUI=False, color='black', unit='height') 

stim = ['T.png', 'A.png', 'B.png', 'L.png', 'E.png']
np.random.shuffle(stim)
responses = []

for t in range(len(stim)):
    myText = visual.TextStim(win,text='+',pos=(0,0), color = 'white')
    myText.draw()
    win.flip()
    core.wait(1)
    thisStimName = (stim[t])
    thisStim = visual.ImageStim(win, image=thisStimName, pos = (0,0))
    thisStim.draw()
    win.flip()
    keys = event.waitKeys(keyList=('f','j'))
    responses=np.append(responses,keys)
    print(responses)
    df = pd.DataFrame({'responses': responses})
    df.to_csv('output.csv')




core.wait(2)
win.close
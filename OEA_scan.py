#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on May 24, 2021, at 13:52
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'OEA_scan'  # from the Builder filename that created this script
expInfo = {'participant': '', 'run': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\mauspad\\Desktop\\new_OEA_stuff\\pumps_psychopy\\OEA_scan.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "wait"
waitClock = core.Clock()
trigger = keyboard.Keyboard()
text = visual.TextStim(win=win, name='text',
    text='wait for 5 trigger from scanner',
    font='Arial',
    pos=(0, 0), height=30, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "visualcue"
visualcueClock = core.Clock()
visual_cue = visual.ImageStim(
    win=win,
    name='visual_cue', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
#import stuff
import serial
import time

#open serial port
ser = serial.Serial(port='COM4', baudrate=19200, bytesize=8)

#pump order:
#0 - tless
#1 - choc milk
#2 - straw milk
#3 - rinse

# Initialize components for Routine "taste_delivery"
taste_deliveryClock = core.Clock()
taste_delivery_fixation = visual.ShapeStim(
    win=win, name='taste_delivery_fixation', vertices='cross',
    size=(100,100),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "tasteITI"
tasteITIClock = core.Clock()
taste_delivery_ITI = visual.ShapeStim(
    win=win, name='taste_delivery_ITI', vertices='cross',
    size=100,
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "rinse_delivery"
rinse_deliveryClock = core.Clock()
rinse_delivery_fixation = visual.ShapeStim(
    win=win, name='rinse_delivery_fixation', vertices='cross',
    size=(100,100),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "rinseITI"
rinseITIClock = core.Clock()
rinse_ITI_fixation = visual.ShapeStim(
    win=win, name='rinse_ITI_fixation', vertices='cross',
    size=100,
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "end"
endClock = core.Clock()
end_task_trigger = keyboard.Keyboard()
end_task = visual.TextStim(win=win, name='end_task',
    text='You have completed this scan :)',
    font='Arial',
    pos=(0, 0), height=30, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "wait"-------
# update component parameters for each repeat
trigger.keys = []
trigger.rt = []
# keep track of which components have finished
waitComponents = [trigger, text]
for thisComponent in waitComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
waitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "wait"-------
while continueRoutine:
    # get current time
    t = waitClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=waitClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *trigger* updates
    waitOnFlip = False
    if trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trigger.frameNStart = frameN  # exact frame index
        trigger.tStart = t  # local t and not account for scr refresh
        trigger.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trigger, 'tStartRefresh')  # time at next scr refresh
        trigger.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(trigger.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(trigger.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if trigger.status == STARTED and not waitOnFlip:
        theseKeys = trigger.getKeys(keyList=['5'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            if trigger.keys == []:  # then this was the first keypress
                trigger.keys = theseKeys.name  # just the first key pressed
                trigger.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in waitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wait"-------
for thisComponent in waitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if trigger.keys in ['', [], None]:  # No response was made
    trigger.keys = None
thisExp.addData('trigger.keys',trigger.keys)
if trigger.keys != None:  # we had a response
    thisExp.addData('trigger.rt', trigger.rt)
thisExp.addData('trigger.started', trigger.tStartRefresh)
thisExp.addData('trigger.stopped', trigger.tStopRefresh)
thisExp.nextEntry()
# the Routine "wait" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('eventtype.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "visualcue"-------
    # update component parameters for each repeat
    visual_cue.setImage(imgpath)
    # keep track of which components have finished
    visualcueComponents = [visual_cue]
    for thisComponent in visualcueComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    visualcueClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "visualcue"-------
    while continueRoutine:
        # get current time
        t = visualcueClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=visualcueClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *visual_cue* updates
        if visual_cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            visual_cue.frameNStart = frameN  # exact frame index
            visual_cue.tStart = t  # local t and not account for scr refresh
            visual_cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(visual_cue, 'tStartRefresh')  # time at next scr refresh
            visual_cue.setAutoDraw(True)
        if visual_cue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > visual_cue.tStartRefresh + cue_ITI-frameTolerance:
                # keep track of stop time/frame for later
                visual_cue.tStop = t  # not accounting for scr refresh
                visual_cue.frameNStop = frameN  # exact frame index
                win.timeOnFlip(visual_cue, 'tStopRefresh')  # time at next scr refresh
                visual_cue.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in visualcueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "visualcue"-------
    for thisComponent in visualcueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('visual_cue.started', visual_cue.tStartRefresh)
    trials.addData('visual_cue.stopped', visual_cue.tStopRefresh)
    # the Routine "visualcue" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "taste_delivery"-------
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    if eventtype == 'tless':
        ser.write(("0run\r").encode())
    elif eventtype == 'milkchoc':
        ser.write(("1run\r").encode())
    elif eventtype == 'milkstraw':
        ser.write(("2run\r").encode())
    # keep track of which components have finished
    taste_deliveryComponents = [taste_delivery_fixation]
    for thisComponent in taste_deliveryComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    taste_deliveryClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "taste_delivery"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = taste_deliveryClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=taste_deliveryClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *taste_delivery_fixation* updates
        if taste_delivery_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            taste_delivery_fixation.frameNStart = frameN  # exact frame index
            taste_delivery_fixation.tStart = t  # local t and not account for scr refresh
            taste_delivery_fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(taste_delivery_fixation, 'tStartRefresh')  # time at next scr refresh
            taste_delivery_fixation.setAutoDraw(True)
        if taste_delivery_fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > taste_delivery_fixation.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                taste_delivery_fixation.tStop = t  # not accounting for scr refresh
                taste_delivery_fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(taste_delivery_fixation, 'tStopRefresh')  # time at next scr refresh
                taste_delivery_fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in taste_deliveryComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "taste_delivery"-------
    for thisComponent in taste_deliveryComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('taste_delivery_fixation.started', taste_delivery_fixation.tStartRefresh)
    trials.addData('taste_delivery_fixation.stopped', taste_delivery_fixation.tStopRefresh)
    
    # ------Prepare to start Routine "tasteITI"-------
    # update component parameters for each repeat
    # keep track of which components have finished
    tasteITIComponents = [taste_delivery_ITI]
    for thisComponent in tasteITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    tasteITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "tasteITI"-------
    while continueRoutine:
        # get current time
        t = tasteITIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=tasteITIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *taste_delivery_ITI* updates
        if taste_delivery_ITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            taste_delivery_ITI.frameNStart = frameN  # exact frame index
            taste_delivery_ITI.tStart = t  # local t and not account for scr refresh
            taste_delivery_ITI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(taste_delivery_ITI, 'tStartRefresh')  # time at next scr refresh
            taste_delivery_ITI.setAutoDraw(True)
        if taste_delivery_ITI.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > taste_delivery_ITI.tStartRefresh + taste_ITI-frameTolerance:
                # keep track of stop time/frame for later
                taste_delivery_ITI.tStop = t  # not accounting for scr refresh
                taste_delivery_ITI.frameNStop = frameN  # exact frame index
                win.timeOnFlip(taste_delivery_ITI, 'tStopRefresh')  # time at next scr refresh
                taste_delivery_ITI.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in tasteITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "tasteITI"-------
    for thisComponent in tasteITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('taste_delivery_ITI.started', taste_delivery_ITI.tStartRefresh)
    trials.addData('taste_delivery_ITI.stopped', taste_delivery_ITI.tStopRefresh)
    # the Routine "tasteITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "rinse_delivery"-------
    # update component parameters for each repeat
    if rinse_delivery == 1.5:
        ser.write(("3run\r").encode())
    else:
        pass
    # keep track of which components have finished
    rinse_deliveryComponents = [rinse_delivery_fixation]
    for thisComponent in rinse_deliveryComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rinse_deliveryClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "rinse_delivery"-------
    while continueRoutine:
        # get current time
        t = rinse_deliveryClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rinse_deliveryClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rinse_delivery_fixation* updates
        if rinse_delivery_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rinse_delivery_fixation.frameNStart = frameN  # exact frame index
            rinse_delivery_fixation.tStart = t  # local t and not account for scr refresh
            rinse_delivery_fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rinse_delivery_fixation, 'tStartRefresh')  # time at next scr refresh
            rinse_delivery_fixation.setAutoDraw(True)
        if rinse_delivery_fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rinse_delivery_fixation.tStartRefresh + rinse_delivery-frameTolerance:
                # keep track of stop time/frame for later
                rinse_delivery_fixation.tStop = t  # not accounting for scr refresh
                rinse_delivery_fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rinse_delivery_fixation, 'tStopRefresh')  # time at next scr refresh
                rinse_delivery_fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rinse_deliveryComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rinse_delivery"-------
    for thisComponent in rinse_deliveryComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('rinse_delivery_fixation.started', rinse_delivery_fixation.tStartRefresh)
    trials.addData('rinse_delivery_fixation.stopped', rinse_delivery_fixation.tStopRefresh)
    # the Routine "rinse_delivery" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "rinseITI"-------
    # update component parameters for each repeat
    # keep track of which components have finished
    rinseITIComponents = [rinse_ITI_fixation]
    for thisComponent in rinseITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rinseITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "rinseITI"-------
    while continueRoutine:
        # get current time
        t = rinseITIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rinseITIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rinse_ITI_fixation* updates
        if rinse_ITI_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rinse_ITI_fixation.frameNStart = frameN  # exact frame index
            rinse_ITI_fixation.tStart = t  # local t and not account for scr refresh
            rinse_ITI_fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rinse_ITI_fixation, 'tStartRefresh')  # time at next scr refresh
            rinse_ITI_fixation.setAutoDraw(True)
        if rinse_ITI_fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rinse_ITI_fixation.tStartRefresh + rinse_ITI-frameTolerance:
                # keep track of stop time/frame for later
                rinse_ITI_fixation.tStop = t  # not accounting for scr refresh
                rinse_ITI_fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rinse_ITI_fixation, 'tStopRefresh')  # time at next scr refresh
                rinse_ITI_fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rinseITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rinseITI"-------
    for thisComponent in rinseITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('rinse_ITI_fixation.started', rinse_ITI_fixation.tStartRefresh)
    trials.addData('rinse_ITI_fixation.stopped', rinse_ITI_fixation.tStopRefresh)
    # the Routine "rinseITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "end"-------
# update component parameters for each repeat
end_task_trigger.keys = []
end_task_trigger.rt = []
# keep track of which components have finished
endComponents = [end_task_trigger, end_task]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_task_trigger* updates
    waitOnFlip = False
    if end_task_trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_task_trigger.frameNStart = frameN  # exact frame index
        end_task_trigger.tStart = t  # local t and not account for scr refresh
        end_task_trigger.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_task_trigger, 'tStartRefresh')  # time at next scr refresh
        end_task_trigger.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(end_task_trigger.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_task_trigger.status == STARTED and not waitOnFlip:
        theseKeys = end_task_trigger.getKeys(keyList=['return'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *end_task* updates
    if end_task.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_task.frameNStart = frameN  # exact frame index
        end_task.tStart = t  # local t and not account for scr refresh
        end_task.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_task, 'tStartRefresh')  # time at next scr refresh
        end_task.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

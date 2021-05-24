# -*- coding: utf-8 -*-
"""
THIS IS STILL BAD CODE.
BUT IT IS LESS BAD THAN BEFORE.

feb 26 2021

@author: mauspad
"""
#import packages
import pandas as pd
import numpy
import ast

# turn csv into dataframe
df = pd.read_csv("data/pilot.csv") #change!

# set up some variables
trialno = list(range(0,60)) # trial number

# calculate and list task onsets relative to scanner start
real_start = df.at[0, "trigger.rt"]
cue_onset_raw = df["visual_cue.started"].tolist()
taste_onset_raw = df["taste_delivery_ITI.started"].tolist()
del cue_onset_raw[0]
del taste_onset_raw[0]
cue_onset = numpy.array(cue_onset_raw)
taste_onset = numpy.array(taste_onset_raw)
cue_onset = (cue_onset - real_start).tolist()
taste_onset = (taste_onset - real_start).tolist()
eventtype = df["eventtype"].tolist()
del eventtype[0]

# make some empty lists to sort into
milkonset = []
tlessonset = []
rinseonset = []

# loop!
for i in trialno:
    if eventtype[i] == "tless":
        tlessonset.append(taste_onset[i])
    elif eventtype[i] == "milkstraw" or eventtype[i] == "milkchoc":
        milkonset.append(taste_onset[i])

print("Cue: " + str(cue_onset) + "\n")
print("Milk: " + str(milkonset) + "\n")
print("Tasteless: " + str(tlessonset) + "\n")

rinseonset = [x + 3.5 for x in milkonset]

print("Rinse: " + str(rinseonset) + "\n")

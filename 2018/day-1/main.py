# get values for freq changes
import json
from pprint import pprint

with open('C:/Users/chadsten/source/repos/AoC18/day-1/data.json') as data_file: 
    data = json.load(data_file)

## determine the end frequency after applying all modifiers in the

freq = 0 # base frequency

for f in data['freq']:
    freq = freq + int(f['value']) # simply loop to add all values

print(str(freq) + " is the end frequency.") # output final frequency

## determine first frequency that has happened twice

occ = {} # initiate occurence object
freq = 0 # base frequency
occ[freq] = 1 # set starting frequency to have occured once
hit = None # we have not had a hit (frequency occuring twice)
present = dict() # our output, it's a gift!

def buildData(occ, freq):
    val = dict() # define object for return

    for f in data['freq']:
        freq = freq + int(f['value']) # calculate new frequency

        try:
            occ[freq]
        except KeyError:
            occ[freq] = 0 # if this doesn't exist, it's the frequency's first occurence
            
        occ[freq] = occ[freq] + 1 # increment the occurence counter

        if occ[freq] > 1:
            val['number'] = occ[freq]
            break # store which frequency has occured twice and leave the loop
        else:
            val['number'] = 'fail' # default value for checking later

    val['freq'] = freq # set new frequency
    return val   

while hit is None: # if no 2nd occurence has been detected yet
    present = buildData(occ, freq) # attempt to find 2nd occurence, carrying over data from previous passes
    freq = present['freq'] # set new frequency for next pass

    if present['number'] != 'fail': # if it's not our default fail, we have a match
        hit = 1

print(str(present['freq']) + " is the first frequency to be repeated.") # output first repeated frequency

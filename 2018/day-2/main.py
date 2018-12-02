# load data
import json
from pprint import pprint

with open('C:/Users/chadsten/source/repos/advent-of-code/2018/day-2/data.json') as data_file: 
	data = json.load(data_file)

# count both of these for our final checksum calculation
doubles = 0
triples = 0

for s in data['strings']:
	# create array of sorted by count letters, so we can do array position match/trim
	s = list(s['value'])
	s.sort()
	s = sorted(s, key=s.count, reverse=True) # second sort to put matching characters first

	# these are just used for short circuiting once one has been found
	has_double = False
	has_triple = False

	# start checking the first 2-3 characters for matches in our sorted data
	while len(s) > 1 and (has_double == False or has_triple == False):

		# find triple first
		if len(s) > 2:
			if s[0] == s[2] and s[0] == s[1] and has_triple == False: # safety check middle val in case sorting fails
				triples = triples + 1
				has_triple = True
				s = s[3:] # remove triple
				continue
	
		# find double
		if s[0] == s[1] and has_double == False:
			doubles = doubles + 1
			has_double = True
			s = s[2:] # remove double
			continue

		# drop letter without match
		else:
			s = s[1:]

print("There are " + str(doubles) + " doubles and " + str(triples) + " triples, for a hash of " + str(doubles * triples) + ".")

index = 0
for s in data['strings']:
	del data['strings'][index] # remove current value, it either matches or needs gone
	index = index + 1 # keep track of index here, as it doesn't reset during the loop for above del
	search = s
	s = list(s['value']) # break into letters so postion comparison is just index alignment

	for h in data['strings']:
		fails = 0
		matches = 0
		match = ''
		i = 0
		haystack = h
		h = list(h['value']) # create second list of letters for index alignment checking

		while i < len(s): # loop check each letter

			if (h[i] != s[i]):
				fails = fails + 1
			else:
				matches = matches + 1
				match = match + h[i]

			i = i+1

		if (fails < 2):
			print(str(search) + " + " + str(haystack))
			print(match)

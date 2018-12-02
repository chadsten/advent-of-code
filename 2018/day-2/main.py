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

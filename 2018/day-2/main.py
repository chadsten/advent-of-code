# get values for freq changes
import json
from pprint import pprint

with open('C:/Users/chadsten/source/repos/advent-of-code/2018/day-2/data.json') as data_file: 
	data = json.load(data_file)

print(data)

doubles = 0
triples = 0

for s in data['strings']:
	s = list(s['value'])
	s.sort()
	has_double = False
	has_triple = False

	while len(s) > 1 and (has_double == False or has_triple == False):

		# find triples first
		if len(s) > 2:
			if s[0] == s[2] and has_triple == False:
				triples = triples + 1
				has_triple = True
				s = s[3:]
				continue
	
		# find doubles
		if s[0] == s[1] and has_double == False:
			doubles = doubles + 1
			has_double = True
			s = s[2:]
			continue
		else:
			s = s[1:]

print("There are " + str(doubles) + " doubles and " + str(triples) + " triples, for a hash of " + str(doubles*triples) + ".")



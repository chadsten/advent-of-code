# load data
import json
import re
from pprint import pprint

with open('C:/Users/chadsten/source/repos/advent-of-code/2018/day-3/data.json') as data_file: 
	data = json.load(data_file)

def mapInput(input):
	mapped = dict()

	input = input.split(' @ ')
	mapped['id'] = input[0]

	input = input[1].split(',')
	mapped['left'] = input[0]

	input = input[1].split(': ')
	mapped['top'] = input[0]

	input = input[1].split('x')
	mapped['width'] = input[0]
	mapped['height'] = input[1]

	return mapped

rows = dict()

for pattern in data['patterns']:
	pattern = pattern['value']
	pattern = mapInput(pattern)
	i = 0
	sr = int(pattern['top']) + 1
	sc = int(pattern['left']) + 1

	while i < int(pattern['width']):
		j = 0
		while j < int(pattern['height']):
			try:
				rows[str(sr + i) + "-" + str(sc + j)]

			except KeyError:
				rows[str(sr + i) + "-" + str(sc + j)] = 0

			rows[str(sr + i) + "-" + str(sc + j)] += 1

			j += 1
		i += 1


counter = 0
for key, value in rows.items():
	if value > 1:
		counter += 1

print(counter)

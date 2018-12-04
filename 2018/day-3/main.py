# load data
import json
from pprint import pprint

with open('C:/Users/chadsten/source/repos/advent-of-code/2018/day-3/data.json') as data_file: 
	data = json.load(data_file)

# split our data up into parts
# ex: #1 @ 1,3: 4x4
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
gift = ''

for pattern in data['patterns']:
	pattern = mapInput(pattern['value']) # break input into parts to map
	sc = int(pattern['top']) # starting row
	sr = int(pattern['left']) # starting column

	i = 0
	while i < int(pattern['width']): # foreach 'row'
		j = 0
		while j < int(pattern['height']): # foreach 'column'
			try:
				rows[str(sr + i) + "-" + str(sc + j)] # check if this has been hit yet

			except KeyError:
				rows[str(sr + i) + "-" + str(sc + j)] = 0

			rows[str(sr + i) + "-" + str(sc + j)] += 1
			j += 1
		i += 1

for pattern in data['patterns']:
	pattern = mapInput(pattern['value']) # break input into parts to map
	sc = int(pattern['top']) # starting row
	sr = int(pattern['left']) # starting column
	cf = 0
	i = 0
	while i < int(pattern['width']): # foreach 'row'
		j = 0
		while j < int(pattern['height']): # foreach 'column'
			if (rows[str(sr + i) + "-" + str(sc + j)] > 1):
				cf += 1
			j += 1
		i += 1
	if (cf < 1):
		print(pattern['id']) # part two, before part one in output only
		break

for pattern in data['patterns']:
	pattern = mapInput(pattern['value']) # break input into parts to map
	sc = int(pattern['top']) # starting row
	sr = int(pattern['left']) # starting column
	cf = 0
	i = 0
	while i < int(pattern['width']): # foreach 'row'
		j = 0
		while j < int(pattern['height']): # foreach 'column'
			if (rows[str(sr + i) + "-" + str(sc + j)] > 1):
				cf += 1
			j += 1
		i += 1
	if (cf < 1):
		print(pattern['id']) # part two, before part one in output only
		break

# print part 1
counter = 0
for key, value in rows.items():
	if value > 1:
		counter += 1

print(counter)

# load data
import json
from pprint import pprint

with open('C:/Users/chadsten/source/repos/advent-of-code/2018/day-3/test.json') as data_file: 
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

	i = 0
	while i < int(pattern['width']): # foreach 'row'
		j = 0
		cf = 0
		while j < int(pattern['height']): # foreach 'column'
			if (rows[str(sr + i) + "-" + str(sc + j)] != 1):
				break
			j += 1
		else:
			print(pattern['id'])
		break
		i += 1

counter = 0
for key, value in rows.items():
	if value > 1:
		counter += 1

print(counter)

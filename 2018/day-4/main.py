from datetime import datetime
import time

# load data
with open('C:/Users/chadsten/source/repos/advent-of-code/2018/day-4/data.txt') as data_file: 
	data = data_file.read().splitlines()

data.sort() # dict sorting in python is abysmal apparently, so fuck it

split_data = dict()

# not having real sorting is depending on some very fragile data
for line in data:
	t = line.split('] ')
	split_data[t[0][1:]] = t[1]
	

fmt = '%Y-%m-%d %H:%M'
guards = dict()
guard = 0

for data in split_data:
	p = split_data[data].split(' ')

	if (p[1] == "asleep"):
		sleep = datetime.strptime(data, fmt)
	elif (p[1] == 'up'):
		wake = datetime.strptime(data, fmt)
		minutes_diff = (wake - sleep).total_seconds() / 60.0
		try:
			guards[guard] # check if this has been hit yet

		except KeyError:
			guards[guard] = 0

		guards[guard] += minutes_diff
	else:
		guard = p[1][1:]


h = 0
for guard in guards:
	if (guards[guard] > h):
		h = guards[guard]
		g = guard
print(g, h)
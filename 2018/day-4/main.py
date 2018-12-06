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
minutes = dict()
guard = 0

for data in split_data:
	p = split_data[data].split(' ')

	if (p[1] == "asleep"):
		sleep = datetime.strptime(data, fmt)
	elif (p[1] == 'up'):
		wake = datetime.strptime(data, fmt)
		minutes_diff = (wake - sleep).total_seconds() / 60.0

		sm = str(sleep)[-5:]
		sm = int(sm[:2])

		wm = str(wake)[-5:]
		wm = int(wm[:2])
		
		i = sm
		j = wm

		# set a minute map to show the frequency of minutes slept by guard
		while i < j:
			try:
				minutes[guard][i] # check if this has been hit yet

			except KeyError:
				minutes[guard][i] = 0

			minutes[guard][i] += 1
			i += 1

		# set the time the guard slept for total
		try:
			guards[guard] # check if this has been hit yet

		except KeyError:
			guards[guard] = 0

		guards[guard] += minutes_diff
	else: # if it's not wake or sleep, it's guard change
		guard = p[1][1:]
		try:
			minutes[guard] # check if this has been hit yet

		except KeyError:
			minutes[guard] = dict()

h = 0
for guard in guards:
	if (guards[guard] > h):
		h = guards[guard]
		g = guard
print(g, h)
print(minutes)

minutes[g]

for min in minutes[g]:
	print(min, minutes[g][min])

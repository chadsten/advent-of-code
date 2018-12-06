# load data
import re
with open('C:/Users/chadsten/source/repos/advent-of-code/2018/day-5/data.txt') as data_file: 
	data = data_file.read().splitlines()

alphabet = list()
alphabet = ("Aa","Bb","Cc","Dd","Ee","Ff","Gg","Hh","Ii","Jj","Kk","Ll","Mm","Nn","Oo","Pp","Qq","Rr","Ss","Tt","Uu","Vv","Ww","Xx","Yy","Zz")  

print(data[0])
test = data[0]

def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str

max = 9900 # from day 1
i = 0
while i < 26:
	test = data[0]
	test = re.sub(alphabet[i][1:], "", test)
	test = re.sub(reverse(alphabet[i])[1:], "", test)

	# extract and run for day 1
	done = False
	while done == False:
		before = len(test)
		for letter in alphabet:
			test = re.sub(letter, "", test)
			test = re.sub(reverse(letter), "", test)
		after = len(test)
		if (after == before):
			done = True
	# end day 1 standalone
	i += 1

	if (len(test) < max):
		max = len(test)

print(max)
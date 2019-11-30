import numpy as np
import itertools
# part 1
i = 0
f = open('input.txt', 'r')
for txt in f:
	lines = np.array([int(i) for i in txt.split(',')])
	lines[1]=12
	lines[2]=2
	while lines[i] !=  99:
		if lines[i] == 1:
			lines[lines[i+3]] = lines[lines[i+1]]+lines[lines[i+2]]
		elif lines[i] == 2:
			lines[lines[i+3]] = lines[lines[i+1]]*lines[lines[i+2]]
		else:
			raise ValueError(f'uh oh {lines[i]}')
		i+=4
print(lines[0])

# part 2
f = open('input.txt', 'r')
noun = -1
verb = -1
for txt in f:
	for n,v in itertools.product(range(100),range(100)):
		lines = np.array([int(i) for i in txt.split(',')])
		i = 0
		lines[1]=n
		lines[2]=v
		while lines[i] !=  99:
			if lines[i] == 1:
				lines[lines[i+3]] = lines[lines[i+1]]+lines[lines[i+2]]
			elif lines[i] == 2:
				lines[lines[i+3]] = lines[lines[i+1]]*lines[lines[i+2]]
			else:
				raise ValueError(f'uh oh {lines[i]}')
			i+=4
		if lines[0] == 19690720:
			noun = n
			verb = v
print(100*noun + verb)


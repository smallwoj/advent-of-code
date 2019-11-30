X = {'L':-1,'R':1,'U':0,'D':0}
Y = {'L':0,'R':0,'U':1,'D':-1}
def allPoints(A):
	ans = {}
	x = 0
	y = 0
	len = 0
	for dirval in A:
		dir = dirval[0]
		val = int(dirval[1:])
		for _ in range(val):
			x+=X[dir]
			y+=Y[dir]
			len += 1
			if (x,y) not in ans:
				ans[(x,y)] = len

	return ans
	
f = open('input.txt')
line1 = f.readline()
line2 = f.readline()
path1 = allPoints(line1.split(','))
path2 = allPoints(line2.split(','))
crossings = set(path1.keys())&set(path2.keys())
print(int(min([abs(p[0])+abs(p[1]) for p in crossings])))
print(int(min([path1[p]+path2[p] for p in crossings])))


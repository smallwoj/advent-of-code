#part 1
f = open('input.txt', 'r')
sum = 0
for line in f:
	sum+=int(line)//3-2

print(sum)

#part 2
f = open('input.txt', 'r')
sum = 0
for line in f:
	curr = int(line)//3-2
	
	while curr > 0:
		sum+=curr
		curr = curr//3-2
print(sum)


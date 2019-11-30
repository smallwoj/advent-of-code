def check(n):
    digs = [int(c) for c in str(n)]
    i = 0
    dd = False
    inc = True
    slots=dict([(i,0) for i in range(10)])
    while i < len(digs)-1:
        # if digs[i] == digs[i+1]: # part 1
        #     dd = True
        if digs[i+1] < digs[i]:
            inc = False
        slots[digs[i]]+=1
        i+=1
    slots[digs[-1]]+=1
    # part 2
    for i in range(10):
        if slots[i] == 2:
            dd = True
    return dd and inc

f = open('input.txt')
bottomtext,toptext = f.readline().split('-')
possible = []
for num in range(int(bottomtext), int(toptext)+1):
    if check(num):
        possible.append(num)

print(len(possible))

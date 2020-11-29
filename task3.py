d = dict()
f = open('font3.txt', 'r')
for line in f:
    k = line.split(',')[1].strip()
    v = line.split(',')[0].strip()
    d[k] = v
print(d)
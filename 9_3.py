filename = 'mbox-short.txt'
filehand = open(filename)
counts = dict()
for line in filehand:
    words = line.split()
    if not len(words) == 0 and words[0] == 'From' : 
        if words[1] not in counts:
            counts[words[1]] = 1
        else:
            counts[words[1]] += 1
print(counts)
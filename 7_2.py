file1 = input('File name: ')
fhand = open(file1)
total = 0
count = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        line2 = float(line[20:])
        total = total + line2
        count = count + 1
print("Average spam confidence: ", total/count)
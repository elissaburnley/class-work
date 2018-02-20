file=open("Margaritaville.txt")

for line in file:
    line2 = line.rstrip()
    print(line2.upper())
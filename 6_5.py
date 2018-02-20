str = 'X-DSPAM-Confidence: 0.8475'
start = str.find(":")
target =str[start+1:]
num = float(target)
print(num)
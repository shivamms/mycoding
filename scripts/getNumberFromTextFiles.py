
import glob
import re
lines = []
textFiles = glob.glob('*.txt')
for tf in textFiles:
    with open(tf) as file:
        lines.append(file.readlines())
lines = sum(lines,[])
matches = [re.compile("[0-9]+\.*[0-9]*").search(line) for line in lines]
numbers = [float(match.group(0)) for match in matches if match]
mean = sum(numbers)/len(numbers)
with open('mean.txt','w') as file:
    file.write(str(mean))

file = open("numbers.txt",'r')
sum=0
for line in file:
    value = int(line)
    sum += value

file.close()
print(sum)
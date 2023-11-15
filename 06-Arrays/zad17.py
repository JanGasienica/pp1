array = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(array[0])):
    array[i][i]=1
    
for rows in array:
    print(rows)
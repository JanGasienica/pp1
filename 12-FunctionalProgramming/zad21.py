arr=[]
for i in range(1,21):
    arr.append(i)

e = list(filter(lambda x: x%2==0 or x%3==0,arr))

print(e)
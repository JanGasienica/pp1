arr=[]
for i in range(1,21):
    arr.append(i)

third_power = list(map(lambda x:x**3,arr))

print(third_power)
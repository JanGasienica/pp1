#name = "Anna May"
#university = "Krakow University of Economics"
#field = "Applied Informatics"
arr = ["Jan", "UEK", "AI"]

file = open("student.txt",'w')
for value in arr:
    file.write(value+"\n")
file.close()
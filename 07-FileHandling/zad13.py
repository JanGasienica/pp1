movie_titles = ["zielona mila", "skazani na shawshang", "forst gump","leon zawodowiec","requiem dla snu"]

file = open("movie_titles.txt",'w')
for value in movie_titles:
    file.write(value+"\n")
file.close()


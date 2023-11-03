def acronym(name):
    words = name.split()  
    acronym = "".join(word[0].upper() for word in words) 
    return acronym
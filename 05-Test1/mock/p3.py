def f(text):
    words = text.split()  
    acronym = [word[0] for word in words if word]  
    return "".join(acronym)  

if __name__ == "__main__":
    print(f("Internet of Things")) 
    print(f("For Your Information"))
    print(f("Python"))
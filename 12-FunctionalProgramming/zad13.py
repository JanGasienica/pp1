def size_bottle(bottle_size):
    def check(ml):
        if bottle_size == 500:
            if ml < bottle_size + 2/100*bottle_size and ml > bottle_size-2/100*bottle_size:
                return True
            return False
        if bottle_size == 1000:
            if ml < bottle_size + 3/100*bottle_size and ml > bottle_size-3/100*bottle_size:
                return True
            return False
        if bottle_size == 1500:
            if ml < bottle_size + 5/100*bottle_size and ml > bottle_size-5/100*bottle_size:
                return True
            return False
    return check

result = size_bottle(1000)
e = 1032
print(f"{e}: {result(e)}")
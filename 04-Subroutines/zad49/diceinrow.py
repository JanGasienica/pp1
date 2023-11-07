def dice_in_row(expression):
    a=[]
    row=0
    highest_row = 0
    rolled_most_times = 0
    for i in expression:
        a.append(i)
        if int(a(i)) == int(a(i-1)):
            row += row
        if row > highest_row:
            highest_row = row
            rolled_most_times = int(a(i))
    return rolled_most_times


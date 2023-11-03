def sum_repeated_digits(number):
    number_str = str(number)  
    digit_count = {}  

    for digit in number_str:
        if digit.isdigit():
            if digit in digit_count:
                digit_count[digit] += 1
            else:
                digit_count[digit] = 1

    total = 0
    for digit, count in digit_count.items():
        if count > 1:
            total += int(digit) * count

    return total



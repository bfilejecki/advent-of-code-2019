def convert_to_digits(input):
    digits = []
    while input:
        digit = input % 10
        input //= 10
        digits.append(digit)
    digits.reverse()
    return digits

def have_decreasing_digits(digits):
    previous = None
    for digit in digits:
        if previous is not None and digit < previous:
            return False
        previous = digit
    return True

def have_adjacent_pair(digits):
    previous = None
    have_pair = False
    for digit in digits:
        if previous is not None and previous == digit:
            have_pair = True
        previous = digit

    return have_pair

def count_fitting_numbers_in_range(start, end):
    count = 0
    for number in range(start, end + 1):
        digits = convert_to_digits(number)
        if have_decreasing_digits(digits) and have_adjacent_pair(digits):
            count += 1
    return count

print(count_fitting_numbers_in_range(256310, 732736))
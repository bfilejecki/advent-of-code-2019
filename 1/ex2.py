def read_input():
    with open('input.txt') as input_file:
        return [int(x) for x in input_file]


def calculate_fuel(mass):
    return int(mass/3) - 2


def calculate_total_fuel(mass):
    tmp_value = mass
    tmp_result = 0
    while True:
        tmp_value = calculate_fuel(tmp_value)
        if tmp_value <= 0:
            break
        tmp_result = tmp_result + tmp_value
    return tmp_result

result = sum(calculate_total_fuel(x) for x in read_input())
print(result)
def read_input():
    with open('input.txt') as input_file:
        return [int(x) for x in input_file]
result = sum(int(x/3) - 2 for x in read_input())
print(result)
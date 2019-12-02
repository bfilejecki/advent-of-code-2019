import sys

HALT_CODE = 99
ADD_CODE = 1
MULTIPLY_CODE = 2

def read_input():
    with open('input.txt') as input_file:
        return [int(x) for x in input_file.readline().split(',')]


def run_code(noun, verb, init_code):
    input_code = read_input()
    input_code_size = len(input_code)
    idx = 0
    tmp_result = None

    input_code[1] = noun
    input_code[2] = verb

    while idx < input_code_size:
        op_code = input_code[idx]
        if op_code == HALT_CODE:
            break

        operand_one_idx = input_code[idx+1]
        operand_two_idx = input_code[idx+2]
        result_idx = input_code[idx+3]

        if operand_one_idx > input_code_size or operand_two_idx > input_code_size or result_idx > input_code_size:
            sys.exit(1)

        if ADD_CODE == op_code:
            tmp_result = input_code[operand_one_idx] + input_code[operand_two_idx]
        elif MULTIPLY_CODE == op_code:
            tmp_result = input_code[operand_one_idx] * input_code[operand_two_idx]
        else:
            sys.exit(1)

        input_code[result_idx] = tmp_result
        idx = idx + 4

    return input_code[0]

def main():
    input = read_input()
    for x in range(99):
        for y in range(99):
            result = run_code(x, y, input.copy)
            if result == 19690720:
                print("noun: {0}, verb: {1} = {2}".format(x, y, result))
                print("You lucky number is: {}".format((100*x)+y))
                sys.exit(0)
    print("Shit it didn't go as intended ;/")     

main()
    
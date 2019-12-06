import sys


def read_input():
    tmp_val = []
    with open('input.txt') as input_file:
        for line in input_file.readlines(): 
            tmp_val.append([(x[:1], int(x[1:])) for x in line.split(',')])
    return tmp_val


def convert_moves_to_list_of_points():
    wires = []
    moves = read_input()
    
    for move_set in moves:
        x = 0
        y = 0
        tmp_counter = 0
        wire = []
        for move in move_set:
            tmp_counter = move[1]
            if "U" == move[0]:
                for _ in range(tmp_counter):
                    y += 1
                    key = (x, y)
                    wire.append(key)
            elif "D" == move[0]:
                for _ in range(tmp_counter):
                    y -= 1
                    key = (x, y)
                    wire.append(key)
            elif "R" == move[0]:
                for _ in range(tmp_counter):
                    x += 1
                    key = (x, y)
                    wire.append(key)
            elif "L" == move[0]:
                for _ in range(tmp_counter):
                    x -= 1
                    key = (x, y)
                    wire.append(key)
        wires.append(wire)
    return wires


wires = convert_moves_to_list_of_points()
crossings_points = set(wires[0][1:]) & set(wires[1][1:])

print("number of crossing points: {}".format(len(crossings_points)))
print(2 + min(sum(wire.index(intersect) for wire in wires) for intersect in crossings_points))

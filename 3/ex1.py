import sys


def read_input():
    tmp_val = []
    with open('input.txt') as input_file:
        for line in input_file.readlines(): 
            tmp_val.append([(x[:1], int(x[1:])) for x in line.split(',')])
    return tmp_val


def convert_moves_to_points():
    points = {}
    moves = read_input()
    
    for move_set in moves:
        x = 0
        y = 0
        tmp_counter = 0
        for move in move_set:
            tmp_counter = move[1]
            if "U" == move[0]:
                for i in range(y, y + tmp_counter):
                    key = (x, i)
                    if key in points:
                        points[key] = points[key] + 1
                    else:
                        points[key] = 1
                y = y + tmp_counter
            elif "D" == move[0]:
                for i in range(y, y - tmp_counter, -1):
                    key = (x, i)
                    if key in points:
                        points[key] = points[key] + 1
                    else:
                        points[key] = 1
                y = y - tmp_counter
            elif "R" == move[0]:
                for i in range(x, x + tmp_counter):
                    key = (i, y)
                    if key in points:
                        points[key] = points[key] + 1
                    else:
                        points[key] = 1
                x = x + tmp_counter
            elif "L" == move[0]:
                for i in range(x, x  - tmp_counter, -1):
                    key = (i, y)
                    if key in points:
                        points[key] = points[key] + 1
                    else:
                        points[key] = 1
                x = x - tmp_counter
    return points


points = convert_moves_to_points()
crossings_points = [k for (k,v) in points.items() if v > 1 and (k[0] != 0 and k[1] != 0)]
smallest_manhattan_distance = min((abs(x[0]) + abs(x[1]) for x in crossings_points))

print("number of points: {}".format(len(points)))
print("number crossing of points: {}".format(len(crossings_points)))
print("smallest manhattan distance of a crossing point is: {}".format(smallest_manhattan_distance))
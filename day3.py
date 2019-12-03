#AOC 2019 Brianna Frye
#Day 3

import re

def parse_to_array(base_file):
    #Just going to hardcode it for 2 lines because why not?
    wire_one = []
    wire_two = []
    try:
        file = open(base_file)
        temp = file.readline()
        if temp == '':
            print('-------ERROR--------')
        wire_one = temp.split(',')

        temp = file.readline()
        if temp == '':
            print('-------ERROR--------')
        wire_two = temp.split(',')
        file.close()
        return wire_one, wire_two
    except IOError:
        print('File does not exist!')
    finally:
        print('Parsing complete!')

def list_points(wire):
    #Converts wire into list of coordinates
    wire_coords = []
    pointer = [0,0]
    step_reg = re.compile(r'([UDLR])(\d+)')

    for step in wire:
        raw = step_reg.search(step)
        direction = raw.group(1)
        amount = int(raw.group(2))

        if direction == 'U':
            for i in range(amount + 1):
                wire_coords.append((pointer[0], (pointer[1] + i)))
            pointer = [pointer[0], pointer[1] + amount]
            
        elif direction == 'D':
            for i in range(amount + 1):
                wire_coords.append((pointer[0], (pointer[1] - i)))
            pointer = [pointer[0], pointer[1] - amount]
        elif direction == 'L':
            for i in range(amount + 1):
                wire_coords.append((pointer[0] - i, pointer[1]))
            pointer = [pointer[0] - amount, pointer[1]]
        elif direction == 'R':
            for i in range(amount + 1):
                wire_coords.append((pointer[0] + i, pointer[1]))
            pointer = [pointer[0] + amount, pointer[1]]
    return wire_coords


wire_one, wire_two = parse_to_array('day3input.txt')
wire_one_points = list_points(wire_one)
wire_two_points = list_points(wire_two)

intersections = list(set(wire_one_points) & set(wire_two_points))
intersections.remove((0,0))

min_dist = 1000000
min_point = 0
for i in intersections:
    dist = abs(i[0]) + abs(i[1])
    if dist < min_dist:
        min_dist = dist
        min_point = i

print(min_dist, min_point)
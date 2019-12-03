#AOC 2019 Brianna Frye
#Day 3, part 2

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
    steps = 0
    point_step_dict = {}

    for step in wire:
        raw = step_reg.search(step)
        direction = raw.group(1)
        amount = int(raw.group(2))

        if direction == 'U':
            for i in range(1, amount + 1):
                point = (pointer[0], (pointer[1] + i))
                wire_coords.append(point)
                steps +=1
                if point not in point_step_dict:
                    point_step_dict[point] = steps
            pointer = [pointer[0], pointer[1] + amount]

        elif direction == 'D':
            for i in range(1, amount + 1):
                point = (pointer[0], (pointer[1] - i))
                wire_coords.append(point)
                steps +=1
                if point not in point_step_dict:
                    point_step_dict[point] = steps
            pointer = [pointer[0], pointer[1] - amount]

        elif direction == 'L':
            for i in range(1, amount + 1):
                point = (pointer[0] - i, pointer[1])
                wire_coords.append(point)
                steps +=1
                if point not in point_step_dict:
                    point_step_dict[point] = steps
            pointer = [pointer[0] - amount, pointer[1]]

        elif direction == 'R':
            for i in range(1, amount + 1):
                point = (pointer[0] + i, pointer[1])
                wire_coords.append(point)
                steps +=1
                if point not in point_step_dict:
                    point_step_dict[point] = steps
            pointer = [pointer[0] + amount, pointer[1]]

    return wire_coords, point_step_dict

wire_one, wire_two = parse_to_array('day3input.txt')
wire_one_points, point_step_dict_one = list_points(wire_one)
wire_two_points, point_step_dict_two = list_points(wire_two)

intersections = list(set(wire_one_points) & set(wire_two_points))
#intersections.remove((0,0))
#print(intersections)


min_steps = 100000000
min_point = 0
for i in intersections:
    steps_one = point_step_dict_one[i]
    steps_two = point_step_dict_two[i]
    print(steps_two, steps_one)
    if (steps_one + steps_two) < min_steps:
        min_steps = steps_one + steps_two
        min_point = i

print(min_steps, min_point)
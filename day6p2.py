#AOC 2019 Brianna Frye
#Day 6

import re

def parse_to_array(base_file):
    data_left = True
    output_array = []
    try:
        file = open(base_file)
        while data_left == True:
            temp = file.readline()
            if temp == '':
                data_left = False
            else:
                output_array.append(temp)
        file.close()
        return output_array
    except IOError:
        print('File does not exist!')
    finally:
        print('Parsing complete!')

def list_bodies(inp):
    list_of_bodies = []
    orbit_dict = {}
    map_reg = re.compile(r'(\w{3})\)(\w{3})')
    for entry in inp:
        results = map_reg.search(entry)
        orbiter = results.group(2)
        orbitee = results.group(1)
        orbit_dict[orbiter] = orbitee

        if orbiter not in list_of_bodies:
            list_of_bodies.append(orbiter)

    return list_of_bodies, orbit_dict

def determine_orbits(body, orbit_dict):
    if str(orbit_dict[body]) == 'COM':
        return ['COM']
    else:
        return determine_orbits(orbit_dict[body], orbit_dict) + [body]

def count_jumps(start_body, end_body, orbit_dict):
    if str(orbit_dict[start_body]) == end_body:
        return 0
    else:
        return 1 + count_jumps(orbit_dict[start_body], end_body, orbit_dict)

data = parse_to_array('day6input.txt')

list_of_bodies, orbit_dict = list_bodies(data)

my_map = determine_orbits('YOU', orbit_dict)
santas_map = determine_orbits('SAN', orbit_dict)

common_points = list(set(my_map) & set(santas_map))

lowest_combo = len(my_map) + len(santas_map)
common_point = ''
for i in common_points:
    my_dist = count_jumps('YOU', i, orbit_dict)
    santas_dist = count_jumps('SAN', i, orbit_dict)
    if my_dist + santas_dist < lowest_combo:
        lowest_combo = my_dist + santas_dist
        common_point = i
        print(str(my_dist) + str(santas_dist))

print(lowest_combo)
print(common_point)
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

def count_orbits(body, orbit_dict):
    if str(orbit_dict[body]) == 'COM':
        return 1
    else:
        return 1 + count_orbits(orbit_dict[body], orbit_dict)

data = parse_to_array('day6input.txt')
print(data)

list_of_bodies, orbit_dict = list_bodies(data)

total = 0
for i in list_of_bodies:
    temp = count_orbits(i, orbit_dict)
    total += temp

print(total)
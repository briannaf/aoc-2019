#AOC 2019 Brianna Frye
#Day 8, part 2

def parse_to_array(base_file):
    data_left = True
    output = ''
    try:
        file = open(base_file)
        while data_left == True:
            temp = file.readline()
            if temp == '':
                data_left = False
                break
            output = temp
        file.close()
        return output
    except IOError:
        print('File does not exist!')
    finally:
        print('Parsing complete!')

data = parse_to_array('day8input.txt')
# print(data)

num_layers = int(len(data) / 150)

# print(num_layers)

layers = []

for i in range(0, 15000, 150):
    layers.append(data[i: i + 150])

final = [['.'] * 25 for i in range(6)]

# 0 black
# 1 white
# 2 transp

# for layer in range(len(layers) - 1, -1, -1):
#     for pixel in  range(0, 150):
#         row = pixel // 25
#         col = pixel % 25
#         if str(layers[layer][pixel]) == '0':
#             final[row][col] = 'X'
#         if str(layers[layer][pixel]) == '1':
#             final[row][col] = ' '

for layer in layers:
    for pixel in  range(0, 150):
        row = pixel // 25
        col = pixel % 25
        if str(layer[pixel]) == '0' and final[row][col] == '.':
            final[row][col] = 'X'
        if str(layer[pixel]) == '1' and final[row][col] == '.':
            final[row][col] = ' '

for i in range(6):
    print(final[i])
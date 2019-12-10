#AOC 2019 Brianna Frye
#Day 8

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

# print(layers)

fewest_zeroes = 150
zero_layer = layers[0]

for i in layers:
    # print(i)
    zero_count = 0
    for j in i:
        if str(j) == '0':
            zero_count +=1
    # print(str(len(i)))
    # print(zero_count)
    if zero_count < fewest_zeroes:
        fewest_zeroes = zero_count
        zero_layer = i

# print(fewest_zeroes)
# print(zero_layer)

one_count = 0
two_count = 0
for i in zero_layer:
    if str(i) == '1':
        one_count +=1
    if str(i) == '2':
        two_count += 1

print(one_count)
print(two_count)
print(str(one_count*two_count))

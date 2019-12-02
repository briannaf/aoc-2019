#AOC 2019 Brianna Frye
#Day 2

def parse_to_array(base_file):
    data_left = True
    output_array = []
    try:
        file = open(base_file)
        while data_left == True:
            temp = file.readline()
            if temp == '':
                data_left = False
                break
            output_array = temp.split(',')
        file.close()
        return output_array
    except IOError:
        print('File does not exist!')
    finally:
        print('Parsing complete!')

data = parse_to_array('day2input.txt')
print(data)

i = 0
while(True):
    opcode = int(data[i])
    print('opcode: ' + str(opcode))
    storage = int(data[i + 3])
    print('storage: ' + str(storage))
    if opcode == 1:
        result = int(data[int(data[i + 1])]) + int(data[int(data[i + 2])])
        #print(str(data[i + 1]) + ' + ' + str(data[i + 2]) + ' = ' + str(result))
    elif opcode == 2:
        result = int(data[int(data[i + 1])]) * int(data[int(data[i + 2])])
        #print(str(data[i + 1]) + ' * ' + str(data[i + 2]) + ' = ' + str(result))
    elif opcode == 99:
        print('stopping!')
        break
    else:
        print('YA DONE GOOFED')
    data[storage] = result
    i += 4

print(data)
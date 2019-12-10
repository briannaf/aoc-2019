#AOC 2019 Brianna Frye
#Day 7, part 2

# Opcodes:
# 1 - add, 3 params: num, num, position to store at
#   XXX01
# 2 - multiply, 3 params: num, num, position to store at
#   XXX02
# 3 - input, 1 param: position to store
#   X03
# 4 - output, 1 param: value/address to output
#   X04
# 5 - jump if true, 2 params: condition, jump location
# 6 - jump if false, 2 params: condition, jump location
# 7 - less than, 3 params: base, comparator, storage location
# 8 - equals, 3 params: num, num, storage location
# 99 - halt, no params
#   99
# 0 = position mode
# 1 = immediate mode

from itertools import permutations

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

def intcode_comp(data, phase, amp_input, start):
    modes_specified = False
    entered_phase = False

    if start > 0:
        entered_phase = True
        i = start
    else:
        i = 0
    while(True):
        opcode = int(data[i])
        modes = ''


        if len(str(opcode)) > 1:
            command = int(str(opcode)[-2:])
            modes_specified = True
            modes = str(opcode)[:-2]
        else:
            command = opcode
            modes_specified = False

        # print('opcode: ' + str(opcode))

        # storage = int(data[i + 3])
        # print('storage: ' + str(storage))
        if command == 1:
            if modes_specified:
                #add back leading zeroes
                while len(modes) < 3:
                    modes = '0' + modes
                if int(modes[-1]) == 1:
                    first_addend = int(data[i + 1])
                else:
                    first_addend = int(data[int(data[i + 1])])
                if int(modes[-2]) == 1:
                    second_addend = int(data[i + 2])
                else:
                    second_addend = int(data[int(data[i + 2])])
                storage_location = int(data[i + 3])
            else:
                first_addend = int(data[int(data[i + 1])])
                second_addend = int(data[int(data[i + 2])])
                storage_location = int(data[i + 3])

            # print('adding ' + str(first_addend) + ' and ' + str(second_addend) + ', storing at ' + str(storage_location))
            result = first_addend + second_addend
            data[storage_location] = result
            i += 4

        elif command == 2:

            if modes_specified:
                #add back leading zeroes
                while len(modes) < 3:
                    modes = '0' + modes
                if int(modes[-1]) == 1:
                    first_multiplicand = int(data[i + 1])
                else:
                    first_multiplicand = int(data[int(data[i + 1])])
                if int(modes[-2]) == 1:
                    second_multiplicand = int(data[i + 2])
                else:
                    second_multiplicand = int(data[int(data[i + 2])])

                storage_location = int(data[i + 3])
            else:
                first_multiplicand = int(data[int(data[i + 1])])
                second_multiplicand = int(data[int(data[i + 2])])
                storage_location = int(data[i + 3])
                
            result = first_multiplicand * second_multiplicand
            data[storage_location] = result
            i += 4

        elif command == 3:
            # inp = int(input('HIT AN INPUT COMMAND. PLEASE GIVE INPUT: '))
            # print(str(inp) + ' WAS THE INPUT')
            if entered_phase == True:
                inp = amp_input
            else:
                inp = phase
                entered_phase = True
            if modes_specified:
                if int(modes[0]) == 1:
                    storage_location = int(data[i + 1])
                else:
                    print('YOU MESSED UP SOMEWHERE')
            else:
                storage_location = int(data[i + 1])
            data[storage_location] = inp
            i += 2

        elif command == 4:
            if modes_specified:
                if int(modes[0]) == 1:
                    print('OUTPUT: ' + str(data[i + 1]))
                    return int(data[i + 1]), data, i+2
                    print('OUTPUT: ' + str(data[int(data[i + 1])]))
                    break
                else:
                    print('YOU MESSED UP SOMEWHERE')
            else:
                print('OUTPUT: ' + str(data[int(data[i + 1])]))
                return int(data[int(data[i + 1])]), data, i+2
            i += 2

        elif command == 5:
            if modes_specified:
                #add back leading zeroes
                while len(modes) < 2:
                    modes = '0' + modes
                if int(modes[-1]) == 1:
                    test_num = int(data[i + 1])
                else:
                    test_num = int(data[int(data[i + 1])])
                if int(modes[-2]) == 1:
                    new_pointer = int(data[i + 2])
                else:
                    new_pointer = int(data[int(data[i + 2])])
            else:
                test_num = int(data[int(data[i + 1])])
                # test_num = int(data[i + 1])
                new_pointer = int(data[i + 2])
                new_pointer = int(data[int(data[i + 2])])

            if test_num != 0:
                i = new_pointer
            else:
                i += 3

        elif command == 6:
            if modes_specified:
                #add back leading zeroes
                while len(modes) < 2:
                    modes = '0' + modes
                if int(modes[-1]) == 1:
                    test_num = int(data[i + 1])
                else:
                    test_num = int(data[int(data[i + 1])])
                if int(modes[-2]) == 1:
                    new_pointer = int(data[i + 2])
                else:
                    new_pointer = int(data[int(data[i + 2])])
            else:
                test_num = int(data[int(data[i + 1])])
                new_pointer = int(data[i + 2])
                new_pointer = int(data[int(data[i + 2])])

            if test_num == 0:
                i = new_pointer
            else:
                i += 3

        elif command == 7:
            if modes_specified:
                #add back leading zeroes
                while len(modes) < 3:
                    modes = '0' + modes
                if int(modes[-1]) == 1:
                    first_num = int(data[i + 1])
                else:
                    first_num = int(data[int(data[i + 1])])
                if int(modes[-2]) == 1:
                    second_num = int(data[i + 2])
                else:
                    second_num = int(data[int(data[i + 2])])
                storage_location = int(data[i + 3])
            else:
                first_num = int(data[int(data[i + 1])])
                second_num = int(data[int(data[i + 2])])
                storage_location = int(data[i + 3])

            if first_num < second_num:
                data[storage_location] = 1
            else:
                data[storage_location] = 0
            i += 4

        elif command == 8:
            if modes_specified:
                #add back leading zeroes
                while len(modes) < 3:
                    modes = '0' + modes
                if int(modes[-1]) == 1:
                    first_num = int(data[i + 1])
                else:
                    first_num = int(data[int(data[i + 1])])
                if int(modes[-2]) == 1:
                    second_num = int(data[i + 2])
                else:
                    second_num = int(data[int(data[i + 2])])
                storage_location = int(data[i + 3])
            else:
                first_num = int(data[int(data[i + 1])])
                second_num = int(data[int(data[i + 2])])
                storage_location = int(data[i + 3])

            if first_num == second_num:
                data[storage_location] = 1
            else:
                data[storage_location] = 0
            i += 4

        elif command == 99:
            print('stopping!')
            return -9999, data, i
        else:
            print('YA DONE GOOFED')
            break
        # print(data)

def get_thruster_signal(levels, program):
    current_prog_a = program
    current_prog_b = program
    current_prog_c = program
    current_prog_d = program
    current_prog_e = program

    pointer_a = 0
    pointer_b = 0
    pointer_c = 0
    pointer_d = 0
    pointer_e = 0

    amp_e_out = 0

    temp_final = 0
    
    while True:
        temp_final = amp_e_out
        amp_a_out, current_prog_a, pointer_a = intcode_comp(current_prog_a, levels[0], amp_e_out, pointer_a)
        amp_b_out, current_prog_b, pointer_b = intcode_comp(current_prog_b, levels[1], amp_a_out, pointer_b)
        amp_c_out, current_prog_c, pointer_c = intcode_comp(current_prog_c, levels[2], amp_b_out, pointer_c)
        amp_d_out, current_prog_d, pointer_d = intcode_comp(current_prog_d, levels[3], amp_c_out, pointer_d)
        amp_e_out, current_prog_e, pointer_e = intcode_comp(current_prog_e, levels[4], amp_d_out, pointer_e)
        print('one loop done')
        if amp_e_out == -9999:
            break
    return int(temp_final)


data = parse_to_array('day7input.txt')
level_source = [5, 6, 7, 8, 9]
levels = permutations(level_source)

print(get_thruster_signal(level_source, data))

max_signal = 0
for i in levels:
    temp = get_thruster_signal(i, data)
    if temp > max_signal:
        max_signal = temp

print(max_signal)
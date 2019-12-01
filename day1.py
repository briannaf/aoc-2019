#AOC 2019 Brianna Frye
#Day 1 

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
            output_array.append(temp)
        file.close()
        return output_array
    except IOError:
        print('File does not exist!')
    finally:
        print('Parsing complete!')
		
data = parse_to_array('day1input.txt')

total = 0
temp = 0

for i in data:
	temp = int(i) // 3
	temp -= 2
	total += temp
	
print(str(total))

total = 0
temp = 0

# PART 2
for i in data:
	test = int(i)
	while test > 0:
		temp = test // 3
		temp -= 2
		if temp > 0:
			total += temp
		test = temp

print(total)
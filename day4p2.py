#AOC 2019 Brianna Frye
#Day 4, part 2
import re

candidates = []

double_regex = re.compile(r'(00|11|22|33|44|55|66|77|88|99)')
triple_regex = re.compile(r'(\d*?)(000|111|222|333|444|555|666|777|888|999)(\d*)')
quintuple_regex = re.compile(r'(\d*?)(00000|11111|22222|33333|44444|55555|66666|77777|88888|99999)(\d*)')

for i in range(206938, 679129):
    has_double = False
    increasing = True
    for j in range(0, 5):
        if int(str(i)[j]) > int(str(i)[j + 1]):
            increasing = False
            break
        if int(str(i)[j]) == int(str(i)[j + 1]):
            has_double = True
            
    if has_double and increasing:
        results = quintuple_regex.search(str(i))
        results_2 = triple_regex.search(str(i))
        if results:
            print('kicked out')
            print(i)
        elif results_2:
            first_half_is_triple = triple_regex.search(results_2.group(1))
            last_half_is_triple = triple_regex.search(results_2.group(3))
            first_half_is_double = double_regex.search(results_2.group(1))
            last_half_is_double = double_regex.search(results_2.group(3))
            if first_half_is_triple or last_half_is_triple:
                print('kicked out')
                print(i)
            elif first_half_is_double or last_half_is_double:
                candidates.append(i)
        else:
            candidates.append(i)

print(candidates)
print(len(candidates))
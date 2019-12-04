#AOC 2019 Brianna Frye
#Day 4

# - six digits
# - between 206938-679128
# - two duplicate adjacent digits
# - left to right, digits do not decrease

# 00----
# -00---
# --00--
# ---00-
# ----00

# 222222
# 679999

candidates = []

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
        candidates.append(i)

print(candidates)
print(len(candidates))
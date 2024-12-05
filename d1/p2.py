from typing import Dict, List

# read the file into a 2d or two arrarys
input_file = "input.txt"
# input_file = "test_input.txt"

lines: List[str] = []
with open(input_file, "r") as f:
    lines = f.readlines()

left_list = []
right_list = []
for l in lines:
    split = l.split('   ')
    left_list.append(int(split[0].strip()))
    right_list.append(int(split[1].strip()))

left_list.sort()
right_list.sort()

# Calc the counts of the right list
count_dict = {}
for i in right_list:
    if count_dict.get(i):
        count_dict[i] = count_dict[i] + 1
    else:
        count_dict[i] = 1

sim_score = 0
for i in left_list:
    count = count_dict.get(i)
    if count != None:
        score = count * i
        sim_score = sim_score + score

print(f'sim score: {sim_score}')

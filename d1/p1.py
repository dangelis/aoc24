from typing import List

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

diff = 0
for i in range(len(lines)):
    diff = diff + abs(left_list[i] - right_list[i])

print(f'total diff: {diff}')

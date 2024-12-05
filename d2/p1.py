from typing import List

input_file = "input.txt"
# input_file = "test_input.txt"
# input_file = "test_mini.txt"

lines: List[str] = []
with open(input_file, "r") as f:
    lines = f.readlines()

print(f"reports: {len(lines)}")

safe_count = 0
bad_slope_count = 0
bad_delta_count = 0

for report in lines:
    levels = report.split(" ")

    increasing = True

    print(f"levels 0: {levels[0]}, levels 1: {levels[1]}")


    if int(levels[0]) > int(levels[1]):
        increasing = False  # decreasing

    for i in range(1, len(levels)):
        current = int(levels[i].strip())
        prev = int(levels[i - 1].strip())

        if increasing and (prev > current):
            print(f"report '{levels}' unsafe due to decrease")
            bad_slope_count = bad_slope_count + 1
            break  #unsafe

        if not increasing and (prev < current):
            print(f"report '{levels}' unsafe due to increase")
            bad_slope_count = bad_slope_count + 1
            break #unsafe

        if prev == current:
            print(f"report '{levels}' unsafe due to no slope")
            bad_slope_count = bad_slope_count + 1
            break #unsafe
    
        abs_delta = abs(prev - current)
        if abs_delta < 1 or abs_delta > 3:
            print(f"report '{levels}' unsafe due to delta of {abs_delta}")
            bad_delta_count = bad_delta_count + 1
            break  #unsafe

        if i == len(levels) - 1:
            print(f"report '{levels}' is safe")
            safe_count = safe_count + 1
        
print(f"safe count: {safe_count}")
print(f"bad slope: {bad_slope_count}")
print(f"bad delta count: {bad_delta_count}")

print(f"total: {bad_delta_count + bad_slope_count + safe_count}")

# 218 too low

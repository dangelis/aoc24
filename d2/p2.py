from copy import copy
from typing import List

input_file = "input.txt"
# input_file = "test_input.txt"
# input_file = "test_mini.txt"

lines: List[str] = []
with open(input_file, "r") as f:
    lines = f.readlines()

# print(f"reports: {len(lines)}")


def is_safe_prune(record: list[str]) -> bool:
    
    safe = True
    i, safe = is_safe(record)
    if not safe:
        # Try removing on of each previous? I think just going back 3 indexes would be enough..
        k = i
        while k >= 0:
            print(f"  removing index {k} and trying again")
            c = copy(record)
            c.pop(k)
            m, safe = is_safe(c)
            if safe:
                break
            k = k - 1
    
    return safe


def is_safe(record: list[str]) -> tuple[int, bool]:
    safe = True
    increasing = True
    errors = 0
    index = 1

    # print(f"levels 0: {record[0]}, levels 1: {record[1]}")
    # print(f"  report: {record}")


    if int(record[0]) > int(record[1]):
        increasing = False  # decreasing

    for i in range(1, len(record)):
        current = int(record[i])
        prev = int(record[i - 1])

        index = i

        if increasing and (prev > current):
            print(f"    report '{record}' unsafe due to decrease")
            safe = False
            break  #unsafe

        if not increasing and (prev < current):
            print(f"    report '{record}' unsafe due to increase")
            safe = False
            break #unsafe

        if prev == current:
            print(f"    report '{record}' unsafe due to no slope")
            safe = False
            break #unsafe
    
        abs_delta = abs(prev - current)
        if abs_delta < 1 or abs_delta > 3:
            print(f"    report '{record}' unsafe due to delta of {abs_delta}")
            safe = False
            break  #unsafe
    
    if safe:
        print(f"    safe")

    return index, safe


safe_count = 0

for report in lines:
    report = report.strip()
    levels = report.split(" ")

    print(f"report: {report}")
    if is_safe_prune(levels):
        safe_count = safe_count + 1

   
        
print(f"safe count: {safe_count}")


# 289 too low
# 293
from typing import List


def parse_operand(input: str, idx: int) -> int:
    number_str = ""
    number_len = 0
    print(f"  parse_operand starting with {input[idx]}")
    while input[idx].isnumeric() or number_len > 3:
        number_str = number_str + input[idx]
        print(f"    number_str now {number_str}")
        idx += 1
        number_len += 1

    print(f"found number_str: {number_str} lenght {number_len}. Next input: {input[idx]}")
    
    if number_len > 3 or not (input[idx] == ',' or input[idx] == ')'):
        return -1 

    print(f"  returning number_str {number_str}")
    return int(number_str)




input_file = "input.txt"
# input_file = "test_input.txt"
# input_file = "test_mini.txt"

input: str
with open(input_file, "r") as f:
    input = f.read()

print(f"input: {input}")

sum = 0
c = 0
while c < len(input):
    c_char = input[c]
    if c_char == 'm':
        print(f"found {c_char}")
        end_range = c + 4
        window = input[c:end_range]
        if window == "mul(":
            print(f"found {window}")
            # valid so far, now check numbers
            c = end_range
            op1 = parse_operand(input, c)

            if op1 > 0:
                print(f"first op: {op1}")
                #skip past first op and comma
                c += len(str(op1)) + 1
                op2 = parse_operand(input, c)
                if op2 > 0:
                    print(f"second op: {op2}")
                    prod = op1 * op2
                    print(f"prod: {prod}")
                    sum += prod
                    print(f"sum: {sum}")
        else:
            print(f"after m didn't find match, window: {window}")
    else:
        print(f"char was {c_char}, moving on")
    

    c += 1

print(f"total: {sum}")

#182619815
    


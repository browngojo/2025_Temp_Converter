def round_ans(val):
    var_rounded = (val * 2 + 1) // 2
    return f"{var_rounded:.0f}"

def to_celsius(to_convert):
    item = (to_convert - 32) * (5/9)
    return round_ans(item)

def to_fahrenheit(to_convert):
    item = (to_convert * (9/5)) + 32
    return round_ans(item)

    
# Main Routine / Testing starts here
to_c_test = [0, 100, -459]
to_f_test = [0, 100, 40, -273]

for item in to_f_test:
    ans = to_fahrenheit(item)
    print(f"{item} C is {ans} F")

print()

for item in to_c_test:
    ans = to_celsius(item)
    print(f"{item} F is {ans} C")
f = open('input.txt', "r")
lines = f.readlines()
f.close()

print (list(lines))

file_lines = list(lines)

def process(o_line):
    c_line = o_line.rstrip("\n")
    return c_line

nums={0:0}

def sum (a):
    num = a
    sol = 0
    while (sol == 0):
        for i in file_lines:
            if (process(i)[0] == '+'):
                num += int(process(i)[1:])
            else:
                num -= int(process(i)[1:])
            if not(num in nums.keys()):
                nums[num] = 1
            else:
                nums[num] = nums[num] + 1

            if (nums[num] == 2):
                sol = num
    print (num, sol)

sum(0)

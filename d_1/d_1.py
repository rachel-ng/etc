f = open('input.txt', "r")
lines = f.readlines()
f.close()

print (list(lines))

file_lines = list(lines)

def process(o_line):
    c_line = o_line.rstrip("\n")
    return c_line

def sum ():
    num = 0
    for i in file_lines:
        if (process(i)[0] == '+'):
            num += int(process(i)[1:])
        else:
            num -= int(process(i)[1:])
    return num

print(sum())

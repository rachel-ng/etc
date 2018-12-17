f = open('input.txt', "r")
lines = f.readlines()
f.close()

print (list(lines))

file_lines = list(lines)

def process(o_line):
    c_line = o_line.rstrip("\n").replace("x","").replace("y","").replace("=","").split(",")
    return c_line[0], c_line[1]

for i in file_lines:
    print(process(i))

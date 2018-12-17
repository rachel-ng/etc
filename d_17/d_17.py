f = open('input.txt', "r")
lines = f.readlines()
f.close()

print (list(lines))

file_lines = list(lines)

def process(o_line):
    c_line = o_line.rstrip("\n").replace("x","").replace("y","").replace("=","").split(",")
    one = c_line[0].strip()
    two = c_line[0].strip()
    return one, two

for i in file_lines:
    print(process(i))

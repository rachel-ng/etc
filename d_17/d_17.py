f = open('input.txt', "r")
lines = f.readlines()
f.close()

print (list(lines))

file_lines = list(lines)

def process(o_line):
    c_line = o_line.rstrip("\n").replace("x","").replace("y","").replace("=","").split(",")
    return c_line[0], c_line[1][1:]

x = {}

y = {}

for i in file_lines:
    reeeee = process(i)
    if not(reeeee[0] in x.keys()):
        x[reeeee[0]] = 1
    else:
        x[reeeee[0]] += 1
    if not(reeeee[1] in y.keys()):
        y[reeeee[1]] = 1
    else:
        y[reeeee[1]] += 1

print (x)

print (y)

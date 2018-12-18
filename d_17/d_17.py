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
y2 = {}

for i in file_lines:
    reeeee = process(i)
    if not(reeeee[0] in x.keys()):
        x[reeeee[0]] = 1
    else:
        x[reeeee[0]] += 1
    oof = reeeee[1]
    uh = oof[0].split("...")
    print (uh)
    if not(uh[1] in y.keys()):
        y[uh[1]] = [uh[0]]
    else:
        y[uh[1]].append(uh[0])

print (x)

print (y)

print (max(x.keys()))

print (max(y.keys()))

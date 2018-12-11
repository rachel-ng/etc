f = open('input.txt', "r")
lines = f.readlines()
f.close()

#print (list(lines))

file_lines = list(lines)

def process(o_line):
    c_line = o_line[1:].replace("@","").replace(","," ").replace("x"," ").rstrip("\n").split()
    #print(c_line)
    return c_line



locations = {}

print(['claim number', 'x left', 'x top', 'x wide', 'x tall'])

for i in file_lines:
    print(process(i))

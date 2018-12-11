f = open('input.txt', "r")
lines = f.readlines()
f.close()

#print (list(lines))

file_lines = list(lines)

def process(o_line):
    c_line = o_line.rstrip("\n").split()
    #print(c_line)
    return c_line

for i in file_lines:
    print(process(i))

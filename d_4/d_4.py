f = open('input.txt', "r")
lines = f.readlines()
f.close()

#print (list(lines))

file_lines = list(lines)

def process(o_line):
    c_line = o_line[1:].replace("@","").replace(":","").replace(","," ").replace("x"," ").rstrip("\n").split()
    #print(c_line)
    return c_line

cleaned_lines = []

for i in file_lines:
    cleaned_lines.append(process(i))

print (cleaned_lines)

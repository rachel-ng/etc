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


locations = {}

print(['claim number', 'x left', 'x top', 'x wide', 'x tall'])

for i in cleaned_lines:
    a = int(i[1]) # stay the same
    b = int(i[2]) # stay the same
    c = int(i[3])
    d = int(i[4])
    while c > -1:
        x = a + c
        while d > -1:
            y = b + d
            z = str(x) + "," + str(y)
            print(z)
            if not(z in locations.keys()):
                locations[z] = 1
            else:
                locations[z] += 1
            d -= 1
        c -= 1

print(locations)

sum = 0
for i in locations.values():
    if i > 1:
        sum += 1

print(sum)

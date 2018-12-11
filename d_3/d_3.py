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
cleaned_lines_2 = []

for i in file_lines:
    cleaned_lines.append(process(i))
    cleaned_lines_2.append(process(i))

locations = {}

print(['claim number', 'x left', 'x top', 'x wide', 'x tall'])

for i in cleaned_lines:
    a = int(i[1]) # stay the same
    b = int(i[2]) # stay the same
    c = int(i[3])
    d = int(i[4])
    while c > 0:
        x = a + c
        while d > 0:
            y = b + d
            z = str(x) + "," + str(y)
            #print(z)
            if not(z in locations.keys()):
                locations[z] = 1
            else:
                locations[z] += 1
            d -= 1
        d = int(i[4])
        c -= 1

#print(locations)

sum = 0
for i in locations.values():
    if i > 1:
        sum += 1

print(sum)

claims = {}

for i in cleaned_lines_2:
    a = int(i[1]) # stay the same
    b = int(i[2]) # stay the same
    c = int(i[3])
    d = int(i[4])
    while c > 0:
        x = a + c
        while d > 0:
            y = b + d
            z = str(x) + "," + str(y)
            #print(z)
            if not(z in claims.keys()):
                claims[z] = []
                claims[z].append(i[0])
            else:
                claims[z].append(i[0])
            d -= 1
        d = int(i[4])
        c -= 1

#print(claims)

valid_claims = {}

for i in claims.keys():
    for c in i:
        if not(c in valid_claims.keys()):
            valid_claims[c] = ""

print(valid_claims)

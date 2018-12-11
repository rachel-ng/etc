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
claims = {}

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
            if not(z in locations.keys()):
                locations[z] = 1
                claims[z] = [i[0]]
            else:
                locations[z] += 1
                claims[z].append(i[0])
            d -= 1
        d = int(i[4])
        c -= 1

#print(locations)
#print(claims.values())

claimed = list(claims.values())

claimed.sort()

#print(claimed)

ok_claims = {}
total_inches = {}

for i in claimed:
    if len(i) == 1:
        if not(i in ok_claims.keys()):
            total_inches[i] = int(cleaned_lines[i][3]) * int(cleaned_lines[i][4])
            print(int(cleaned_lines[i][3]) * int(cleaned_lines[i][4]))
            ok_claims[i] = 1
        else:
            ok_claims[i] += 1

#print(ok_claims)
#print(total_inches)

sum = 0
for i in locations.values():
    if i > 1:
        sum += 1

print(sum)

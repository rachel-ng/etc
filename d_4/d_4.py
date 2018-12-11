f = open('input.txt', "r")
lines = f.readlines()
f.close()

#print (list(lines))

file_lines = list(lines)

def process(o_line):
    c_line = o_line[1:].replace("1518","").replace("[","").replace("]","").replace("#","").replace("@","").replace(":","").replace(","," ").replace("-"," ").replace("x"," ").rstrip("\n").split()
    #print(c_line)
    return c_line

cleaned_lines = []

for i in file_lines:
    cleaned_lines.append(process(i))

cleaned_lines.sort()

#print (cleaned_lines)

months = {}
guard_ids = {}

for i in cleaned_lines:
    if (len(i) == 7):
        guard_ids[i[3]]
    if not(i[0] in months.keys()):
        months[i[0]] = []
        months[i[0]].append(i[1:])
        print(i[0])
    else:
        months[i[0]].append(i[1:])

for m in months:
    for i in months[m]:
        print (m + ":\t" + str(i))

for g in guard_ids:
    print(g)

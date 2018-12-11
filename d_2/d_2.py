
f = open('input.txt', "r")
lines = f.readlines()
f.close()

print (list(lines))

file_lines = list(lines)

def process(o_line):
    c_line = o_line.rstrip("\n")
    #print(c_line)
    return c_line


def compare(box_id):
    letters = {}
    i = 0
    while (i < len(box_id)):
        if not(box_id[i] in letters.keys()):
            letters[box_id[i]] = 1
        else:
            letters[box_id[i]] = letters[box_id[i]] + 1
        i += 1
    print(letters)
    return letters

def mult(letters):
    two = 0
    three = 0
    if (2 in letters.values()):
        two = 1
    if (3 in letters.values()):
        three = 1
    return (two, three)

two_same = {}
three_same = {}
twothree_same = {}
neither = {}

def twothree():
    two = 0
    three = 0
    for box_id in file_lines:
        dos, tres = mult(compare(process(box_id)))
        if ((dos == 1) and (tres == 1)):
            twothree_same[process(box_id)] = ""
        if (dos == 1):
            two_same[process(box_id)] = ""
        if (tres == 1):
            three_same[process(box_id)] = ""
        else:
            neither[process(box_id)] = ""
        two += dos
        three += tres
    print(two * three)

twothree()

#print("two same")
#print(list(two_same.keys()))
#print("three same")
#print(list(three_same.keys()))
#print("both same")
#print(list(twothree_same.keys()))
#print("no same")
#print(list(neither.keys()))



two_three = list(twothree_same.keys())

two_three.sort()

#print (two_three)

yikes = [
    'udtoeizfvmbrttpkgnhacjxwld',
    'ugygeizfvmbrmtpkgnhacjxwld',
    'uqyhepzfvmbrstpkghhacjxwld',
    'uqyleizfgmbrstlkgnhacjxwld',
    'uqyoeikfvmbrstpkgehacjxwle',
    'uqyoeisfvmbrstpkglhscjxwld',
    'uqyoeixfvlbrstpkgxhacjxwld',
    'uqyoeizfvebrsypygnhacjxwld',
    'uqyoeizfvmbjstpmgnhacjxmld',
    'uqyoeizfvmbrsfpkgnhfcdxwld',
    'uqyoeizfvmbrstekgnhayjywld',
    'uqyoeizfvmbrstpkgmoacjxwlm',
    'uqyoeizyvmbrsdpkgnhacdxwld',
    'uqyoiizcvmbrsipkgnhacjxwld',
    'uqyoxizfvmbrsggkgnhacjxwld']

print(yikes)

yikess = []

for i in yikes:
    if (i[0] == "u") :
        yikess.append(i[1:])
    else:
        yikess.append(i)

print(yikess)

yikesss = []

for i in yikess:
    if(i[-2:] == "ld"):
        yikesss.append(i[:-2])
    else:
        yikesss.append(i)

print(yikesss)

q = []
other = []

for i in yikesss:
    if (i[0] == "q"):
        q.append(i[1:])

print (q)


q1 = []
for i in q:
    if (i[0] == "y"):
        q1.append(i[1:])
    else:
        other.append(i)

print (q1)

other1 = []
e = []

for i in q1:
    if (i[0] == "o" and i[1] == "e"):
        e.append(i[2:])
    else:
        other1.append(i)

e.sort()
print(e[1:])

e2 = []
for i in e: 
    if (i[0] == "i"):
        e2.append(i[1:])
    else:
        other1.append(i)

print (e2)
print(len(e2))


e3=[]

for i in e2: 
    print(len(i))
    if (i[4] == "b" and len(i) == 18):
        e3.append(i[:4] + i[5:])
    else:
        other1.append(i)

print (e3)
print(len(e3))



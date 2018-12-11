
f = open('input.txt', "r")
lines = f.readlines()
f.close()

#print (list(lines))

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
    #print(letters)
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

check = list(neither.keys())

check.sort()

#print(check)


first_letters = {}

for i in check:
    if not(i[0] in first_letters.keys()):
        first_letters[i[0]] = [i]
    else:
        first_letters[i[0]].append(i)

for i in first_letters:
    print (i + "\t" + str(first_letters[i]))

yikes = []
for i in first_letters['u']: # len = 25
    yikes.append(i[1:])

print (yikes)

for i in first_letters.keys():
    if i == 'u':
        print ("no")
    else:
        for u in i:
            print(u)
            print (len(u))

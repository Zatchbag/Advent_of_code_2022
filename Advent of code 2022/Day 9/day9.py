# open input files
with open('exampleinput.txt', 'r') as exampleinputfile:
    exampleinputwhole = exampleinputfile.read()
with open('input.txt', 'r') as inputfile:
    inputwhole = inputfile.read()

# format input
exampleinput_newline = exampleinputwhole.split('\n')
exampleinput = []
exampletemporarylist = []
for x in exampleinput_newline:
    exampletemporarylist.append(x.split(' '))
for z in exampletemporarylist:
    y = (z[0], z[1])
    exampleinput.append(y)

input_newline = inputwhole.split('\n')
input = []
temporarylist = []
for x in input_newline:
    temporarylist.append(x.split(' '))
for z in temporarylist:
    y = (z[0], z[1])
    input.append(y)

def headmovements(input):
    H = [0,0]
    headmovementslist = []
    for command in input:
        direction, count = command
        if direction == 'R':
            for x in range(int(count)):
                H[0] += 1
                headmovementslist.append(H[:])
        elif direction == 'L':
            for x in range(int(count)):
                H[0] -= 1
                headmovementslist.append(H[:])
        elif direction == 'U':
            for x in range(int(count)):
                H[1] += 1
                headmovementslist.append(H[:])
        elif direction == 'D':
            for x in range(int(count)):
                H[1] -= 1
                headmovementslist.append(H[:])
    return headmovementslist

def tailmovements(input):
    T = [0,0]
    tailmovementslist = []
    for headpostion in input:
        x, y = headpostion
# # difference of 2, difference of 0, x + 1
# # differnce of -2, difference of 0, x - 1 
        if x - T[0] == 2 and y - T[1] == 0 or x - T[0] == -abs(2) and y - T[1] == 0:
            T[0] += int((1 * ((x - T[0]) / 2)))
            tailmovementslist.append(T[:])
# # difference of 0, difference of +2, y + 1 
# # difference of 0, difference of -2, y - 1
        elif x - T[0] == 0 and y - T[1] == 2 or x - T[0] == 0 and y - T[1] == -abs(2):
            T[1] += int((1 * ((y - T[1]) / 2)))
            tailmovementslist.append(T[:])
# # difference of 0, difference of abs(1), same
# # difference of abs(1), difference of 0, same
# # difference of 0, difference of 0, same
# # difference of abs(1), difference of abs(1), same
        elif abs(x - T[0]) == 1 and abs(y - T[1]) == 0 or abs(x - T[0]) == 0 and abs(y - T[1]) == 1 or abs(x - T[0]) == 0 and abs(y - T[1]) == 0 or abs(x - T[0]) == 1 and abs(y - T[1]) == 1:
            tailmovementslist.append(T[:])
# # difference of 2, difference of -1, x + 1 y - 1
# # difference of 1, difference of -2, x + 1 y - 1
        elif x - T[0] == 2 and y - T[1] == -1 or x - T[0] == 1 and y - T[1] == -2:
            T[0] += 1
            T[1] -= 1
            tailmovementslist.append(T[:])
# # difference of -2, difference of 1, x - 1 y + 1
# # difference of -1, difference of 2, x - 1 y + 1
        elif x - T[0] == -2 and y - T[1] == 1 or x - T[0] == -1 and y - T[1] == 2:
            T[0] -= 1
            T[1] += 1
            tailmovementslist.append(T[:])
# # difference of 2, difference of 1, x + 1 y + 1
# # difference of 1, difference of 2, x + 1 y + 1
        elif x - T[0] == 2 and y - T[1] == 1 or x - T[0] == 1 and y - T[1] == 2:
            T[0] += 1
            T[1] += 1
            tailmovementslist.append(T[:])
# # difference of -2, difference of -1, x - 1 y - 1
# # difference of -1, difference of -2, x - 1 y - 1
        elif x - T[0] == -2 and y - T[1] == -1 or x - T[0] == -1 and y - T[1] == -2:
            T[0] -= 1
            T[1] -= 1
            tailmovementslist.append(T[:])

    return tailmovementslist
        
def uniquecount(input):
    uniquelist = []
    for x in input:
        if x not in uniquelist:
            uniquelist.append(x)
    return len(uniquelist)

# print('Unique locations visited: ' + str(uniquecount(tailmovements(headmovements(input)))))

# part 2 solution
firstinput = headmovements(exampleinput)
print()
print(firstinput)
secondinput = tailmovements(firstinput)
print()
print(secondinput)
thirdinput = tailmovements(secondinput)
print()
print(thirdinput)
fourthinput = tailmovements(thirdinput)
print()
print(fourthinput)
fifthinput = tailmovements(fourthinput)
print()
print(fifthinput)
sixthinput = tailmovements(fifthinput)
print()
print(sixthinput)

print(tailmovements(sixthinput))
print()
# eighthinput = tailmovements(seventhinput)
# print()
# print(eighthinput)
# ninthinput = tailmovements(eighthinput)
# print()
# print(ninthinput)
# tenthinput = tailmovements(ninthinput)
# print()
# print(tenthinput)
# print(uniquecount(tenthinput))

# print(headmovements(exampleinput))


# def tailmovements(input):
#     tailmovementslist = []
#     headindex = 0
#     for headpostion in input:
#         x, y = headpostion
#         if x - T[0] == 2 and y - T[1] == 0 or x - T[0] == -abs(2) and y - T[1] == 0:
#             T[0] += int((1 * ((x - T[0]) / 2)))
#             tailmovementslist.append(T[:])
#             headindex += 1
#         elif x - T[0] == 0 and y - T[1] == 2 or x - T[0] == 0 and y - T[1] == -abs(2):
#             T[1] += int((1 * ((y - T[1]) / 2)))
#             tailmovementslist.append(T[:])
#             headindex += 1
#         elif abs(x - T[0]) == 1 and abs(y - T[1]) == 0 or abs(x - T[0]) == 0 and abs(y - T[1]) == 1 or abs(x - T[0]) == 0 and abs(y - T[1]) == 0 or abs(x - T[0]) == 1 and abs(y - T[1]) == 1:
#             tailmovementslist.append(T[:])
#             headindex += 1
#         elif abs(x - T[0]) == 2 and abs(y - T[1]) == 1 or abs(x - T[0]) == 1 and abs(y - T[1]) == 2:
#             T[0] = input[headindex-1][0]
#             T[1] = input[headindex-1][1]
#             tailmovementslist.append(T[:])
#             headindex += 1
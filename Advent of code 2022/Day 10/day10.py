# open input files
with open('exampleinput.txt', 'r') as exampleinputfile:
    exampleinputwhole = exampleinputfile.read()
with open('input.txt', 'r') as inputfile:
    inputwhole = inputfile.read()

# format input files
exampleinputlines = exampleinputwhole.splitlines()
exampleinput = []
for x in exampleinputlines:
    y = x.split(' ')
    exampleinput.append(y)

inputlines = inputwhole.splitlines()
input = []
for x in inputlines:
    y = x.split(' ')
    input.append(y)

# Part 1
# -----------------------------------------------------------------------
# if line == "noop", add 1 to cyclecount
# else, add 2 to cyclecount
    # split cyclecount + 2 by + 1s and add verify logic between.

# if line == "noop", x = x
# else, x += VALUE

# if cyclecount % 20 == 0, cyclecount * x
    # append to signalstrength list

# sum(signalstrength list)

signalstrength = []

def part1(input):
    x = 1
    cyclecount = 0
    signalstrength = []
    for individualcommand in input:
        if individualcommand[0] == 'noop':
            print(individualcommand)
            cyclecount += 1
            if cyclecount % 20 == 0:
                print('cyclecount is divisible by 20 @ ' + str(cyclecount) + ' and x is currently ' + str(x))
                y = x * cyclecount
                signalstrength.append(y)
            else:
                pass
            print(cyclecount)
        else:
            print(individualcommand)
            cyclecount += 1
            print(cyclecount)
            if cyclecount % 20 == 0:
                print('cyclecount is divisible by 20 @ ' + str(cyclecount) + ' and x is currently ' + str(x))
                y = x * cyclecount
                signalstrength.append(y)
            else:
                pass
            cyclecount += 1
            if cyclecount % 20 == 0:
                print('cyclecount is divisible by 20 @ ' + str(cyclecount) + ' and x is currently ' + str(x))
                y = x * cyclecount
                signalstrength.append(y)
            else:
                pass
            print(cyclecount)
            x += int(individualcommand[1])
    del signalstrength[1::2]
    print(signalstrength)
    return sum(signalstrength)

# print(part1(input))


# Part 2
# -----------------------------------------------------------------------

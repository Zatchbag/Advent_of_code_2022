from pprint import pprint

with open('exampleinput.txt', 'r') as exampleinputfile:
    exampleinput = exampleinputfile.read()
with open('input.txt', 'r') as inputfile:
    input = inputfile.read()

def directories(input):
    path = []
    directory = {'/home/': 0}
    firstsplit = input.splitlines()
    for line in firstsplit:
        line = line.split()
        print(line)
        if line[0] == "$":
            if line[1] == "ls":
                pass
            else:
                if line[2] == '..':
                    path = path[:-1]
                elif line[2] == '/':
                    directory['/home/'] = 0
                else:
                    path.append(line[2])
                    joinedpath = '/home/' + '/'.join(path)
                    directory[joinedpath] = 0
        else:
            if line[0] != 'dir':
                temppath = '/home/' + '/'.join(path)
                for key in directory.keys():
                    if key in temppath:
                        directory[key] += int(line[0])

    directoryvalues = list(directory.values())
    for value in directoryvalues[1:]:
        directory['/home/'] -= value

    directory['/home/'] = sum(directory.values())
    
    return directory


def directorysum(input):
    newlist = []
    for value in list(input.values()):
        if value <= 100000:
            newlist.append(value)
        else:
            pass
    return sum(newlist)

def deletewhich(input):
    availablevolume = 70000000 - input['/home/']
    targetvolume = 30000000 - availablevolume
    targetdelete = 99999999999999
    for value in list(input.values()):
        if value >= targetvolume and value < targetdelete:
            targetdelete = value
    return targetdelete




pprint(directories(exampleinput))
pprint(directorysum(directories(exampleinput)))
pprint(deletewhich(directories(input)))
    



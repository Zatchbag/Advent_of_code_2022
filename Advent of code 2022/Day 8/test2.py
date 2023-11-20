def format_number(input):
    inputstring = reversed(str(input))
    finalstring = []
    count = 0
    for letter in inputstring:
        if count < 3:
            finalstring.append(letter)
            count += 1
        if count == 3:
            count = 0
            finalstring.append(",")
    reversedfinalstring = list(reversed(finalstring))

    if reversedfinalstring[0] == ',':
        del reversedfinalstring[0]

    return "".join(reversedfinalstring)
    
print(format_number(6987498279857923650984732))
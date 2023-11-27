# imports
from pprint import pprint
import math

# input
items = {
    'monkey0' : [50, 70, 89, 75, 66, 66], 
    'monkey1' : [85], 
    'monkey2' : [66, 51, 71, 76, 58, 55, 58, 60], 
    'monkey3' : [79, 52, 55, 51], 
    'monkey4' : [69, 92], 
    'monkey5' : [71, 76, 73, 98, 67, 79, 99], 
    'monkey6' : [82, 76, 69, 69, 57], 
    'monkey7' : [65, 79, 86]
    }

exampleitems = {
    'monkey0' : [79, 98], 
    'monkey1' : [54, 65, 75, 74], 
    'monkey2' : [79, 60, 97], 
    'monkey3' : [74], 
}


# solutions
inspectioncountdict = {
    'monkey0' : 0, 
    'monkey1' : 0, 
    'monkey2' : 0, 
    'monkey3' : 0,
    'monkey4' : 0, 
    'monkey5' : 0, 
    'monkey6' : 0, 
    'monkey7' : 0, 
}

exampleinspectioncountdict = {
    'monkey0' : 0, 
    'monkey1' : 0, 
    'monkey2' : 0, 
    'monkey3' : 0,
}
    
# def round(dictionary):
#     # monkey0
#     inspectioncountdict['monkey0'] += len(dictionary['monkey0'])
#     for item in dictionary['monkey0']:
#         new = int(math.floor((item * 5)/3))
#         if new % 2 == 0:
#             dictionary['monkey2'].append(new)
#         else:
#             dictionary['monkey1'].append(new)
#     dictionary['monkey0'] = []

#     # monkey1
#     inspectioncountdict['monkey1'] += len(dictionary['monkey1'])
#     for item in dictionary['monkey1']:
#         new = int(math.floor((item * item)/3))
#         if new % 7 == 0:
#             dictionary['monkey3'].append(new)
#         else:
#             dictionary['monkey6'].append(new)
#     dictionary['monkey1'] = []

#     # monkey2
#     inspectioncountdict['monkey2'] += len(dictionary['monkey2'])
#     for item in dictionary['monkey2']:
#         new = int(math.floor((item + 1)/3))
#         if new % 13 == 0:
#             dictionary['monkey1'].append(new)
#         else:
#             dictionary['monkey3'].append(new)
#     dictionary['monkey2'] = []

#     # monkey3
#     inspectioncountdict['monkey3'] += len(dictionary['monkey3'])
#     for item in dictionary['monkey3']:
#         new = int(math.floor((item + 6)/3))
#         if new % 3 == 0:
#             dictionary['monkey6'].append(new)
#         else:
#             dictionary['monkey4'].append(new)
#     dictionary['monkey3'] = []

#     # monkey4
#     inspectioncountdict['monkey4'] += len(dictionary['monkey4'])
#     for item in dictionary['monkey4']:
#         new = int(math.floor((item * 17)/3))
#         if new % 19 == 0:
#             dictionary['monkey7'].append(new)
#         else:
#             dictionary['monkey5'].append(new)
#     dictionary['monkey4'] = []

#     # monkey5
#     inspectioncountdict['monkey5'] += len(dictionary['monkey5'])
#     for item in dictionary['monkey5']:
#         new = int(math.floor((item + 8)/3))
#         if new % 5 == 0:
#             dictionary['monkey0'].append(new)
#         else:
#             dictionary['monkey2'].append(new)
#     dictionary['monkey5'] = []

#     # monkey6
#     inspectioncountdict['monkey6'] += len(dictionary['monkey6'])
#     for item in dictionary['monkey6']:
#         new = int(math.floor((item + 7)/3))
#         if new % 11 == 0:
#             dictionary['monkey7'].append(new)
#         else:
#             dictionary['monkey4'].append(new)
#     dictionary['monkey6'] = []

#     # monkey7
#     inspectioncountdict['monkey7'] += len(dictionary['monkey7'])
#     for item in dictionary['monkey7']:
#         new = int(math.floor((item + 5)/3))
#         if new % 17 == 0:
#             dictionary['monkey5'].append(new)
#         else:
#             dictionary['monkey0'].append(new)
#     dictionary['monkey7'] = []

#     # pprint(inspectioncountdict)
#     return dictionary



# def exampleround(dictionary):
#     # monkey0
#     exampleinspectioncountdict['monkey0'] += len(dictionary['monkey0'])
#     for item in dictionary['monkey0']:
#         new = int(math.floor((item * 19)))
#         if new % 23 == 0:
#             dictionary['monkey2'].append(new)
#         else:
#             dictionary['monkey3'].append(new)
#     dictionary['monkey0'] = []

#     # monkey1
#     exampleinspectioncountdict['monkey1'] += len(dictionary['monkey1'])
#     for item in dictionary['monkey1']:
#         new = int(math.floor((item + 6)))
#         if new % 19 == 0:
#             dictionary['monkey2'].append(new)
#         else:
#             dictionary['monkey0'].append(new)
#     dictionary['monkey1'] = []

#     # monkey2
#     exampleinspectioncountdict['monkey2'] += len(dictionary['monkey2'])
#     for item in dictionary['monkey2']:
#         new = int(math.floor((item * item)))
#         if new % 13 == 0:
#             dictionary['monkey1'].append(new)
#         else:
#             dictionary['monkey3'].append(new)
#     dictionary['monkey2'] = []

#     # monkey3
#     exampleinspectioncountdict['monkey3'] += len(dictionary['monkey3'])
#     for item in dictionary['monkey3']:
#         new = int(math.floor((item + 3)))
#         if new % 17 == 0:
#             dictionary['monkey0'].append(new)
#         else:
#             dictionary['monkey1'].append(new)
#     dictionary['monkey3'] = []

#     pprint(dictionary)
#     pprint(exampleinspectioncountdict)

#     return dictionary


# def recursive_function(input, times, time_count = 1):
#     input = exampleround(input)
#     if time_count >= times:
#         return input
#     else:
#         return recursive_function(input, times, time_count + 1)
    
# recursive_function(exampleround(exampleitems), 100)


# # Part 2
def exampleround2(dictionary):
    # monkey0
    exampleinspectioncountdict['monkey0'] += len(dictionary['monkey0'])
    for item in dictionary['monkey0']:
        new = int(math.floor((item * 19)))
        if new % 23 == 0:
            dictionary['monkey2'].append(new)
        else:
            dictionary['monkey3'].append(new)
    dictionary['monkey0'] = []

    # monkey1
    exampleinspectioncountdict['monkey1'] += len(dictionary['monkey1'])
    for item in dictionary['monkey1']:
        new = int(math.floor((item + 6)))
        if new % 19 == 0:
            dictionary['monkey2'].append(new)
        else:
            dictionary['monkey0'].append(new)
    dictionary['monkey1'] = []

    # monkey2
    exampleinspectioncountdict['monkey2'] += len(dictionary['monkey2'])
    for item in dictionary['monkey2']:
        new = int(math.floor((item * item)))
        if item % 13 == 0:
            dictionary['monkey1'].append(new)
        else:
            dictionary['monkey3'].append(new)
    dictionary['monkey2'] = []

    # monkey3
    exampleinspectioncountdict['monkey3'] += len(dictionary['monkey3'])
    for item in dictionary['monkey3']:
        new = int(math.floor((item + 3)))
        if new % 17 == 0:
            dictionary['monkey0'].append(new)
        else:
            dictionary['monkey1'].append(new)
    dictionary['monkey3'] = []

    pprint(dictionary)
    pprint(exampleinspectioncountdict)

    return dictionary

# def round2(dictionary):
#     # monkey0
#     inspectioncountdict['monkey0'] += len(dictionary['monkey0'])
#     for item in dictionary['monkey0']:
#         new = int(math.floor((item * 5)))
#         if new % 2 == 0:
#             dictionary['monkey2'].append(new)
#         else:
#             dictionary['monkey1'].append(new)
#     dictionary['monkey0'] = []

#     # monkey1
#     inspectioncountdict['monkey1'] += len(dictionary['monkey1'])
#     for item in dictionary['monkey1']:
#         new = int(math.floor((item * item)))
#         if new % 7 == 0:
#             dictionary['monkey3'].append(new)
#         else:
#             dictionary['monkey6'].append(new)
#     dictionary['monkey1'] = []

#     # monkey2
#     inspectioncountdict['monkey2'] += len(dictionary['monkey2'])
#     for item in dictionary['monkey2']:
#         new = int(math.floor((item + 1)))
#         if new % 13 == 0:
#             dictionary['monkey1'].append(new)
#         else:
#             dictionary['monkey3'].append(new)
#     dictionary['monkey2'] = []

#     # monkey3
#     inspectioncountdict['monkey3'] += len(dictionary['monkey3'])
#     for item in dictionary['monkey3']:
#         new = int(math.floor((item + 6)))
#         if new % 3 == 0:
#             dictionary['monkey6'].append(new)
#         else:
#             dictionary['monkey4'].append(new)
#     dictionary['monkey3'] = []

#     # monkey4
#     inspectioncountdict['monkey4'] += len(dictionary['monkey4'])
#     for item in dictionary['monkey4']:
#         new = int(math.floor((item * 17)))
#         if new % 19 == 0:
#             dictionary['monkey7'].append(new)
#         else:
#             dictionary['monkey5'].append(new)
#     dictionary['monkey4'] = []

#     # monkey5
#     inspectioncountdict['monkey5'] += len(dictionary['monkey5'])
#     for item in dictionary['monkey5']:
#         new = int(math.floor((item + 8)))
#         if new % 5 == 0:
#             dictionary['monkey0'].append(new)
#         else:
#             dictionary['monkey2'].append(new)
#     dictionary['monkey5'] = []

#     # monkey6
#     inspectioncountdict['monkey6'] += len(dictionary['monkey6'])
#     for item in dictionary['monkey6']:
#         new = int(math.floor((item + 7)))
#         if new % 11 == 0:
#             dictionary['monkey7'].append(new)
#         else:
#             dictionary['monkey4'].append(new)
#     dictionary['monkey6'] = []

#     # monkey7
#     inspectioncountdict['monkey7'] += len(dictionary['monkey7'])
#     for item in dictionary['monkey7']:
#         new = int(math.floor((item + 5)))
#         if new % 17 == 0:
#             dictionary['monkey5'].append(new)
#         else:
#             dictionary['monkey0'].append(new)
#     dictionary['monkey7'] = []

#     # pprint(inspectioncountdict)
#     return dictionary

def recursive_function(input, times, time_count = 1):
    input = exampleround2(input)
    if time_count >= times:
        return input
    else:
        return recursive_function(input, times, time_count + 1)
    
recursive_function(exampleround2(exampleitems), 1000)
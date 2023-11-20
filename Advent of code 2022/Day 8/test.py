x = [[6,2,3,4,8],[1,2,3,4,5],[5,4,3,2,1],[3,2,1,2,3],[1,2,3,2,1]]
y = 6
n = 1
count = 0

visibilitylist = []
for a in x:
    for number in a:
        templist = []
        visibilitytemplist = []
        # check to the right for taller trees
        for z in range((count+1),len(a)):
            print(a[z])
            if number <= a[z]:
                n = 0
            else:
                pass
            templist.append(n)
            print(templist)
            n=1

        if len(templist) == len(range((count+1),len(a))):
            if 0 in templist:
                visibilitytemplist.append(0)
            else:
                visibilitytemplist.append(1)
            templist = []

        count += 1
        if count == len(a):
            count = 0
        
        # check down for taller trees
        for z in range((count+1),len(a)):
            print(a[z])
            if number <= a[z]:
                n = 0
            else:
                pass
            templist.append(n)
            print(templist)
            n = 1
        templist = []

        if 0 in templist:
            visibilitytemplist.append(0)
        else:
            visibilitytemplist.append(1)

        count += 1
        if count == len(a):
            count = 0


print(n)
#array of array
datastruct = []


def createpascaldatastructure(level):
    if level == 1:
        datastruct.append([1])
    elif level == 2:
        datastruct.append([1, 1])
    elif level >= 3:
        #fetch previous level
        prelevel = datastruct[level-2]
        #create current level
        currlevel = [1]
        #loop for prelevel and add the summed items
        for i in range(0, len(prelevel)-1):
            currlevel.append(prelevel[i]+prelevel[i+1])
        currlevel.append(1)
        #add current level to data structure
        datastruct.append(currlevel)


def printPascal(level):
    for i in range(0, level):
        createpascaldatastructure(i+1)
    #print datastructure in correct format
    tabcount = level-1;
    for n in datastruct:
        lineN = "{}".format("\t"*tabcount)
        tabcount = tabcount-1
        for item in n:
            lineN = lineN + str(item) + "\t\t"
        print(lineN)



printPascal(8)
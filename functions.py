import math
import data

def getDistance(User, Bengkel):
    return euclidDist(User.location, Bengkel.location)

def euclidDist(listA, listB):
    itLA = iter(listA)
    itLB = iter(listB)
    result = 0
    for i,j in zip(itLA, itLB):
        result += (i-j)**2
    return math.sqrt(result)

def cariBengkel(User):
    itBgkl = iter(data.listBengkel)
    min = 999999
    for i in itBgkl:
        dist = getDistance(User, i)
        if (dist < min):
            min = dist
            result = i
    return print(result.name)
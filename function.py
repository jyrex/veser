from main import *

def getDistance(user, bengkel):
    return euclidDist(user, bengkel)

def euclidDist(listA, listB):
    itLA = iter(listA[1])
    itLB = iter(listB[1])
    result = 0
    for i,j in zip(itLA, itLB):
        result += (i-j)**2
    return math.sqrt(result)

def cariBengkel(user):
    itBgkl = iter(listBengkel)
    min = 999999
    for i in itBgkl:
        dist = getDistance(user, i)
        if (dist < min):
            min = dist
            result = i
            #globals()[pilih] = pilih+1
    #return print(result[0])
    return result[0]

#def makeOrder(idUser, Keluhan):
    #order += [idOrder, idUser, idBengkel]

#def checkPrice():

#def placeOrder():

#def updateStatus():

#def updatePrice():


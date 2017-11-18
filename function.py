import math
from data import *

def getDistance(user, bengkel):
    return euclidDist(user, bengkel)

def euclidDist(listA, listB):
    itLA = iter(listA.lokasi)
    itLB = iter(listB.lokasi)
    result = 0
    for i,j in zip(itLA, itLB):
        result += (i-j)**2
    return math.sqrt(result)

def cariBengkel(User):
    itbgkl = iter(bengkel)
    min = 999999
    for i in itbgkl:
        dist = getDistance(User, i)
        if (dist < min):
            min = dist
            result = i
    return result.nama

#def makeOrder(idUser, Keluhan):
    #order += [idOrder, idUser, idBengkel]

#def checkPrice():

#def placeOrder():

#def updateStatus():

#def updatePrice():


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
    #for debug purpose
    #print(result.kode,result.nama,result.lokasi)
    return result


def placeOrder(idord, ord, quantity, user, namaB):
    order.append(Order(idord, user.kode, namaB.kode))
    detail.append(Detail(order[len(order) - 1], ord, len(ord)*50, quantity))
    print ("\ntotal order = ")
    for i in range(0, len(order)):
        print("ID Order = {}".format(order[i].kode))
        print("ID User = {}".format(order[i].user))
        print("ID Bengkel = {}".format(order[i].bengkel))
        if (order[i].kode == detail[i].kode):
            print("keluhan = {}".format(detail[i].namaService))
        print('\n')


#def checkPrice():


#def updateStatus():

#def updatePrice():


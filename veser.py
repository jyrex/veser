import math

userA = ["Randy", [1, 3]]
userB = ["Axel", [4, 5]]
userC = ["Julio", [2,7]]
listUser = [userA, userB, userC]

bgklA = ["Yamaha", [3,4]]
bgklB = ["Honda", [0,6]]
bgklC = ["Suzuki", [1,1]]
listBengkel = [bgklA, bgklB, bgklC]

def getDistance(listUser, listBengkel):
    return euclidDist(listUser, listBengkel)

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
    return print(result[0])

#main program
print("userA = ",userA,"\nuserB = ",userB,"\nuserC = ",userC)
inp = input("pilih user = ")
# inp = input("pilih user (1, 2, 3 )= ")
# if (inp = 1):
#     inp = usrA
# elif (inp = 2):

cariBengkel(locals()[inp])
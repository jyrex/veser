from data import *
from function import *
import time
import math

#start main program
for i in range(0, len(user)) :
    print("{} = {}".format(user[i].kode, user[i].nama))

#choose user and then save user into var usr
usr = int(input("pilih user = "))
usr = user[usr-1]


#for debug purpose
#print(usr.kode, usr.nama, usr.lokasi)

#user choose for service or just bengkel list
print ("\n1. Service \n2. List Bengkel")
inp = int(input("masukan pilihan = "))
print ('\n')

#service
if (inp == 1):
    namaB = cariBengkel(user[inp])
    print("Bengkel yang dipilih {}".format(namaB.nama))
    tmp = int(input("Masukan id order = "))
    ord = input("Masukan keluhan = ")
    quantity = int(input("Quantity = "))
    placeOrder(tmp, ord, quantity, usr, namaB)

#pilih manual
elif (inp == 2):
    for i in range(0, len(bengkel)):
        print("{}. {}".format(i + 1, bengkel[i].nama))
    inp = int(input("masukan pilihan bengkel = "))
    print ("\n")
    for i in range(0, len(bengkel)):
        if (inp == bengkel[i].kode):
            print("lokasi bengkel {}".format(bengkel[i].lokasi))


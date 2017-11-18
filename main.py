from classes import *
from function import *
import time
import math

user = [User(1, "Randy", [1, 3]),
        User(2, "Axel", [4, 5]),
        User(3, "Julio", [2, 7])
        ]

bengkel = [Bengkel(1, "Yamaha", [3, 4]),
           Bengkel(2, "Suzuki", [1, 1]),
           Bengkel(3, "Honda", [0, 6])
           ]

order = [Order(1,1,1)]

detail = [Detail(1,1,"ban",10000,1)]

# main program
for i in range(0, len(user)):
    print("{} = {}".format(user[i].id, user[i].nama))
inp = input("pilih user = ")
# inp = input("pilih user (1, 2, 3 )= ")
# if (inp = 1):
#     inp = usrA
# elif (inp = 2):


namaB = cariBengkel(locals()[inp])
# print (namaB)

if (namaB == "Yamaha"):
    pilih = 0
elif (namaB == "Honda"):
    pilih = 1
elif (namaB == "Suzuki"):
    pilih = 2

print("Bengkel yang dipilih {}".format(namaB))

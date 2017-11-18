from classes import *
from function import *
import time
import math

# main program
for i in range(0, len(user)):
    print("{} = {}".format(user[i].kode, user[i].nama))
inp = int(input("pilih user = "))

namaB = cariBengkel(user[inp])
# print (namaB)

print("Bengkel yang dipilih {}".format(namaB))

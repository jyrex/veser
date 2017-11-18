from data import *
from function import checkPrice
import time
import math
    
# main program
for i in range(0, len(user)):
    print("{} = {}".format(user[i].kode, user[i].nama))

tmp = int(input("pilih user = "))
tmp = tmp-1
tmp = user[tmp]

print (tmp.nama)

print ("\n1. Service \n2. List Bengkel")
inp = int(input("masukan pilihan = "))

namaB = cariBengkel(user[inp])
# print (namaB)

print("Bengkel yang dipilih {}".format(namaB))

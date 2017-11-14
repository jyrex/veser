slot = 0
bengkel = [["a","a","a"], ["a","a",""], ["","a",""]]
slot = [0, 0 ,0]
for i in range(0, 3):
	for j in range(0, 3):
		if bengkel[i][j] == "":
			slot[i] = slot[i]+1
		else:
			slot[i] = slot[i]
			
	print "bengkel{} ada {} slot kosong".format(i+1, slot[i])

x = "penuh"
while x == "penuh":
	print "bengkel1 = 1 | bengkel2 = 2 | bengkel3 = 3"
	pilih = input("silahkan pilih bengkel yang kosong = ")
	pilih = pilih-1
	if pilih >= 0 and pilih < 3:
		if slot[pilih] == 0:
			print "bengkel penuh pilih yang lain"
		else:
			x = ""
	else:
		print "inputan salah"

for j in range(0, 3):
	if bengkel[pilih][j] == "":
		x = "n"		
		while x == "n":		
			bengkel[pilih][j] = raw_input("masukan keluhan = ")	
			print bengkel[pilih][j]
			x = raw_input("ini keluhan anda(y/n)? ")
			print "keluhan telah masuk ke database"

		print "terima kasih telah menggunakan aplikasi kami"
		break



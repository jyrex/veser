import time

#mendata bengkel mana saja yang kosong
slot = 0
bengkel = [["a","a","a"], ["a","a",""], ["","a",""]]
slot = [0, 0 ,0]
for i in range(0, 3):
	for j in range(0, 3):
		if bengkel[i][j] == "":
			slot[i] = slot[i]+1				#ini mengecek slot kosong dan ditaro di slot[i]

	print("bengkel{} ada {} slot kosong".format(i + 1, slot[i]))	#ini dengan string pengganti {}
	#print ("bengkel", i+1, "ada", slot[i], "slot kosong")		#ini dengan manual
#.format(i+1, slot[i])

#check apakah ada slot kosong pada bengkel tersebut
x = "penuh"
while x == "penuh":							#mengecek ada slot kosong atau tidak
	print ("bengkel 1 = 1 | bengkel 2 = 2 | bengkel 3 = 3")
	pilih = int(input("silahkan pilih bengkel yang kosong = "))
	pilih = pilih-1
	if pilih >= 0 and pilih < 3:
		if slot[pilih] == 0:
			print ("bengkel penuh pilih yang lain")
		else:
			x = ""
	else:
		print ("inputan salah")

#input keluhan
for j in range(0, 3):
	if bengkel[pilih][j] == "":
		x = "n"		
		while x == "n":		
			bengkel[pilih][j] = input("masukan keluhan = ")	
			print (bengkel[pilih][j])
			x = input("ini keluhan anda(y/n)? ")
			print ("keluhan telah masuk ke database")
		
		#countdown waktu service 
		num = len(bengkel[pilih][j])/20+3
		num = int(num)				
		while (num >= 0):
			print ("sisa waktu {} detik".format(num))
			time.sleep(num)
			num -= 1
			'''
			# Try to convert it to a float
			try:
			    num = float(num)
			except ValueError:
			    print('Please enter in a number.\n')
			    continue
		 	

			# Run our time.sleep() command,
			# and show the before and after time
			print('Before: %s' % time.ctime())
			time.sleep(num)
			print('After: %s\n' % time.ctime())
			'''
			
		print ("terima kasih telah menggunakan aplikasi kami")
		break


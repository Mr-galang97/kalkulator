#logo
print("=======================================")
print("Author : muhammad saiful galang")
print("wWhatsApp : 082146685361")
print("github : https://github.com/Mr-galang97")
print("=======================================")

print("============================")
print("1. penambahan ")
print("2. pengurangan ")
print("3. pembagian ")
print("4. perkalian ")
print("============================")

pilih = input("Masukkan pilihan anda : ")
if pilih == 1:
      print
      angka_1 = input("Masukkan angka pertama : ")
      angka_2 = input("Masukkan angka kedua : ")
      total = angka_1 + angka_2
      print("jadi "+str(angka_1)+" + "+str(angka_2)+" = "+str(total))

elif pilih == 2:
        print
        angka_1 = input("Masukkan angka pertama : ")
        angka_2 = input("Masukkan angka kedua : ")
        total = angka_1 + angka_2
        print("jadi "+str(angka_1)+" - "+str(angka_2)+" = "+str(total))

elif pilih == 3:
        print
        angka_1 = input("Masukkan angka pertama : ")
        angka_2 = input("Masukkan angka kedua : ")
        total = angka_1 + angka_2
        print("jadi "+str(angka_1)+" bagi "+str(angka_2)+" = "+str(total))

elif pilih == 4:
        print
        angka_1 = input("Masukkan angka pertama : ")
        angka_2 = input("Masukkan angka kedua : ")
        total = angka_1 + angka_2
        print("jadi "+str(angka_1)+" x "+str(angka_2)+" = "+str(total))

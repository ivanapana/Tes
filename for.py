for i in range (1,11):
    print (i)

a = int(input("Masukkan angka diantara 1-10: "))

while a >=1 and a <=10:
    print (a)
    if a == 5:  
        print("Program dihentikan.")
        break
    a = int(input("Masukkan angka diantara 1-10: (Ketik 5 untuk menghentikan program)"))
    
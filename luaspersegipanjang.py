def hasil (panjang, lebar):
    luas = panjang * lebar
    return luas

p = float(input("Masukkan Panjang Persegi Panjang: "))
l = float(input("Masukkan Lebar Persegi Panjang: "))
s = input("Masukkan satuan: ")

hasill = hasil (p, l)

print (f"Luas persegi panjang adalah {hasill} {s}")
a = int(input("Masukkan nilai ujian anda: "))

if a <=60:
    print (f"Nilai ujian anda adalah {a} masuk dikategori D")
elif a <=79 and a >= 61:
    print (f"Nilai ujian anda adalah {a} masuk dikategori C")
elif a <= 90 and a >= 80:
    print (f"Nilai ujian anda adalah {a} masuk dikategori B")
elif a <= 100 and a >= 91:
    print (f"Nilai ujian anda adalah {a} masuk dikategori A")
else :
    print (f"Tolong masukkan nilai diantara 1-100")
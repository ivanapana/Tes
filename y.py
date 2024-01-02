print ("Suhu Utama: ")
print ("1. Celcius ")
print ("2. Fahrenheit")
print ("3. Reamur")
print ("4. Rankine")
print ("5. Kelvin")

suhu = float(input("Masukkan nilai suhu: "))
namasuhu = int(input("pilih suhu utama 1/2/3/4/5: "))

c1 = 9/5 * suhu + 32
c2 = suhu + 273.15
c3 = 4/5 * suhu
c4 = (suhu + 273.15) * 9/5

f1 = (suhu-32) * 5/9
f2 = (suhu + 459.67) * 5/9
f3 = 4/9 * (suhu - 32)
f4 = suhu + 459.67

k1 = suhu - 273.15
k2 = (suhu * 9/5) - 459.67
k3 =  (suhu-273) * 4/5
k4 = suhu * 9/5

r1 = suhu / (4/5)
r2 = (suhu * 2.25) + 32
r3 = (suhu/(4/5)) + 273.15
r4 = (suhu * 2.25) + 491.67

ra1 = (suhu - 491.67) * 5/9
ra2 = (suhu- 459.67)
ra3 = (suhu * 5/9)
ra4 =(suhu - 491.67) * 4/9

while namasuhu == '1''2''3''4''5':
    if namasuhu == '1':
        print ("Celcius ke ")
        print (f"Fahrenheit = {c1}")
        print (f"Kelvin = {c2}")
        print (f"Reamur = {c3}")
        print (f"Rankine = 1{c4}")

    elif namasuhu == '2':
        print ("Rahrenheit ke ")
        print (f"Celcius = {f1}")
        print (f"Kelvin = {f2}")
        print (f"Reamur = {f3}")
        print (f"Rankine = {f4}")

    elif namasuhu == '3':
        print ("Reamur ke ")
        print (f"Celcius= {r1}")    
        print (f"Fahrenheit= {r2}")
        print (f"Kelvin= {r3}")
        print (f"Rankine= {r4}")

    elif namasuhu == '4':
        print ("Rankine ke ")
        print (f"Celcius = {ra1}")
        print (f"Fahrenheit = {ra2}")
        print (f"Kelvin = {ra3}")
        print (f"Reamur = {ra4}")

    elif namasuhu == '5':
        print ("Kelvin ke ")
        print (f"Celcius = {k1}")
        print (f"Fahrenheit = {k2}")
        print (f"Reamur = {k3}")
        print (f"Rankine= {k4}")

    else :
        print ("masukkan angka diantara 1-5")
        namasuhu = int(input("pilih suhu utama 1/2/3/4/5: "))




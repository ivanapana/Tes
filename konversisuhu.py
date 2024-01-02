print ("suhu utama: ")
print ("1. celcius ")
print ("2. fahrenheit")
print ("3. reamur")
print ("4. rankine")
print ("5. kelvin")

suhu = float(input("Masukkan nilai suhu= "))
namasuhu = input("pilih suhu utama 1/2/3/4/5= ")

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

if namasuhu == '1':
    print ("celcius ke ")
    print (f"fahrenheit = {c1}")
    print (f"kelvin = {c2}")
    print (f"reamur = {c3}")
    print (f"rankine = 1{c4}")

elif namasuhu == '2':
    print ("fahrenheit ke ")
    print (f"celcius = {f1}")
    print (f"kelvin = {f2}")
    print (f"reamur = {f3}")
    print (f"rankine = {f4}")

elif namasuhu == '3':
    print ("reamur ke ")
    print (f"celcius= {r1}")    
    print (f"fahrenheit= {r2}")
    print (f"kelvin= {r3}")
    print (f"rankine= {r4}")

elif namasuhu == '4':
    print ("rankine ke ")
    print (f"celcius = {ra1}")
    print (f"fahrenheit = {ra2}")
    print (f"kelvin = {ra3}")
    print (f"reamur = {ra4}")

elif namasuhu == '5':
    print ("kelvin ke ")
    print (f"celcius = {k1}")
    print (f"fahrenheit = {k2}")
    print (f"reamur = {k3}")
    print (f"rankine= {k4}")

else :
    print ("masukkan angka diantara 1-5")
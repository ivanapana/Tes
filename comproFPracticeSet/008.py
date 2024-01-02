# Import library os untuk mengakses file
import os 

# Buka file data.txt dengan mode read
f = open ("data.txt", "r")

# Bagi isi file menjadi kata-kata
data = f.read()

# Hitung jumlah kata
words = data.split()

# Tampilkan jumlah kata
count = len (words)

# Tutup file
print ("Jumlah kata: ", count)

f.close()


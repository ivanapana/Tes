# Import library os untuk mengakses file
import os

# Buka file data.txt dengan mode read
f = open ("data.txt", "r")

# Baca setiap baris dan file
for line in f:
    # Tampilkan baris ke layar
    print (line)

# Tutup file
f.close()
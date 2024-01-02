# Import library os untuk mengakses file
import os

# Coba buka file data.txt
try:
    f = open("data.txt", "r")

    # Baca isi file
    data = f.read()

    # Tampilkan isi file ke layar
    print (data)

# Jika file tidak ditemukan, tampilkan pesam
except FileNotFoundError:
    print("File tidak ditemukan")
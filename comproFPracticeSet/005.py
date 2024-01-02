# Import library os untuk mengakses
import os

# Buka file data.txt dengan mode read
with open ("data.txt", "r") as file:
    # Baca isi file
    data = file.read()

    # Tampilkan isi file ke layar
    print (data)
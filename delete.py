import os 

file = "data.txt"

if os.path.isfile(file):
    os.remove(file)
    print(f"{file} berhasil dihapus")
else:
    print(f"{file} tidak ditemukan")
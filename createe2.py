file = open("data.txt", "r")
#buat file yang mempunyai method baca file/ .read()
content = file.read()
#cetak file
print(content)
#tutup file
file.close()
import numpy as np

dataBarang = np.dtype([
    ('NamaBarang', 'U30'),
    ('KodeBarang', 'U15'),
    ('Jumlah', 'i4'),
    ('HargaPerUnit', 'f8')
    #Total Nilai Inventaris  = Jumlah * HargaPerUnit  (tiap barang)
])

# Input
n = int(input("Jumlah barang: "))

barang = np.zeros(n, dtype = dataBarang)

for i in range(n):
    print("=== Data Barang Ke- ", i+1, "===")
    barang[i]['NamaBarang'] = input("Nama Barang: ")
    barang[i]['KodeBarang'] = input("Kode Barang: ")
    barang[i]['Jumlah'] = int(input("Jumlah: "))
    barang[i]['HargaPerUnit'] = float(input("Harga Per Unit: "))


for brg in barang:
    nilaiInventaris = brg['Jumlah'] * brg['HargaPerUnit']
    print(brg['NamaBarang'], " | ", brg['KodeBarang'], " | ", brg['Jumlah'], " | ", brg['HargaPerUnit'], " | Total Nilai: ", nilaiInventaris)


# Pencarian
cari = input("Cari Barang: ")
hasil = barang[(barang['NamaBarang'] == cari) | (barang['KodeBarang'] == cari)]

if len(hasil) > 0:
    print("=== DATA DITEMUKAN ===")
    for h in hasil:
        print(h['NamaBarang'], " | ", h['KodeBarang'], " | ", h['Jumlah'], " | ", h['HargaPerUnit'], " | Total Nilai", h['Jumlah'] * h['HargaPerUnit'])
else:
    print("Barang tidak ditemukan")
import numpy as np

dataMahasiswa = np.dtype([
    ('Nama', 'U30'),
    ('NIM', 'U15'),
    ('Nilai', 'f4'),
    ('TahunMasuk', 'i4')
])

# Input
n = int(input("Jumlah mahasiswa: "))

mahasiswa = np.zeros(n, dtype = dataMahasiswa)

for i in range(n):
    print("=== Data Mahasiswa Ke " , i+1, " ===")
    mahasiswa[i]['Nama'] = input("Nama : ")
    mahasiswa[i]['NIM'] = input("NIM : ")
    mahasiswa[i]['Nilai'] = float(input("Nilai : "))
    mahasiswa[i]['TahunMasuk'] = int(input("Tahun Masuk : "))

for mhs in mahasiswa:
    print("Nama: ", mhs['Nama'] , ", NIM: ", mhs['NIM'], ", Nilai: ", mhs['Nilai'], ", Tahun Masuk: ", mhs['TahunMasuk'])


# Nilai
semuaNilai = mahasiswa['Nilai']
tertinggi = np.max(semuaNilai)
terendah = np.min(semuaNilai)
rataRata = np.mean(semuaNilai)

print("Nilai Tertinggi: ", tertinggi)
print("Nilai Terendah: ", terendah)
print("Rata-Rata: ", rataRata)

# Pencarian
cari = input("Cari Mahasiswa: ")
hasil = mahasiswa[(mahasiswa['Nama'] == cari) | (mahasiswa['NIM'] == cari)]

if len(hasil) > 0:
    print("=== DATA DITEMUKAN ===")
    for h in hasil:
            print("Nama: ", h['Nama'] , ", NIM: ", h['NIM'], ", Nilai: ", h['Nilai'], ", Tahun Masuk: ", h['TahunMasuk'])
else:
     print("Data tidak ditemukan")



     
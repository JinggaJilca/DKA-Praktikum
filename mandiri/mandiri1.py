# NAMA : JINGGA JIL CARISSA
# NIM : 103072400121
# IF 04-03

# NOMOR 1
nama = input("Masukkan nama mahasiswa           : ") #Variabel nama akan menerima input string
tugas = int(input("Masukkan nilai tugas       : ")) #Variabel tugas menerima input int
uts = int(input("Masukkan nilai UTS           : ")) #Variabel uts menerima input int
uas = int(input("Masukkan nilai UAS           : ")) #Variabel uas menerima input int

print()

#Mencetak semua input yang telah dilakukan sebelumnya
print("Nama Mahasiswa   : ", nama)
print("Nilai Tugas      : ", tugas)
print("Nilai UTS        : ", uts)
print("Nilai UAS        : ", uas)

print("---------------------------")
#Kalkulasi nilai akhir
nilaiAKhir = ((tugas * 0.20) + (uts * 0.35) + (uas * 0.45))
# Mencetak nilai akhir
print("Nilai Akhir ", nama , " :", f"{nilaiAKhir:.2f}") #format agar 2 angka dibelakang koma



# NOMOR 2
print()
celsius = float(input("Masukkan suhu Celsius: ")) #Menerima input celcius
fahrenheit = (celsius * 9/5) + 32 #Menghitung konversi celcius -> fahrenheit
kelvin = celsius + 273.15 #Menghitung konversi celsius -> kelvin

print(f"{celsius:.1f} °C = {fahrenheit:.2f} °F = {kelvin:.2f} K")
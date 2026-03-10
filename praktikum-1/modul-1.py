# ARIMATIKA
a = 2 + 2
b = 3* 2
c = 3 / 2
d  = 3 // 2 #Pembagian int
e = 8 / 3

print(c)
print(d)

#STRING
str1 = "Praktikum DKA"
str2 = "Informatika"
str1_2 = str1 + " " + str2
print(str1_2)

perulanganstr1 = str1 * 3
print(perulanganstr1)

# CHAR
char = 'DKA'
firstChar = char[0] #Mengambil karakter paling awal
lastChar = char[2]
print(firstChar + " " + lastChar)

char1 = "Praktikum Kum Kum"
sliced = char1[5:8]
print(sliced)

print(len(char1)) #Hitung panjang karakter
print(char1.upper())
print(char1.lower())

spasiBerlebih = "          Bambang Sunandang"
print(spasiBerlebih.strip())


str3 = "Jumlah pejabat"
replaceStr3 = str3.replace("pejabat", "Mahasiswa")
print(replaceStr3)


#LIST
listAngka = [1,2,3]
#0 -> index awal | -1 -> index terakhir
print(listAngka[-1])


listKata = ["Jingga", "Jil", "Carissa"]
print(listKata)

listCampur = [5, "Jumlahnya", ["ini adalah", "list"]]
print(listCampur)

listArray = [1,5,7, "Praktikum", True]
elm1 = listArray[0]
elm2 = listArray[-1]
elm3 = listArray[-2]
print(elm1)
print(elm2)
print(elm3)

#LIST COMPHERENSION
listPangkat = [a**2 for a in range(15)]
print(listPangkat)

#Dengan kondisi
perulanganKondisi = [x for x in range(20) if x % 2 == 0]
print(perulanganKondisi)

#Perulangan string
buahBuahan = ["Banana", "Anggur" , "Melon"]
upperBuah = [buah.upper() for buah in buahBuahan]
print(upperBuah)

#DICTIONARY
mahasiswa = {
    "nama" : "Jingga",
    "nim" : 1023123,
    "IPK" : 5.0,
    "Prodi" : "IF"
}
print(mahasiswa["nama"])

#Menambahkan nilai baru
mahasiswa["bulan lahir"] = "Januari"
print(mahasiswa)

#Mengubah nilai
mahasiswa["nama"] = "Bambang Sunandag"
print(mahasiswa)

#Menghapus nilai
del mahasiswa["bulan lahir"]
print("Setelah penghapusan = ", mahasiswa)

#Akses keys dan value list
kunciMahasiswa = mahasiswa.keys()
valueMahasiswa = mahasiswa.values()
print(kunciMahasiswa)
print(valueMahasiswa)

for key, value in mahasiswa.items():
    print(key, value)

if "nama" in mahasiswa:
    print("Kunci nama ditemukan")
else:
    print("Kunci nama tidak ditemukan")


#DATA SET
setData = set()
setData = {1,5,9, "APPL", 3.15}
setData.add("Banana")
setData.remove("APPL")
print(setData)

setData2 = {3,4,5}
unionSetData = setData | setData2 #Penggabungan tanpa duplikasi
print(unionSetData)

setData3 = setData & setData2 #Menemukan yg ada di kedua set
print(setData3)

setData4 = setData - setData2 #Menghapus yg sama
print(setData4)

#Memeriksa isi set
if 3.15 in setData:
    print("ditemukan")
else:
    print("tidak ditemukan")


print(len(setData))


#BOOLEAN
x = 1
y = 2
print(x < y)
print(x == y)

hujan = False
if hujan:
    print("Pake hujan")
else:
    print("Ayo nyawit")


#INPUT
nama = input("Masukkan nama anda: ")
print("Hello", nama)


umur = int(input("Masukkan angka: "))
print("Umur %s adalah %d" % (nama, umur))
# %s : digunakan untuk menyisipkan string 
# %d : digunakan untuk menyisipkan integer 
# %f : digunakan untuk menyisipkan float 
print(f"nama anda adalah {nama} umur anda {umur}")

#RANGE
numbers = list(range(10))
print(numbers)


fruits = ["apple", "orange", "tomato", "papaya", "pear"] 
for i in range(0, len(fruits), 2) : 
            #awal , panjang, stop
    print(fruits[i])


# PERCABANGAN
x = 8 
 
if x < 5 : 
    print("x kurang dari 5") 
elif x < 7 : 
    print("x kurang dari 7") 
elif x < 9 : 
    print("x kurang dari 9") 
else : 
    print("x lebih besar atau sama dengan 7") 
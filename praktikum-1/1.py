def isKabisat(tahun):
    if(tahun % 400 == 0) | (tahun % 4 == 0 & tahun % 100 != 0):
        hasil = True
    else:
        hasil = False
    return hasil

tahun = int(input("Masukkan tahun: "))
print(isKabisat(tahun))


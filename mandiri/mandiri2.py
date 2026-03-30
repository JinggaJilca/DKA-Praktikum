import numpy as np

# ======= NOMOR 1
def menuMahasiswa():

    while True: #Bagian ini akan selalu dijalankan
        print("\n=== SELAMAT DATANG ===")
        print("DAFTAR MENU: ")
        print("(1) Input Data Mahasiswa")
        print("(2) Tampilkan Array Nilai")
        print("(3) Tampilkan Nilai Akhir")
        print("(4) Analisis Nilai Kelas")
        print("(5) Tampilkan 3 Nilai Akhir Tertinggi")
        print("(6) Cari Mahasiswa")
        print("(7) Update Data Mahasiswa")
        print("(8) Hapus Mahasiswa")
        print("(0) Keluar")

        userInput = int(input("\nMasukkan pilihan: ")) #Menerima input menu interaktif

        if userInput == 1: #Masuk ke menu 1
            n = int(input("Jumlah Mahasiswa: "))

            namaMahasiswa = []  # Membuat array

            # Membentuk ulang array 2D menjadi n baris dan 4 kolom dengan struktur
            nilaiMahasiswa = np.zeros((n, 4))
                # Kolom 0 : nilai tugas
                # Kolom 1 : nilai UTS
                # Kolom 2 : nilai UAS
                # kolom 3 : nilai Akhir
                
            for i in range(n): #Menjalankan perulangan sebanyak n
                print(f"\n=== Data Mahasiswa Ke-{i + 1} ===")

                # Menyimpan nama ke List menggunakan .append()
                nama = input("Nama : ")
                namaMahasiswa.append(nama)

                # Menyimpan nilai ke Array 2D berdasarkan baris ke-i
                nilaiMahasiswa[i, 0] = float(
                    input("Nilai Tugas : "))  # Kolom 0
                nilaiMahasiswa[i, 1] = float(
                    input("Nilai UTS   : "))  # Kolom 1
                nilaiMahasiswa[i, 2] = float(
                    input("Nilai UAS   : "))  # Kolom 2

                # Menghitung Nilai Akhir dan simpan di Kolom 3
                nilaiMahasiswa[i, 3] = (0.3 * nilaiMahasiswa[i, 0]) + (
                    0.3 * nilaiMahasiswa[i, 1]) + (0.4 * nilaiMahasiswa[i, 2])

            print("\nData berhasil disimpan!")

        elif userInput == 2: #Masuk ke menu 2
            if len(namaMahasiswa) == 0: #Jika isi array kosong maka akan menampilkan pesan
                print("\nData masih kosong! Silakan input data terlebih dahulu.")
            else:
                print("\n=== DAFTAR NILAI MAHASISWA ===")
                #Menjalankan perulangan sebanyak jumlah mahasiswa
                for i in range(len(namaMahasiswa)):
                    #Mencetak isi array bedasarkan index i
                    print(f"{i+1}. Nama        : {namaMahasiswa[i]}")
                    print(f"   Nilai Tugas : {nilaiMahasiswa[i, 0]}")
                    print(f"   Nilai UTS   : {nilaiMahasiswa[i, 1]}")
                    print(f"   Nilai UAS   : {nilaiMahasiswa[i, 2]}")
                    print(f"   Nilai Akhir : {nilaiMahasiswa[i, 3]}")

        elif userInput == 3: #Masuk ke menu 3
            if len(namaMahasiswa) == 0: #Jika isi array kosong maka akan menampilkan pesan
                print("\nData masih kosong!")
            else:
                print("\n=== DAFTAR NILAI AKHIR MAHASISWA ===")
                #Menjalankan perulangan sebanyak jumlah mahasiswa
                for i in range(len(namaMahasiswa)):
                    #Mencetak isi array bedasarkan index i
                    print(
                        f"{i+1}. Nama: {namaMahasiswa[i]} | Nilai Akhir: {nilaiMahasiswa[i, 3]:.2f}") #Nilai akhir dicetak 2 angka dibelakang koma

        elif userInput == 4:
            if len(namaMahasiswa) == 0: #Jika isi array kosong maka akan menampilkan pesan
                print("\nData masih kosong!")
            else:
                print("\n=== ANALISIS NILAI KELAS ===")
                # Mengambil seluruh baris (:) khusus pada kolom ke-3 (Nilai Akhir)
                nilaiAkhir = nilaiMahasiswa[:, 3]

                #Mendapatkan rata-rata dan median dari bawaan numpy
                rataRata = np.mean(nilaiAkhir)
                medianNilai = np.median(nilaiAkhir)

                #Mencetak hasil dengan 2 angka dibelakang koma
                print(f"Rata-Rata Nilai Akhir : {rataRata:.2f}")
                print(f"Median Nilai Akhir    : {medianNilai:.2f}")
                print("\n--- Daftar Mahasiswa Nilai UAS > Median Nilai Akhir ---")

                cekLolos = False #Untuk validasi apakah ada mahasiswa yang UAS nya melebihi median
                for i in range(len(namaMahasiswa)):
                    # Mengecek kolom ke-2 (UAS) apakah lebih dari median
                    if nilaiMahasiswa[i, 2] > medianNilai:
                        print(
                            f"- {namaMahasiswa[i]} (UAS: {nilaiMahasiswa[i, 2]})")
                        cekLolos = True
                #Jika tetap false maka tidak ada yang nilai UAS melebihi median
                if not cekLolos:
                    print("Tidak ada nilai mahasiswa yang melebihi median")

        elif userInput == 5:
            if len(namaMahasiswa) == 0:
                print("\nData masih kosong!")
            else:
                print("\n=== TOP 3 NILAI AKHIR TERTINGGI ===")
                # np.argsort() untuk mengurutkan indeks dari terkecil-terbesar

                # Mengurutkan indeks dari kecil ke besar berdasarkan Kolom 3 (nilaiAkhir)
                indeks_urut = np.argsort(nilaiMahasiswa[:, 3])

                # Membalik urutannya menjadi descending
                indeks_desc = indeks_urut[::-1]

                # Mengambil 3 teratas
                indeks_top3 = indeks_desc[:3]

                # Mencetak hasil
                posisi = 1
                for idx in indeks_top3:
                    print(
                        f"{posisi}. Nama: {namaMahasiswa[idx]} | Nilai Akhir: {nilaiMahasiswa[idx, 3]:.2f}")
                    posisi += 1

        elif userInput == 6:
            if len(namaMahasiswa) == 0:
                print("\nData masih kosong!")
            else:
                cari = input("\nMasukkan Nama Mahasiswa: ")

                # in untuk mencari apakah keyword ada dalam array
                if cari in namaMahasiswa:
                    # Mendapatkan index nama yg dicari
                    idx = namaMahasiswa.index(cari)

                    print("\n=== DATA DITEMUKAN ===")
                    print(f"Nama        : {namaMahasiswa[idx]}")
                    print(f"Nilai Tugas : {nilaiMahasiswa[idx, 0]}")
                    print(f"Nilai UTS   : {nilaiMahasiswa[idx, 1]}")
                    print(f"Nilai UAS   : {nilaiMahasiswa[idx, 2]}")
                    print(f"Nilai Akhir : {nilaiMahasiswa[idx, 3]}")
                else:
                    print("Mahasiswa tidak ditemukan")

        elif userInput == 7:
            if len(namaMahasiswa) == 0:
                print("\nData masih kosong!")
            else:
                cari = input("\nMasukkan Nama Mahasiswa yang akan diupdate: ")

                if cari in namaMahasiswa:
                    idx = namaMahasiswa.index(cari)

                    print(f"\nUpdate nilai untuk {namaMahasiswa[idx]}:")
                    # Input untuk update nilai baru
                    nilaiMahasiswa[idx, 0] = float(
                        input("Nilai Tugas Baru : "))
                    nilaiMahasiswa[idx, 1] = float(
                        input("Nilai UTS Baru   : "))
                    nilaiMahasiswa[idx, 2] = float(
                        input("Nilai UAS Baru   : "))

                    # Menghitung nilai akhir
                    nilaiMahasiswa[idx, 3] = (0.3 * nilaiMahasiswa[idx, 0]) + (
                        0.3 * nilaiMahasiswa[idx, 1]) + (0.4 * nilaiMahasiswa[idx, 2])
                    print("\nData berhasil diperbarui!")
                else:
                    print("Mahasiswa tidak ditemukan")

        elif userInput == 8:
            if len(namaMahasiswa) == 0:
                print("\nData masih kosong!")
            else:
                cari = input("\nMasukkan Nama Mahasiswa yang akan dihapus: ") #Menerima input nama yang akan dicari

                if cari in namaMahasiswa:
                    idx = namaMahasiswa.index(cari)

                    # pop untuk menghapus isi array bedasarkan index
                    namaMahasiswa.pop(idx)

                    # np.delete() untuk mengapus baris pada array 2D
                    # axis=0 baris, axis=1  kolom.
                    nilaiMahasiswa = np.delete(nilaiMahasiswa, idx, axis=0)

                    print(f"\nData '{cari}' berhasil dihapus!")
                else:
                    print("Mahasiswa tidak ditemukan")

        elif userInput == 0:
            print("\nProgram selesai dijalankan")
            break

        else:
            print("\nPilihan tidak tersedia di menu. Silakan coba lagi.")

# MAIN PROGRAM
menuMahasiswa()

import random
#=== NOMOR 2
namaPelanggan = [] #Membuat array 1D untuk menampung nama pelanggan
def menuBelanja(): #Membuat fungsi untuk mempermudah run
    print("\n=== INPUT DATA ===") #Pesan Menu yg sedang berjalan
    #Menerima input banyak jumlah pelanggan
    n = int(input("Masukkan jumlah pelanggan: "))
    dataBelanja = np.zeros((n, 2)) #Membuat array 2D sebanyak n baris dengan 2 kolom

    #Menjalankan perulangan sebanyak n dengan iterasi i
    for i in range(n):
        print(f"=== Data Pelanggan Ke-{i+1} ===")
        #Input nama
        inputNama = input("Masukkan nama: ")
        namaPelanggan.append(inputNama)

        #Input total dan jumlah transaksi untuk array 2D
        dataBelanja[i, 0] = float(input("Total Belanja       : "))  # Kolom 0
        dataBelanja[i, 1] = float(input("Jumlah Transaksi    : "))  # Kolom 1

        print("\nData Pelanggan berhasil disimpan!\n")

    print("\n=== KODE UNDIAN ===")
    kodeUndian = [] #Membuat list kosong untuk menampung isi kode
    #Menjalankan perulangan sebanyak pelanggan dengan iterasi i
    for i in range(len(namaPelanggan)):
        # Untuk mendapatkan angka acak 4 digit
        angkaAcak = random.randint(1000, 9999)
        #Karena kode harus dilengkapi "UND-" sebelum angka
        kode = f"UND-{angkaAcak}"
        #Memasukkan kode kedalam list
        kodeUndian.append(kode)

        #Mencetak seluruh pelanggan dan kode undiannya
        print(f"{i+1}. {namaPelanggan[i]}, {kodeUndian[i]}")

    print("\nSemua kode undian berhasil dibuat")

    print("\n=== MENAMPILKAN SELURUH DATA ===")
    #Menjalankan perulangan sebanyak pelanggan dengan iterasi i
    for i in range(len(namaPelanggan)):
        #Mencetak semua data bedasarkan index ke i
        print(f"{i+1}.{namaPelanggan[i]}")
        print(f"   Total Belanja    : {dataBelanja[i, 0]}")
        print(f"   Jumlah Transaksi : {dataBelanja[i, 1]}")
        print(f"   Kode Undian      : {kodeUndian[i]}")

    print("\nData berhasil ditampilkan!")

    print("\n=== RATA-RATA TOTAL BELANJA ===")
    #Mendapatkan isi dari array 2D kolom ke 2 (totalBelanja) saja
    totalBelanja = dataBelanja[:, 0]
    #Mendapatkan rata-rata dengan np.mean()
    rataRata = np.mean(totalBelanja)
    print(f"Rata-Rata Total Belanja : {rataRata}")

    print("\n=== DAFTAR PELANGGAN PRIORITAS ===")
    #Membuat list untuk menampung status pelanggan prioritas atau bukan
    isPrioritas = []

    #Menjalankan perulangan sebanyak pelanggan dengan iterasi i
    for i in range(len(namaPelanggan)):
        #Percabangan jika total belanja lebih dari rata-rata maka
        if (dataBelanja[i, 0] > rataRata):
            #Akan mencetak isi data
            print(
                f"{i+1}.{namaPelanggan[i]} (Total Belanja : {dataBelanja[i, 0]})")
            #Memasukkan nilai prioritas ke dalam list berupa boolean
            isPrioritas.append(True)
        else:
            #Jika bukan prioritas maka akan menampung False
            isPrioritas.append(False)


    print("\n=== DAFTAR PESERTA UNDIAN ===")
    isPeserta = [] #Membuat list untuk menampung apakah peserta undian karena syarat peserta = jumlah transaksi >= 3
    #Menjalankan perulangan sebanyak pelanggan dengan iterasi i
    for i in range(len(namaPelanggan)): 
        #Percabangan untuk kolom 2 (jumlahTransaksi) lebih dari atau sama dengan 3 maka
        if (dataBelanja[i, 1] >= 3):
            #Mencetak isi data
            print(
                f"{i+1}.{namaPelanggan[i]} (Jumlah Transaksi : {dataBelanja[i, 1]})")
            #Mengisi list peserta menjadi True yang artinya merupakan peserta
            isPeserta.append(True)
        else:
            #Jika bukan peserta list akan berisi False
            isPeserta.append(False)

    print("\n=== DAFTAR SLOT UNDIAN ===")
    slotUndian = [] #Membuat list untuk menampung slotUndian 
    
        #Menjalankan perulangan sebanyak pelanggan dengan iterasi i
    for i in range(len(namaPelanggan)):
        slot = 0 #Set nilai awal slot = 0
        totalBelanja = dataBelanja[i, 0] #Menampung kolom total belanja bedasarkan index i
        #Mengecek bedasarkan list peserta apakah benar termasuk peserta undian?
        if (isPeserta[i] == True): 
            #Jika benar maka akan mengecek total belanja untuk mendapatkan slot
            if (totalBelanja > 300000):
                slot = 1
            elif ((totalBelanja >= 300000) and (totalBelanja <= 700000)):
                slot = 2
            elif (totalBelanja > 700000):
                slot = 3
        # Mengecek isi list apakah pelanggan ini merupakan prioritas, jika iya maka slot akan bertambah 2
        if (isPrioritas[i]):
            slot += 2

        #Memasukkan slot ke dalam list slot undian
        slotUndian.append(slot)

        #Jika slot lebih dari 1 maka akan ditampilkan datanya
        if slot > 0:
            print(f"{i+1}.{namaPelanggan[i]}, Slot Undian : {slotUndian[i]}")

    print("\n=== 2 PEMENANG ACAK ===")
    kotakUndian = [] #Membuat list untuk menjadi kotak undiannya
    #Menjalankan perulangan sebanyak pelanggan dengan iterasi i
    for i in range(len(namaPelanggan)):
        jumlahSlot = slotUndian[i] #Mendapatkan nilai berapa slot yang didapatkan bedasarkan index
        if jumlahSlot > 0: #Jika jumlah slot > 0 maka akan melakukan perulang
            for j in range(jumlahSlot): #Sebanyak jumlah slot untuk dimasukkan ke kotak undian
                kotakUndian.append(i) #Memasukkan niai index ke dalam kotak undian

    #Memilih otomatis pemenang pertama dengan random.choice()
    pemenangPertama = random.choice(kotakUndian)
    #Memperbarui isi kotak undian agar pemenang pertama tidak masuk ke dalam undian ke-2
    kotakUndianSisa = [
        undian for undian in kotakUndian if undian != pemenangPertama]
    #Memilih otomatis pemenang ke 2
    pemenangKedua = random.choice(kotakUndianSisa)

    #Mencetak daftar pemenang bedasarkan indexnya
    print(f"Pemenang 1 : {namaPelanggan[pemenangPertama]} , Kode Undian : {kodeUndian[pemenangPertama]}")
    print(f"Pemenang 2 : {namaPelanggan[pemenangKedua]} , Kode Undian : {kodeUndian[pemenangKedua]}")

    print("\n=== CARI DATA PELANGGAN BEDASARKAN KODE ===")
    cari = input("Masukkan kode undian: ") #Menerima input kode
    if cari in kodeUndian: #Mengecek apakah dalam array kode undian terdapat keyword yg dicari jika iya
        idx = kodeUndian.index(cari) #Mendapatkan index dari keyword
        # Mencetak data yang ditemukan
        print(f"=== DATA DITEMUKAN ===")
        print(f"Nama                : {namaPelanggan[idx]}")
        print(f"Total Belanja       : {dataBelanja[idx, 0]}")
        print(f"Jumlah Transaksi    : {dataBelanja[idx, 1]}")
        print(f"Kode Undian         : {kodeUndian[idx]}")


# MAIN PROGRAM
# menuBelanja()

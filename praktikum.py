data = {}

def tambah():
    print("Tambah Data")
    nama = input("Nama\t\t: ")
    nim = int(input("NIM\t\t: "))
    tugas = int(input("Nilai Tugas\t: "))
    uts = int(input("Nilai UTS\t: "))
    uas = int(input("Nilai UAS\t: "))
    nilaiakhir = (tugas * 0.3 + uts * 0.35 + uas * 0.35)
    data[nama] = nim, tugas, uts, uas, nilaiakhir


def tampilkan():
    if data.items():
        print("DAFTAR NILAI")
        print("======================================================================================")
        print("|  No  |      NIM      |      NAMA         |    TUGAS   |   UTS   |   UAS   | AKHIR  |")
        print("|======|===============|===================|============|=========|========|========|")
        i = 0
        for a in data.items():
            i += 1
            print(f"| {i:4} | {a[0]:13s} | {a[1][0]:17} | {a[1][1]:10d} |  {a[1][2]:6d} | {a[1][2]:7d} | {a[1][4]:6.2f} | ")
    else:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Daftar Nilai |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("======================================================================================")
        print("|  No  |      Nama     |      NIM      |   TUGAS  |   UTS   |   UAS   | Nilai Akhir  |")
        print("======================================================================================")
        print("|      |               |             Tidak Ada Data         |         |                |")
    print("==========================================================================================")


def hapus():
    print("Hapus Data Nilai Mahasiswa")
    nama = input(" Masukan Nama\t:")
    if nama in data.keys():
        del data[nama]
        print()
        print("=================================")
        print("===| BERHASIL MENGHAPUS DATA |===")
        print("=================================")
    else:
        print("Data {0} tidak ada".format(nama))
        
def cari():
    print("===================================")
    print("===| Cari Data Nilai Mahasiswa |===")
    print("===================================")
    nama = input(" Masukan Nama: ")
    if nama in data.keys():
        print("\n")
        print("DAFTAR NILAI")
        print("==================================================================")
        print("NAMA     NIM  TUGAS  UTS UAS NILAI AKHIR")
        print("| {0} |     {1}    | ".format(nama, data[nama]))
        print("==================================================================")
    else:
        print("Datanya {0} tidak ada ".format(nama))


def ubah():
    print("===================================")
    print("===| Edit Data Nilai Mahasiswa |===")
    print("===================================")
    nama = input("Masukan Nama\t\t: ")
    if nama in data.keys():
        nim = input("NIM baru\t\t\t: ")
        tugas = int(input("Nilai Tugas Baru\t: "))
        uts = int(input("Nilai UTS Baru\t\t: "))
        uas = int(input("Nilai UAS Baru\t\t: "))
        nilaiakhir = (tugas * 30 / 100 + uts * 35 / 100 + uas * 35 / 100)
        data[nama] = nim, tugas, uts, uas, nilaiakhir
        print()
        print("BERHASIL MENGUBAH DATA")
        print("======================")
    else:
        print("Data nilai {0} tidak ada ".format(nama))
while True:
    print("\n=======Program Daftar Nilai=======")
    pil = input("(T)ambah, (U)bah, (H)apus, (L)ihat,(C)ari, (K)eluar: ")
    if pil.lower() == "l":
        tampilkan()
    elif pil.lower() == "t":
        tambah()
    elif pil.lower() == "u":
        ubah()
    elif pil.lower() == "h":
        hapus()
    elif pil.lower() == "c":
        cari()
    elif pil.lower() == "k":
        print()
        print("====== KELUAR DARI PROGRAM ======")
        break
    else:
        print("\nAnda memasukkan pilihan yang salah")
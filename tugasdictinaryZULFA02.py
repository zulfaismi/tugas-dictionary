kontak = {}

def tambah_kontak(nama,nomor):
    if nama in kontak:
        print(f"kontak dengan nama{nama} sudah ada.")
    else:
            kontak[nama] = nomor
            print(f"{nama} berhasil ditambahkan.")

def hapus_kontak(nama):
    if nama in kontak:
        del kontak[nama]
        print(f"kontak{nama} berhasil dihapus.")
    else:
        print(f"kontak dengan nama{nama} tidak ditemukan.")

    def cari_kontak(nama):
        if nama in kontak:
            print(f"nomor telepon{nama}: {kontak[nama]}")
        else:
            print(f"kontak dengan nama{nama} tidak ditemukan.")

def tampilkan_kontak():
    if kontak:
        print("daftar kontak:")
        for nama, nomor in kontak.items():
            print(f"{nama}:{nomor}")
    else:
        print("tidak ada kontak yang tersimpan.")

while True:
    print("\n menu:")
    print("1. tambah kontak")
    print("2. hapus kontak")
    print("3. cari kontak")
    print("4. tampilkan semua kontak")
    print("5. keluar")

    pilihan = input("pilih menu (1-5):")

    if pilihan =="1":
        nama = input("masukkan nama:")
        nomor = input("masukkan nomor telepon:")
        tambah_kontak(nama,nomor)
    elif pilihan == "2":
        nama = input("masukkan nama yang ingin dihapus:")
        hapus_kontak(nama)
    elif pilihan == "3":
         nama = input("masukkan nama yang ingin dicari:")
         cari_kontak(nama)
    elif pilihan == "4":
         tampilkan_kontak()
    elif pilihan == "5":
        print("pilihan tidak valid. silahkan coba agi.")
        break
    else:
        print("pilihan tidak valid. silahkan coba lagi.")
            

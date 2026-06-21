from data import baca_data_dari_csv
from kodenya import tambah_pasien, tampilkan_semua, panggil_pasien
from kodenya import ubah_pasien, hapus_pasien, menu_cari, menu_urut

def tampilkan_menu():
    print("""
ANTRIAN RUMAH SAKIT
1. Daftar Pasien Baru
2. Tampilkan Semua Antrean
3. Panggil Pasien (Layani)
4. Cari Pasien
5. Urutkan Data
6. Ubah Data Pasien
7. Hapus Data Pasien
0. Keluar

    """)

def main():
    antrean = baca_data_dari_csv()

    while True:
        tampilkan_menu()
        pilih = input("Pilih Menu: ")
        if pilih == '1':
            antrean = tambah_pasien(antrean)
        elif pilih == '2':
            tampilkan_semua(antrean)
        elif pilih == '3':
            antrean = panggil_pasien(antrean)
        elif pilih == '4':
            menu_cari()
        elif pilih == '5':
            menu_urut(antrean)
        elif pilih == '6':
            antrean = ubah_pasien(antrean)
        elif pilih == '7':
            antrean = hapus_pasien(antrean)
        elif pilih == '0':
            print("Data tersimpan")
            break
        else:
            print("Coba lagi")

if __name__ == "__main__":
    main()

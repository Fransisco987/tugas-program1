from datetime import datetime
from struktur import peta_pasien
from data import simpan_data_ke_csv
from algo import cari_pasien, urutkan_pasien



'''fitur tambah pasien'''
def tambah_pasien(antrean):
    print("\n--- DAFTAR PASIEN BARU ---")
    semua = antrean.ambil_semua()
    if len(semua) == 0:
        nomor = 1
    else:
        nomor = max(int(d['nomor_antrean']) for d in semua) + 1

    rm = input("Nomor Rekam Medis: ").strip().upper()
    if rm == "":
        print("nomornya gaboleh kosong")
        return antrean
    else:
        if rm in peta_pasien:
            print("data udah ada,input yang lain!!!!")
            return antrean
        else:
            nama = input("Nama Lengkap: ")
            jk = input("Jenis Kelamin (L/P): ").upper()
            umur = input("Umur: ")
            keluhan = input("Keluhan: ")
            print("\nPrioritas:")
            print("1. Gawat Darurat")
            print("2. Lanjut Usia / Ibu Hamil")
            print("3. Umum")
            pilih_prioritas = input("Pilih (1/2/3): ")

            if pilih_prioritas == '1':
                prioritas = "1. Gawat Darurat"
            elif pilih_prioritas == '2':
                prioritas = "2. Lanjut Usia / Ibu Hamil"
            else:
                prioritas = "3. Umum"

            waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            '''buat nympen datanya'''
            data_baru = {
                'nomor_antrean': str(nomor), 'rekam_medis': rm, 'nama': nama,
                'jenis_kelamin': jk, 'umur': umur, 'keluhan': keluhan,
                'prioritas': prioritas, 'waktu_daftar': waktu, 'status': 'Menunggu'
            }

            antrean.enqueue(data_baru)
            peta_pasien[rm] = data_baru
            simpan_data_ke_csv(antrean)
            print(f"berhasil: {nomor}")

    return antrean


'''fitur tampilin data'''
def tampilkan_semua(antrean):
    daftar = antrean.ambil_semua()
    
    if len(daftar) == 0:
        print("antrian kosong.")
    else:
        print("\n" + "="*110)
        print(f"{'No':<3} | {'RM':<8} | {'Nama':<15} | {'Prioritas':<18} | {'Status'}")
        print("-"*110)
        for d in daftar:
            print(f"{d['nomor_antrean']:<3} | {d['rekam_medis']:<8} | {d['nama']:<15} | {d['prioritas']:<18} | {d['status']}")
        print("="*110)


'''fitur panggil pasien'''
def panggil_pasien(antrean):
    pasien = antrean.dequeue()
    
    if pasien is None:
        print("tidak ada pasien di antriannya.")
    else:
        pasien['status'] = 'lagi dilayani'
        simpan_data_ke_csv(antrean)
        print(f"\npanggilan:nomor {pasien['nomor_antrean']} - {pasien['nama']}")
        print(f"masuk keruang pemeriksaan.")
    
    return antrean


'''fitur ngubah data pasiennya'''
def ubah_pasien(antrean):
    rm = input("Masukkan Nomor Rekam Medis: ").strip().upper()

    if rm not in peta_pasien:
        print("Data TIDAK DITEMUKAN!")
    else:
        data_lama = peta_pasien[rm]
        print(f"\nData Lama: {data_lama['nama']}, Umur: {data_lama['umur']}")

        nama_baru = input("Nama Baru (kosongkan jika sama): ")
        umur_baru = input("Umur Baru (kosongkan jika sama): ")
        if nama_baru != "":
            data_lama['nama'] = nama_baru
        if umur_baru != "":
            data_lama['umur'] = umur_baru

        simpan_data_ke_csv(antrean)
        print("Data berhasil diubah.")
    
    return antrean

'''menghapus data pasien'''
def hapus_pasien(antrean):
    rm = input("Masukkan Nomor RM yang mau dihapus: ").strip().upper()
    daftar_baru = [d for d in antrean.ambil_semua() if d['rekam_medis'] != rm]

    if rm in peta_pasien:
        antrean.muat_data(daftar_baru)
        del peta_pasien[rm]
        simpan_data_ke_csv(antrean)
        print("Data dihapus.")
    else:
        print("Tidak ditemukan.")
    
    return antrean

'''cari pasien'''
def menu_cari():
    kata = input("Cari Nama Pasien: ")
    hasil = cari_pasien('nama', kata)
    
    if len(hasil) == 0:
        print("Tidak ada yang cocok.")
    else:
        for h in hasil:
            print(h)

def menu_urut(antrean):
    print("\n1. Urut Nomor Antrean")
    print("2. Urut Nama Pasien")
    pilih = input("Pilih: ")

    if pilih == '1':
        daftar_urut = urutkan_pasien(antrean.ambil_semua(), 'nomor_antrean')
    elif pilih == '2':
        daftar_urut = urutkan_pasien(antrean.ambil_semua(), 'nama')
    else:
        print(" Pilihan salah.")
        return

    antrean.muat_data(daftar_urut)
    tampilkan_semua(antrean)
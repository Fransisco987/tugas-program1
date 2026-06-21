import csv
from struktur import Queue, peta_pasien

NAMA_FILE = 'data.csv'

'''ini baca data'''
def baca_data_dari_csv():
    antrean = Queue()
    daftar_sementara = []
    try:
        with open(NAMA_FILE, 'r', encoding='utf-8') as f:
            baca = csv.DictReader(f)
            for baris in baca:
                daftar_sementara.append(baris)
                peta_pasien[baris['rekam_medis']] = baris 
        antrean.muat_data(daftar_sementara)
    except:
        antrean = Queue()
    return antrean


'''ini simpan ke csv'''
def simpan_data_ke_csv(antrean):
    try:
        with open(NAMA_FILE, 'w', newline='', encoding='utf-8') as f:
            tulis = csv.DictWriter(f, fieldnames=[
                'nomor_antrean','rekam_medis','nama','jenis_kelamin',
                'umur','keluhan','prioritas','waktu_daftar','status'
            ])
            tulis.writeheader()
            for d in antrean.ambil_semua():
                tulis.writerow(d)
        return True
    except:
        return False

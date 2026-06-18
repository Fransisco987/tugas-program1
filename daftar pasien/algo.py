from struktur import peta_pasien
'''ini algoritma sercing'''
def cari_pasien(kunci, nilai):
    hasil = []
    if kunci == 'rekam_medis':
        if nilai in peta_pasien:
            hasil.append(peta_pasien[nilai])
        else:
            hasil = []
    else:
        for d in peta_pasien.values():
            if nilai.lower() in d[kunci].lower():
                hasil.append(d)
    return hasil



'''ini algoritma sorting'''
def urutkan_pasien(daftar, kunci, naik=True):
    n = len(daftar)
    for i in range(n):
        for j in range(0, n-i-1):
            
            if kunci == 'nomor_antrean':
                a = int(daftar[j][kunci])
                b = int(daftar[j+1][kunci])
            else:
                a = daftar[j][kunci].lower()
                b = daftar[j+1][kunci].lower()
            if (a > b and naik) or (a < b and not naik):
                daftar[j], daftar[j+1] = daftar[j+1], daftar[j]
    return daftar
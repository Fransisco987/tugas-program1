'''ini antriannya menggunakan queue fifo yang dimana orang masuk duluan itu yang dilayani duluan'''
class Queue:
    def __init__(self):
        self.data = []
    def enqueue(self, item):
        if item['prioritas'] == '1. Gawat Darurat':
            self.data.insert(0, item)  
        elif item['prioritas'] == '2. Lanjut Usia / Ibu Hamil':
            pos = 0
            for d in self.data:
                if d['prioritas'] == '1. Gawat Darurat':
                    pos += 1
                else:
                    break
            self.data.insert(pos, item)
        else:
            self.data.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.data.pop(0)
        else:
            return None
    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
    def ambil_semua(self):
        return self.data
    def muat_data(self, daftar):
        self.data = daftar


'''ini hashmap,cari pasien'''
peta_pasien = {}

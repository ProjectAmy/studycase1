class daftaranggota:

    def __init__(self, listang, jenis):
        self.daftar = listang
        self.jenis = jenis
        self.nama = None

    def tampil(self):

        if self.daftar:
            print("Daftar anggota klub ", self.jenis)
            i = 1
            for anggota in self.daftar:
                print(f"{i}. {anggota}")
                i += 1
        else:
            print(f"belum ada anggota klub {self.jenis}. silahkan menambahka anggota")

    def tambah(self):

        self.nama = input("Masukan nama anggota baru : ")

        if self.nama in self.daftar:
            print(f"{self.nama} sudah masuk ke dalam daftar anggota klub {self.jenis}")
            self.tampil()
        else:
            self.daftar.add(self.nama)
            print(f"{self.nama} telah dimasukan ke dalam anggota klub {self.jenis}")
            self.tampil()

    def hapus(self):

        self.nama = input("Masukan nama yang ingin dihapus : ")

        if self.nama in self.daftar:
            self.daftar.remove(self.nama)
            print(f"{self.nama} sudah dihapus dari anggota klub {self.jenis}")
        else:
            print(f"{self.nama} tidak ada dalam daftar anggota klub {self.jenis}")
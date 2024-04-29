# Membuat daftar belanja dengan format OOP

class daftarbelanja:
    def __init__(self):
        self.daftar = []
        self.item_baru = None
        self.index_hapus = None
        self.dihapus = None

    def tampilkan_daftar(self):

        if self.daftar: # ada isinya atau tidak
            print("\nDaftar Belanja : ")
            for nomor, item in enumerate(self.daftar, start=1):
                print(f"{nomor}. {item}")
        else:
            print("belum ada daftar belanja. Silahkan menambah daftar belanja")

    def tambah_item(self):
        self.item_baru = input("Masukan item baru : ")
        self.daftar.append(self.item_baru)
        print(f"Item {self.item_baru} telah ditambahkan ke dalam daftar")

    def hapus_item(self):

        if not self.daftar:
            print("belum ada daftar belanja. Silahkan isi daftar belanja")
            return

        self.tampilkan_daftar()
        self.index_hapus = int(input("Masukan nomor barang yang mau di hapus : "))

        if 1 <= self.index_hapus <= len(self.daftar):
            self.dihapus = self.daftar.pop(self.index_hapus - 1)
            print(f"item {self.dihapus} telah dihapus dari daftar belanja anda")
        else:
            print("tidak ada nomer tersebut")
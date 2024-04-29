# ini adalah aplikasi daftar belanja

import belanja

if __name__ == '__main__' :

    listbelanja = []
    belanjaku = belanja.daftarbelanja(listbelanja)

    while True:

        print("\nMenu:")
        print("1. Tampilkan Daftar Belanja")
        print("2. Tambah Item ke Daftar Belanja")
        print("3. Hapus Item dari Daftar Belanja")
        print("4. Keluar")
        pilihan = input("Pilih menu (1/2/3/4): ")
        if pilihan == "1":
            belanjaku.tampilkan_daftar()
        elif pilihan == "2":
            belanjaku.tambah_item()
        elif pilihan == "3":
            belanjaku.hapus_item()
        elif pilihan == "4":
            print("Terima kasih! Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
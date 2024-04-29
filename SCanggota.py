# mencoba study case nambah anggota

import anggota

anggotaset = set()
klub = anggota.daftaranggota(anggotaset, "motor")

while True:
    print(f"\nMenu Anggota Klub {klub.jenis}")
    print(f"1. Daftar Anggota Klub {klub.jenis}")
    print(f"2. Tambah Anggota Klub {klub.jenis}")
    print(f"3. Hapus Anggota Klub {klub.jenis}")
    print(f"4. Keluar aplikasi Klub {klub.jenis}")

    pilihan = input("\nPilih menu 1 / 2 / 3 / 4 : ")

    if pilihan == "1" :
        klub.tampil()
    elif pilihan == "2" :
        klub.tambah()
    elif pilihan == "3" :
        klub.hapus()
    elif pilihan == "4" :
        print("Terima kasih! Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
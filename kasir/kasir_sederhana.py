from query import *
from helper import *

import time
import datetime

# senarai
daftar_pembayaran = [
    'Qris',
    'Tunai'
]

# variabel
cacah = 0
total = 0 
keranjang_belanja = []
daftar_id = []

while True:
    # menampilkan menu
    data_menu_dari_query = ambil_menu_db()
    menampilkan_menu(data_menu_dari_query)

    # input
    try:
        id_pilihan = int(input("Masukkan Angka Pada Menu: (0: Selesai):"))

        if id_pilihan == 0:
            if len(keranjang_belanja) > 0:
                total = hitung_total(keranjang_belanja)
                total_setelah_diskon = diskon_harga(total)
                rincian_pembelian(keranjang_belanja, total, cacah, total_setelah_diskon)

                # Logika Pembayaran
                while True:
                    try:
                        if len(keranjang_belanja) > 0:
                            print("===============")
                            print("==Silahkan Melakukan Pembayaran==")
                            print("Pilih Pembayaran Anda:")
                            for pembayaran in range(len(daftar_pembayaran)):
                                print(pembayaran + 1,'.', daftar_pembayaran[pembayaran])

                        pilih_pembayaran = int(input("Masukkan Nomor Pembayaran yang Tertera Pada Daftar:"))
                        waktu_transaksi = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                        if pilih_pembayaran == 1:
                        # sebuah qris dengan timer. namun, dimenit ke 1 sudah muncul apakah pembayaran sudah berhasil?
                            pembayaran_qris(total_setelah_diskon)
                            nama_metode = "QRIS"

                        elif pilih_pembayaran == 2:
                            # membuat fungsi memasukkan duit beserta logikanya
                            pembayaran_tunai(total_setelah_diskon)
                            nama_metode = "Tunai"

                        elif pilih_pembayaran <= 0:
                            print("==Pilihan Pembayaran Tidak Ada, coba lagi==")
                            continue

                        else:
                            print("==Pilihan Pembayaran Tidak Ada, Coba Lagi")

                        struk_buktiPembayaran(total_setelah_diskon, nama_metode, waktu_transaksi)

                        print('selesai')
                        (buktiTransakri_db(nama_metode, total_setelah_diskon))

                        break # Tombol exit untuk keluar dari perulangan

                    # menangani pilih pembayaran > 2 karena piliihannya hanya ada 2
                    except ValueError:
                        print("==Angka Tidak Ada Pada Pilihan, Coba Lagi==")
            # ketika user input 0 maka keranjang langsung kosong
            else:
                print("Keranjang belanja anda kosong")
                print('Selesai')
            break

        # memasukan id menu ke dalam daftar_id
        for menu in data_menu_dari_query:
            daftar_id.append(menu[0])

        # mengecek apakah id yg diketik ada di dalam daftar_id atau tidak
        if id_pilihan not in daftar_id:
            print("==Menu Tidak Ada Pada Pilihan, Coba Lagi==")
            continue # Tombol skip untuk langsung melompat ke awal perulangan berikutnya

        jumlah_makanan = int(input("Masukkan Jumlah Makanan:"))


    # menangani input berupa selain angka
    except ValueError:
        print("==Angka Tidak Ada Pada Pilihan, Coba Lagi==")

    else:
        cacah += 1
        logikaKeranjang_belanja(id_pilihan, jumlah_makanan, keranjang_belanja, data_menu_dari_query)


        
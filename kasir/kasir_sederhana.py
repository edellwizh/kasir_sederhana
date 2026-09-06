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
   
id_pilihan = 0
while id_pilihan != 5:
    # menampilkan menu
    data_menu_dari_query = ambil_menu_db()
    menampilkan_menu(data_menu_dari_query)

    # input
    try:
        id_pilihan = int(input("masukkan angka makanan pada menu:"))

        # logika pilihan
        if id_pilihan == 1:
            harga_satuan = 10000
        elif id_pilihan == 2: 
            harga_satuan = 12000
        elif id_pilihan == 3:
            harga_satuan = 13000
        elif id_pilihan == 4:
            harga_satuan = 15000

        elif id_pilihan == 5:
            if len(keranjang_belanja) > 0:
                diskon = diskon_harga(total)
                rincian_pembelian(keranjang_belanja, total, cacah, diskon)

                # Logika Pembayaran
                while True:
                    try:
                        if len(keranjang_belanja) > 0:
                            print("===============")
                            print("==Silahkan Melakukan Pembayaran==")
                            print("Pilih Pembayaran Anda:")
                            for pembayaran in range(len(daftar_pembayaran)):
                                print(pembayaran + 1,'.', daftar_pembayaran[pembayaran])

                        pilih_pembayaran = int(input("Masukkan nomor pembayaran yang tertera pada daftar:"))
                        waktu_transaksi = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                        if pilih_pembayaran == 1:
                        # sebuah qris dengan timer. namun, dimenit ke 1 sudah muncul apakah pembayaran sudah berhasil?
                            pembayaran_qris(diskon)
                            nama_metode = "QRIS"

                        elif pilih_pembayaran == 2:
                            # membuat fungsi memasukkan duit beserta logikanya
                            pembayaran_tunai(diskon)
                            nama_metode = "Tunai"

                        struk_buktiPembayaran(diskon, nama_metode, waktu_transaksi)

                        print('selesai')
                        (buktiTransakri_db(nama_metode, diskon))

                        break 

                    except ValueError:
                        print("==angka tidak ada pada pilihan, coba lagi==")
            else:
                print("Keranjang belanja anda kosong")
                print('selesai')
                break
        else:
            print('==angka tidak ada pada menu, coba lagi==')
            menampilkan_menu(data_menu_dari_query)

        if id_pilihan != 5:
            jumlah_makanan = int(input("masukkan jumlah makanan:"))

            total_sementara =  jumlah_makanan * harga_satuan
            total += total_sementara
            print("==Total saat ini==:", total_sementara)

    except ValueError:
        print("==angka tidak ada pada menu, coba lagi==")

    else:
        cacah += 1
        # antara mengubah keranjang belanja atau pun gimana nantinya 
        logikaKeranjang_belanja(id_pilihan, jumlah_makanan, keranjang_belanja, data_menu_dari_query)

        print(keranjang_belanja)
        # belum ada pilihan ke 5

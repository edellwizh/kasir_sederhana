import time
import datetime

# Menampung fungsi pada main.py
def menampilkan_menu(data_menu):
    print("kasir sederhana")
    print("===============")
    for menu in data_menu:
        print(menu[0], '.', menu[1], 'Rp',menu[3])

def logikaKeranjang_belanja(nama_menu, jumlah_makanan, keranjang_belanja, daftar_menu, daftar_harga):
    sudah_ada = False
    for cek in range(len(keranjang_belanja)):
        if daftar_menu[nama_menu - 1] == keranjang_belanja[cek][0]:
            keranjang_belanja[cek][2] += jumlah_makanan
            sudah_ada = True
            break
    if sudah_ada == False:
        keranjang_belanja.append([daftar_menu[nama_menu-1], daftar_harga[nama_menu-1], jumlah_makanan]) 

def diskon_harga(total):
    if total >= 100000:
        potongan = total * 0.15
        setelah_diskon = total - potongan
        return setelah_diskon
    else:
        return total

def rincian_pembelian(keranjang_belanja, total, cacah, diskon):
    print("===============")
    print('Rincian Pembelian:')
    print('jumlah memesan:', cacah, 'x')
    print('No|Menu|Harga Satuan|Jumlah = total')
    for i in range(len(keranjang_belanja)):
        nama_menu = keranjang_belanja[i][0]
        harga_satuan = keranjang_belanja[i][1]
        jumlah_makanan = keranjang_belanja[i][2]

        total_sementara =  jumlah_makanan * harga_satuan
        print(i + 1,'.|',nama_menu,"|",harga_satuan,"|",jumlah_makanan,"=",total_sementara)

    print("Total Pembayaran:", total)

    if total >= 100000:
        print("Total Pembayaran Setelah Diskon:", diskon)
        print("==Selamat Anda Mendapatkan Diskon 15%==")

def pembayaran_tunai(diskon):
    while True:
        try:
            jumlah_uang = int(input("Masukkan nominal uang anda: Rp."))

            if jumlah_uang >= diskon:
                kembalian = jumlah_uang - diskon
                print("== Pembayaran Via Tunai ==")
                print("==Pembayaran Anda Telah Berhasil==")
                print("==Silahkan ke kasir untuk memberikan bukti ini==")
                print("Kembalian:", kembalian)
                break

            else:
                print("==Uang yang Anda masukkan kurang dari harga pembelian Anda, coba lagi==")
                continue
        except ValueError:
            print("masukkan angka, coba lagi")

def pembayaran_qris(diskon):
    print("== Pembayaran Via Qris ==")
    print("Total yang harus dibayar: Rp.", diskon)
    print("Silakan scan QR code di bawah ini (Simulasi):")
    print("[  [X] QR CODE SIMULASI [X]  ]")
    print("Menunggu konfirmasi pembayaran...")
    time.sleep(3) 
    
    print("\n== Pembayaran QRIS Berhasil! ==")
    print("Silakan tunjukkan layar ini ke kasir.")

def struk_buktiPembayaran(diskon, nama_metode, waktu_transaksi):
    print("==================================")
    print("       STRUK BUKTI PEMBAYARAN     ")
    print("==================================")
    print("Metode Pembayaran :", nama_metode)
    print("Total Dibayar     : Rp", diskon)
    print("Waktu Transaksi   :", waktu_transaksi)
    print("==================================")
    print("== Tunjukkan bukti ini ke kasir ==")
import time
import datetime

# Menampung fungsi pada main.py
def menampilkan_menu(data_menu):
    print("kasir sederhana")
    print("===============")
    for menu in data_menu:
        print(menu[0], '.', menu[1], 'Rp',menu[3])

def logikaKeranjang_belanja(id_pilihan, jumlah_makanan, keranjang_belanja, data_menu_dari_query):
    # mencari tau id_pilihan yg dipilih itu isinya apa
    for menu in data_menu_dari_query:

        # menangani input jumlah makanan <= 0
        if jumlah_makanan <= 0:
            print("==Jumlah makanan harus lebih dari 0==")
            return # Tombol exit untuk keluar dari fungsi
        
        if id_pilihan == menu[0]:
            nama_menu = menu[1]
            harga = menu[3]
            break
        
    # mengecek apakah id menunya sudah ada di dalam keranjang atau belum
    sudah_ada = False
    for cek in range(len(keranjang_belanja)):
        if id_pilihan == keranjang_belanja[cek][0]:
            keranjang_belanja[cek][3] += jumlah_makanan
            sudah_ada = True
            break
    if sudah_ada == False:
        keranjang_belanja.append([id_pilihan, nama_menu,harga, jumlah_makanan]) 

def hitung_total(keranjang_belanja):
    total = 0
    for item in keranjang_belanja:
        total += item[2] * item[3] # harga * jumlah
    return total

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
        nama_menu = keranjang_belanja[i][1]
        harga_satuan = keranjang_belanja[i][2]
        jumlah_makanan = keranjang_belanja[i][3]

        total_sementara =  jumlah_makanan * harga_satuan
        print(i + 1,'.|',nama_menu,"|",harga_satuan,"|",jumlah_makanan,"=",total_sementara)

    print("Total Pembayaran:", total)

    if total >= 100000:
        print("Total Pembayaran Setelah Diskon:", diskon)
        print("==Selamat Anda Mendapatkan Diskon 15%==")

def pembayaran_tunai(total_setelah_diskon):
    while True:
        try:
            jumlah_uang = int(input("Masukkan Nominal Uang Anda: Rp."))

            if jumlah_uang >= total_setelah_diskon:
                kembalian = jumlah_uang - total_setelah_diskon
                print("== Pembayaran Via Tunai ==")
                print("==Pembayaran Anda Telah Berhasil==")
                print("==Silahkan ke Kasir Untuk Memberikan Bukti Ini==")
                print("Kembalian:", kembalian)
                return kembalian, jumlah_uang

            if jumlah_uang < total_setelah_diskon:
                print("==Uang yang Anda masukkan kurang dari harga pembelian Anda, coba lagi==")
                continue
        except ValueError:
            print("==Masukkan Angka, Coba Lagi==")

def pembayaran_qris(total_setelah_diskon):
    print("== Pembayaran Via Qris ==")
    print("Total yang harus dibayar: Rp.", total_setelah_diskon)
    print("Silakan scan QR code di bawah ini (Simulasi):")
    print("[  [X] QR CODE SIMULASI [X]  ]")
    print("Menunggu konfirmasi pembayaran...")
    time.sleep(3) 
    
    print("\n== Pembayaran QRIS Berhasil! ==")
    print("Silakan tunjukkan layar ini ke kasir.")

def struk_buktiPembayaran(total_setelah_diskon, nama_metode, waktu_transaksi):
    print("==================================")
    print("       STRUK BUKTI PEMBAYARAN     ")
    print("==================================")
    print("Metode Pembayaran :", nama_metode)
    print("Total Dibayar     : Rp", total_setelah_diskon)
    print("Waktu Transaksi   :", waktu_transaksi)
    print("==================================")
    print("== Tunjukkan bukti ini ke kasir ==")
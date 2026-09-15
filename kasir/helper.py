import time

""" 1. fungsi menampilkan_menu berguna untuk menampilkan menu dan harga"""
def menampilkan_menu(data_menu):
    print("===============")
    print("kasir sederhana")
    print("===============")
    for menu in data_menu:
        print(menu[0], '.', menu[1], 'Rp',menu[3])

""" 2. fungsi logikaKeranjang_belanja berguna untuk menjalankan proses dari keranjang belanja
    - for menu in data_menu_dari_query => mengambil data menu dari db kemudian mengambil id nya yg dilanjut untuk menjabarkan nama_menu, harga, dan subtotal nya berapa dari id tersebut.
    
    - for cek in range keranjang_belanja => untuk mengecek apakah id_menu sudah ada di dalam keranjang atau belum. jika sudah ada maka masukkan kedalam id_menu yang lama, jika belum ada tambahkan id_mennu tersebut.
"""
def logikaKeranjang_belanja(id_pilihan, jumlah_pesan, keranjang_belanja, data_menu_dari_query):
    for menu in data_menu_dari_query:
        if jumlah_pesan <= 0:
            print("==Jumlah makanan harus lebih dari 0==")
            return # tombol exit untuk keluar dari fungsi
        
        if id_pilihan == menu[0]:
            nama_menu = menu[1]
            harga_satuan = menu[3]
            subtotal = harga_satuan * jumlah_pesan
            break
        
    sudah_ada = False
    for cek in range(len(keranjang_belanja)):
        if id_pilihan == keranjang_belanja[cek][0]:
            keranjang_belanja[cek][3] += jumlah_pesan
            sudah_ada = True
            break
    if sudah_ada == False:
        keranjang_belanja.append([id_pilihan, nama_menu, harga_satuan, jumlah_pesan, subtotal]) 

""" 3. fungsi hitung_total berguna untuk menghitung total seluruh keranjang belanja dan fungsi ini berjalan dengan mengambil isi dari keranjang belanja seperti indeks ke 2 sebagai harga menu * indeks ke 3 sebagai jumlah satuan.
"""
def hitung_total(keranjang_belanja):
    total = 0
    for item in keranjang_belanja:
        total += item[2] * item[3] 
    return total

""" 4. fungsi diskon_harga berguna untuk memberikan potongan jika total lebih dari yang sudah ditetapkan"""
def diskon_harga(total):
    if total >= 100000:
        potongan = total * 0.15
        setelah_diskon = total - potongan
        return setelah_diskon
    else:
        return total

""" 5. fungsi rincian_pembelian berguna untuk menampilkan seluruh rincian pembelian dengan cara mengambil isi dari keranjang belanja sesuai dengan indeks masing-masing
"""
def rincian_pembelian(keranjang_belanja, total, cacah, diskon):
    print("==================================")
    print("       RINCIAN PEMBELIAN          ")
    print("==================================")
    print('Jumlah Memesan:', cacah, 'x')
    print(' No |Menu |Harga Satuan|Jumlah = total ')
    for i in range(len(keranjang_belanja)):
        nama_menu = keranjang_belanja[i][1]
        harga_satuan = keranjang_belanja[i][2]
        jumlah_pesan = keranjang_belanja[i][3]
        subtotal = keranjang_belanja[i][4]

        print(i + 1,'.|',nama_menu," | ",harga_satuan," | ",jumlah_pesan,"=",subtotal)

    print("Total Pembayaran:", total)

    if total >= 100000:
        print("Total Pembayaran Setelah Diskon:", diskon)
        print("==Selamat Anda Mendapatkan Diskon 15%==")

""" 6. fungsi pembayaran_tunai berguna untuk melakukan proses jika memilih pembayaran secara tunai dan logika nya hanya disuruh untuk memasukan jumlah_uang dan alurnya jika jumlah uang < total pembelian maka akan disuruh coba lagi.
"""
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

""" 6. fungsi pembayaran_qris berguna untuk melakukan proses jika memilih pembayaran secara qris dan logika nya hanya disuruh untuk scan qr simulasi dan setelah 3 detik berjalan maka muncul pembayaran telah berhasil 
"""
def pembayaran_qris(total_setelah_diskon):
    print("== Pembayaran Via Qris ==")
    print("Total yang harus dibayar: Rp.", total_setelah_diskon)
    print("Silakan scan QR code di bawah ini (Simulasi):")
    print("[  [X] QR CODE SIMULASI [X]  ]")
    print("Menunggu konfirmasi pembayaran...")
    time.sleep(3) 
    
    print("\n== Pembayaran QRIS Berhasil! ==")

""" 7. fungsi struk_buktiPembayaran berguna untuk menyimpan seluruh transaksi user ke db dan menunjukkan struk bukti ini ke kasir untuk ditindak lanjuti oleh kasir setelah itu kasir mengecek ke db. apakah transaksi sudah benar-benar di lakukan atau belum.
"""
def struk_buktiPembayaran(total_setelah_diskon, nama_metode, waktu_transaksi):
    print("==================================")
    print("       STRUK BUKTI PEMBAYARAN     ")
    print("==================================")
    print("Metode Pembayaran :", nama_metode)
    print("Total Dibayar     : Rp", total_setelah_diskon)
    print("Waktu Transaksi   :", waktu_transaksi)
    print("==================================")
    print("== Tunjukkan bukti ini ke kasir ==")
# senarai
daftar_menu = ['Mie Rebus',
        'Nasi Goreng',
        'Bubur Ayam',
        'Nasi Campur',
        'Selesai']
daftar_harga = [10000,
         12000,
         13000,
         15000,
         0]
daftar_pembayaran = [
    'Qris',
    'Tunai',
    'Debit'
]

# variabel
cacah = 0
total = 0 
keranjang_belanja = []

# membuat fungsi
def menampilkan_menu(daftar_menu, daftar_harga):
    print("kasir sederhana")
    print("===============")
    for indeks in range(len(daftar_menu)):
        print(indeks + 1,'.', daftar_menu[indeks], '| Rp.', daftar_harga[indeks])

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
                print("==Pembayaran Anda Telah Berhasil==")
                print("==Silahkan ke kasir untuk memberikan bukti ini==")
                print("Kembalian:", kembalian)
                break

            else:
                print("==Uang yang Anda masukkan kurang dari harga pembelian Anda, coba lagi==")
                continue
        except ValueError:
            print("masukkan angka, coba lagi")
    

nama_menu = 0
while nama_menu != 5:
    # menampilkan menu
    menampilkan_menu(daftar_menu, daftar_harga)

    # input
    try:
        nama_menu = int(input("masukkan angka makanan pada menu:"))

        # logika pilihan
        if nama_menu == 1:
            harga_satuan = 10000
        elif nama_menu == 2: 
            harga_satuan = 12000
        elif nama_menu == 3:
            harga_satuan = 13000
        elif nama_menu == 4:
            harga_satuan = 15000

        elif nama_menu == 5:
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

                        if pilih_pembayaran == 1:
                        # sebuah qris dengan timer 3 menit. namun, dimenit ke 1 sudah muncul apakah pembayaran sudah berhasil?
                            print("wait a minute")

                        elif pilih_pembayaran == 2:
                            # membuat fungsi memasukkan duid beserta logikanya
                            pembayaran_tunai(diskon)

                        elif pilih_pembayaran == 3:
                            print("==Silahkan menuju ke kasir untuk melakukan pembayaran==")
                            print("==Jangan lupa untuk foto bukti pembayaran anda==")

                        print('selesai')
                        break # supaya ketika user baru mulai tapi pilih menu 5 langsung selesai

                    except ValueError:
                        print("==angka tidak ada pada pilihan, coba lagi==")
            else:
                print("Keranjang belanja anda kosong")
                print('selesai')
                break
        

        else:
            print('==angka tidak ada pada menu, coba lagi==')
            menampilkan_menu(daftar_harga, daftar_menu)

        if nama_menu != 5:
            jumlah_makanan = int(input("masukkan jumlah makanan:"))

            total_sementara =  jumlah_makanan * harga_satuan
            total += total_sementara
            print("==Total saat ini==:", total_sementara)

    except ValueError:
        print("==angka tidak ada pada menu, coba lagi==")

    else:
        cacah += 1
        logikaKeranjang_belanja(nama_menu, jumlah_makanan, keranjang_belanja, daftar_menu, daftar_harga)

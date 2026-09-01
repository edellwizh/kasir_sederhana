# senarai
daftar_menu = ['mie rebus',
        'nasi goreng',
        'bubur ayam',
        'nasi campur',
        'selesai']
daftar_harga = [10000,
         12000,
         13000,
         15000,
         0]

# variabel
cacah = 0
total = 0 
keranjang_belanja = []

# membuat fungsi
def menampilkan_menu(daftar_menu, daftar_harga):
    print("kasir sederhana")
    print("===============")
    for indeks in range(0, len(daftar_menu)):
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

def rincian_pembelian(keranjang_belanja, total, cacah, logika_diskon):
    print('==================================')
    print('jumlah memesan:', cacah, 'x')
    print('Rincian Pembelian:')
    print('No|Menu|Harga Satuan|Jumlah = total')
    for i in range(len(keranjang_belanja)):
        nama_menu = keranjang_belanja[i][0]
        harga_satuan = keranjang_belanja[i][1]
        jumlah_makanan = keranjang_belanja[i][2]

        total_sementara =  jumlah_makanan * harga_satuan
        print(i + 1,'.|',nama_menu,"|",harga_satuan,"|",jumlah_makanan,"=",total_sementara)

    print("Total Pembayaran:", total)

    if total >= 100000:
        print("Total Pembayaran Setelah Diskon:", logika_diskon)
        print("Selamat Anda Mendapatkan Diskon 15%")

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
            logika_diskon = diskon_harga(total)
            rincian_pembelian(keranjang_belanja, total, cacah, logika_diskon)
            print('selesai')
            break # supaya ketika user baru mulai tapi pencet 5 langsung selesai
        else:
            print('==angka tidak ada pada menu, coba lagi==')
            menampilkan_menu(daftar_harga, daftar_menu)

        if nama_menu != 5:
            jumlah_makanan = int(input("masukkan jumlah makanan:"))

            total_sementara =  jumlah_makanan * harga_satuan
            total += total_sementara
            print("==Total saat ini==:", total_sementara)

    except ValueError:
        print("masukkan angka, coba lagi")

    else:
        cacah += 1
        logikaKeranjang_belanja(nama_menu, jumlah_makanan, keranjang_belanja, daftar_menu, daftar_harga)

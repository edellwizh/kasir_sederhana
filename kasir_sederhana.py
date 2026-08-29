# variabel penampung
cacah = 0 # total berapa kali memesan
total = 0 # jumlah seluruhnya
keranjang_belanja = []  # menyimpan menu, harga, dan jumlah_makanan

# senarai
menu = ['mie rebus',
        'nasi goreng',
        'bubur ayam',
        'nasi campur',
        'selesai']
harga = [10000,
         12000,
         13000,
         15000,
         0]

# memunculkan senarai
while True or pesan_lagi == "y":
    print("kasir sederhana")
    print("===============")
    for indeks in range(0, len(menu)):
        print(indeks + 1,'.', menu[indeks], '| Rp.', harga[indeks])

# input
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
        print('selesai')
        break
    else:
        print('angka tidak ada pada menu, coba lagi')
        continue

    jumlah_makanan = int(input("masukkan jumlah makanan:"))

    total_sementara =  jumlah_makanan * harga_satuan
    print("==Total saat ini==:", total_sementara)

# logika untuk menambahkan isi variabel kosong diatas
    cacah += 1

    # mengecek apakah menu sudah ada atau belum dikeranjang belanja
    sudah_ada = False
    for cek in range(len(keranjang_belanja)):
        if menu[nama_menu - 1] == keranjang_belanja[cek][0]:
            keranjang_belanja[cek][2] += jumlah_makanan
            sudah_ada = True
            break
    if sudah_ada == False:
        keranjang_belanja.append([menu[nama_menu-1], harga[nama_menu-1], jumlah_makanan]) 
        # menggunakan kurung siku karena append hanya menerima satu data didalam senarai jadi kalo menggunakan ini isinya menjadi ['nasi goreng', 2]

    pesan_lagi = input('==apakah masih ingin berbelanja (y/n)==:')
    if pesan_lagi == "n":
        print('==================================')
        print('jumlah memesan:', cacah, 'x')
        
        # print('Total pembayaran: Rp', total)

        print('Rincian Pembelian:')
        print('Menu|Harga Satuan|Jumlah = total')
        for i in range(len(keranjang_belanja)):
            nama_menu = keranjang_belanja[i][0]
            harga_satuan = keranjang_belanja[i][1]
            jumlah_makanan = keranjang_belanja[i][2]

            total_sementara =  jumlah_makanan * harga_satuan
            total += total_sementara
            print(i + 1,'.',nama_menu,"|",harga_satuan,"|",jumlah_makanan,"=",total_sementara)

        print("total seluruhnya:", total)
        break

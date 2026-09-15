from connect import hubungkan_db

import datetime

""" 1. fungsi menyimpan_buktiTransaksi_db berguna untuk menambahkan rincian pembelian user ke dalam tabel transaksi dan detail_transaksi yang ada pada di database. adapun tabel databasenya yaitu:
transaksi:
id_transaksi
metode_pembayaran
total
waktu

detail_transaksi:
id_detail 
id_transaksi - foreign key
id_menu - foreign key
jumlah_pesan
subtotal

kemudian berikut penjelasan dari masing-masing variabel ataupun hal lainnya yang ada didalam fungsi ini:
- db => membuka jalur sambungan antara python ke database.
- cursor => perantar antara python dengan db.
- cursor.execute => untuk membungkus perintah INSERT, SELECT, UPDATE, ataupun DELETE  ke dalam values nya dengan perintah dan values di taro ke dalam sebuah  variabel.
- db.commit => menyimpan perubahan di database.
- cursor.close => menutup perantara antara python dengan db.
- db.close => menutup koneksi antara python dengan db.

setelah itu didalam fungsi ini ada tabel:
1. transaksi => menambahkan metode pembayaran, total dan waktu ke dalam db.
2. detail_transaksi => menambahkan jumlah_pesan, subtotal ke dalam db dengan foreign key id_transaksi dan id_menu yg saling terhubung disetiap tabel. kemudian di bagian ini berjalan dengan cara melakukan perulangan yang berfungsi sebagai membongkar isi dari keranjang belanja dan di masukkan ke database.

fungsi dari variabel values_transaksi dan values_detailTransaksi => menjabarkan isi sebenarnya dari values.
%s, %s, %s => untuk memasukkan bahwa nilai valuesnya ada 3
"""
def menyimpan_buktiTransaksi_db(nama_metode, total_setelah_diskon, keranjang_belanja):
    try:
        db = hubungkan_db()
        cursor = db.cursor()


        # 1. bagian transaksi
        waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_transaksi = "INSERT INTO transaksi (metode_pembayaran, total, waktu) VALUES (%s, %s, %s)"
        values_transaksi = (nama_metode, total_setelah_diskon, waktu)

        cursor.execute(sql_transaksi, values_transaksi)

        # 2. bagian detail_transaksi
        id_transaksi_baru = cursor.lastrowid

        sql_detailTransaksi = "INSERT INTO detail_transaksi (id_transaksi, id_menu, jumlah_pesan, subtotal) VALUES (%s, %s, %s, %s)"

        for item in keranjang_belanja:
            id_menu = item[0]
            jumlah_pesan = item[3]
            subtotal = item[4]

            values_detailTransaksi = (id_transaksi_baru, id_menu, jumlah_pesan, subtotal)
            cursor.execute(sql_detailTransaksi, values_detailTransaksi)

        db.commit()
        cursor.close() 
        db.close() 
        print("Data transaksi berhasil disimpan ke database")

    except Exception as e:
        db.rollback()
        print("== Gagal menyimpan transaksi ke Database! Error:", e)

""" 2. fungsi ambil_menu_db berfungsi sebagai menampilkan tabel dari menu ada apa saja. kemudian yang membedakan fungsi ini dengan fungsi diatas adalah bagian:
- execute => ibaratnya memeberikan pesanan ke pelayan (INSERT, UPDATE, DELETE)
- fetchall => melakukan perintah lanjutan kepelayan (SELECT)

setelah itu, berikut adalah tabel dari 
menu:
id_menu
nama_menu
kategori_menu
harga
"""
def ambil_menu_db():
    db = hubungkan_db()
    cursor = db.cursor()

    sql = "SELECT * FROM menu"
    cursor.execute(sql)

    hasil_menu  = cursor.fetchall() # mengambil hasilnya

    cursor.close()
    db.close

    return hasil_menu
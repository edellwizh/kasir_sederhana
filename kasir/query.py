from connect import hubungkan_db

import datetime

def menyimpan_buktiTransaksi_db(nama_metode, total_setelah_diskon, keranjang_belanja):
    try:
        db = hubungkan_db() # membuka jalur sambungan ke db
        cursor = db.cursor() # perantara antara python dengan db


        # 1. bagian transaksi
        waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_transaksi = "INSERT INTO transaksi (metode_pembayaran, total, waktu) VALUES (%s, %s, %s)"
        values_transaksi = (nama_metode, total_setelah_diskon, waktu) # isi yang sebenarnya dari values pada variabel sql dan kenapa bisa tau bahwa valuesnya adalah ini?? karena cursor.execute

        cursor.execute(sql_transaksi, values_transaksi)

        # 2. bagian detail_transaksi
        id_transaksi_baru = cursor.lastrowid

        sql_detailTransaksi = "INSERT INTO detail_transaksi (id_transaksi, id_menu, jumlah_pesan, subtotal) VALUES (%s, %s, %s, %s)"

        # fungsi perulangan untuk membongkar isi keranjang belanja 
        for item in keranjang_belanja:
            id_menu = item[0]
            jumlah_pesan = item[3]
            subtotal = item[4]

            values_detailTransaksi = (id_transaksi_baru, id_menu, jumlah_pesan, subtotal)
            cursor.execute(sql_detailTransaksi, values_detailTransaksi)

        db.commit() # untuk menyimpan perubahan pada db 
        cursor.close() # menutup perantaranya
        db.close() # menutup koneksi
        print("Data transaksi berhasil disimpan ke database")

    except Exception as e:
        db.rollback()
        print("== Gagal menyimpan transaksi ke Database! Error:", e)

def ambil_menu_db():
    db = hubungkan_db()
    cursor = db.cursor()

    sql = "SELECT * FROM menu"
    cursor.execute(sql) # menjalankan pencarian

    hasil_menu  = cursor.fetchall() # mengambil hasilnya

    # execute => ibaratnya memebrikan pesanan ke pelayan (INSERT, UPDATE, DELETE)
    # fetchall => melakukan perintah lanjutan kepelayan (SELECT)

    cursor.close()
    db.close

    return hasil_menu
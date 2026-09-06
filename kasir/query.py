from connect import hubungkan_db

import time
import datetime

def buktiTransakri_db(nama_metode, diskon):
    db = hubungkan_db() # membuka jalur sambungan ke db
    cursor = db.cursor() # perantara antara python dengan db

    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql = "INSERT INTO transaksi (metode_pembayaran, total, waktu) VALUES (%s, %s, %s)"
    val = (nama_metode, diskon, waktu) # isi yang sebenarnya dari values pada variabel sql dan kenapa bisa tau bahwa valuesnya adalah ini?? karena cursor.execute

    cursor.execute(sql, val)
    db.commit() # untuk menyimpan perubahan pada db 

    cursor.close() # menutup perantaranya
    db.close() # menutup koneksi
    print("[Data transaksi berhasil disimpan ke phpMyAdmin!]")

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
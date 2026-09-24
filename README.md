# 🛒 Aplikasi Kasir Sederhana (CLI & MySQL)

Proyek ini adalah langkah awal saya dalam mempelajari dasar-dasar pemrograman Python menggunakan antarmuka berbasis *Command Line Interface* (CLI). Melalui proyek kasir ini, saya belajar menghubungkan logika program Python dengan database **MySQL (via phpMyAdmin)** untuk mengolah dan menyimpan data transaksi.

Proyek ini menjadi fondasi penting bagi saya untuk terus berkembang dan mendalami Python ke tingkat yang lebih lanjut.

---

## 📌 Hal yang Saya Pelajari di Proyek Ini

- **Dasar Python & CLI:** Mengolah *input* pengguna, manipulasi *list* dan *dictionary*, serta membuat alur program di terminal.
- **Koneksi Database:** Mengintegrasikan Python dengan MySQL menggunakan `mysql-connector-python`.
- **Relasi Tabel Master-Detail:** Menyimpan nota transaksi sekaligus rincian barang belanjaan secara terhubung.
- **Penanganan Error Sederhana:** Menerapkan `try-except` dan `rollback` agar data di database tetap aman saat terjadi kegagalan sistem.

---

## 🛠️ Prasyarat & Alat yang Digunakan

- **Python 3.x**
- **Laragon** (untuk menjalankan Apache & MySQL / phpMyAdmin)
- **Library Python:** `mysql-connector-python`

---

## 🗄️ Struktur Database (`db_kasir`)

Proyek ini menggunakan database `db_kasir` dengan 3 tabel utama:

1. **`menu`** — Menyimpan daftar makanan/minuman dan harganya (`id_menu`, `nama_menu`, `harga`).
2. **`transaksi`** — Menyimpan data nota utama (`id_transaksi`, `metode_pembayaran`, `total`, `waktu`).
3. **`detail_transaksi`** — Menyimpan rincian item belanja per nota (`id_detail_transaksi`, `id_transaksi`, `id_menu`, `jumlah_pesan`, `subtotal`).

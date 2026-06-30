import json

# 1. Load data dari file DataJSON.json yang sudah dibuat terpisah
with open('DataJSON.json') as f:
    data = json.load(f)

# Fungsi untuk menampilkan menu makanan dan minuman
def tampilkan_menu():
    print("\n===============================")
    print("--- Menu Makanan ---")
    for item in data["makanan"]:
        print(f"- {item['nama']}: Rp {item['harga']}")
    
    print("\n--- Menu Minuman ---")
    for item in data["minuman"]:
        print(f"- {item['nama']}: Rp {item['harga']}")
    print("===============================\n")

# Fungsi untuk menghitung total harga berdasarkan nama item
def hitung_total(kategori, nama_item, jumlah):
    if kategori in data:
        for item in data[kategori]:
            if item['nama'].lower() == nama_item.lower():
                return item['harga'] * jumlah
    return 0    

# Fungsi diskon untuk makanan dan minuman
def hitung_diskon(kategori, total):
    if kategori == "makanan" and total >= 50000:
        return total * 0.1 
    elif kategori == "minuman" and total >= 30000:
        return total * 0.05  
    return 0

# Fungsi Kasir (Diberi 'pass' agar tidak menyebabkan IndentationError)
def kasir(kategori, item, jumlah, uang):
    pass

# --- AWAL SIMULASI ---

# Panggil fungsi ini agar daftar menunya muncul di layar!
tampilkan_menu()

kategori_beli = input("Masukkan kategori yang ingin dibeli (makanan/minuman): ").lower()
item_beli = input("Masukkan nama item yang ingin dibeli: ")
jumlah_beli = int(input("Masukkan jumlah yang ingin dibeli: "))

# Hitung total harga untuk item pertama
total_item1 = hitung_total(kategori_beli, item_beli, jumlah_beli)
total_tambahan = 0

# Menggunakan .title() agar jika user ketik 'iya' atau 'Iya' tetap terbaca benar
Klarifikasi = input("\nApakah ingin beli lagi? (Cukup/Iya): ").title()

while Klarifikasi == "Iya":
    kategori_beli_tambahan = input("\nMasukkan kategori tambahan (makanan/minuman): ").lower()
    tambahan_item = input("Masukkan nama item tambahan: ")
    tambahan_jumlah = int(input("Masukkan jumlah tambahan: "))
    
    # Menggunakan += agar total tambahan terus diakumulasikan jika beli berkali-kali
    harga_item_baru = hitung_total(kategori_beli_tambahan, tambahan_item, tambahan_jumlah)
    total_tambahan += harga_item_baru
    
    print(f"-> Berhasil menambahkan {tambahan_jumlah} porsi {tambahan_item} = Rp {harga_item_baru:,}")
    
    # PENTING: Tanyakan ulang di sini agar perulangan bisa berhenti saat user ketik 'Cukup'
    Klarifikasi = input("\nApakah ingin beli lagi? (Cukup/Iya): ").title()

# Gabungkan seluruh total harga sebelum menghitung diskon
total_gabungan = total_item1 + total_tambahan
diskon = hitung_diskon(kategori_beli, total_gabungan)
total_bayar = total_gabungan - diskon

# --- STRUK PEMBAYARAN ---
print("\n========== NOTA PEMBAYARAN ==========")
print(f"Item Utama   : {jumlah_beli}x {item_beli} = Rp {total_item1:,}")
if total_tambahan > 0:
    print(f"Item Tambah  : Rp {total_tambahan:,}")
print("-------------------------------------")
print(f"Total Kotor  : Rp {total_gabungan:,}")
print(f"Diskon       : Rp {diskon:,.0f}")
print(f"Total Bayar  : Rp {total_bayar:,.0f}")
print("=====================================")
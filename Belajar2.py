daftar_Harga = {
    "Ayam": 15000,
    "Sapi": 12000,
    "Kambing": 10000
}

# Variabel ini akan terus menyimpan dan menjumlahkan harga tiap daging
grand_total = 0

while True:
    print("\nDaftar Harga Daging:")
    for Daging, harga in daftar_Harga.items():
        print(f"{Daging}: Rp {harga} per kg")
    
    pilihan = input("Masukkan jenis daging yang ingin dibeli (Ayam/Sapi/Kambing): ").title()

    if pilihan not in daftar_Harga:
        print("Jenis daging tidak tersedia. Silakan pilih dari daftar.")
        continue

    # --- Proses Hitung Tiap Item ---
    if pilihan == "Ayam":
        Beli_Daging = float(input("Masukkan jumlah ayam yang dibeli (dalam kg): "))
        if Beli_Daging >= 5:
            Bayar = Beli_Daging * daftar_Harga[pilihan] * 0.9
        else:
            Bayar = Beli_Daging * daftar_Harga[pilihan]
            
    elif pilihan == "Sapi":
        Beli_Daging = float(input("Masukkan jumlah sapi yang dibeli (dalam kg): "))
        if Beli_Daging >= 2:
            Bayar = Beli_Daging * daftar_Harga[pilihan] * 0.85
        else:
            Bayar = Beli_Daging * daftar_Harga[pilihan]
            
    elif pilihan == "Kambing":
        Beli_Daging = float(input("Masukkan jumlah kambing yang dibeli (dalam kg): "))
        if Beli_Daging >= 3:
            Bayar = Beli_Daging * daftar_Harga[pilihan] * 0.88
        else:
            Bayar = Beli_Daging * daftar_Harga[pilihan]

    # Akumulasikan harga item ke total seluruhnya
    grand_total += Bayar

    # Tampilkan keranjang belanjaan saat ini
    print(f"-> Berhasil menambahkan: {Beli_Daging} kg {pilihan} (Rp {Bayar:,.0f})")
        
    # --- Konfirmasi Selesai Belanja ---
    Klarifikasi = input("\nApakah ingin beli lagi? (Cukup/Iya): ")
    if Klarifikasi.lower() != "iya":
        # Kode di bawah ini HANYA jalan jika user mengetik "Cukup" atau selain "iya"
        print("\n=========================================")
        print(f"   TOTAL NOTA BELANJA: Rp {grand_total:,.0f}")
        print("=========================================")
        print("Terima kasih sudah berbelanja!")
        break
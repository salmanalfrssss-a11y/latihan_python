Harga_Daging=int(10000)
Beli_Daging=float(input("Masukkan jumlah daging yang dibeli (dalam kg): "))
Bayar2=int(Beli_Daging*Harga_Daging)
#print("Total harga yang harus dibayar: Rp", Bayar)

if Beli_Daging > 2 and Beli_Daging < 5:
    Bayar = Bayar2 -5000
elif Beli_Daging >= 5:
    Bayar = Bayar2 - 7000
else:
    Bayar = Bayar2
print("Total harga: Rp", Bayar) 

Klarifikasi=input("Apakah ingin beli lagi? (Cukup/Iya): ")

while Klarifikasi == "Iya":
    Beli_Daging2=float(input("Masukkan jumlah daging yang dibeli (dalam kg): "))
    Beli_Daging = Beli_Daging + Beli_Daging2
    Bayar2=int(Beli_Daging*Harga_Daging)
    if Beli_Daging > 2 and Beli_Daging < 5:
        Bayar = Bayar2 -5000
    elif Beli_Daging >= 5:
        Bayar = Bayar2 - 7000
    else:
        Bayar = Bayar2
    print("Total harga: Rp", Bayar) 
    Klarifikasi=input("Apakah ingin beli lagi? (Cukup/Iya): ")


print("Total harga yang harus dibayar: Rp", Bayar)
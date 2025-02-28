def hitung_biaya_pengiriman(berat, jarak, express=False, member=False):
    biaya = 10000
    if berat > 5:
        biaya += 5000
    if jarak > 10:
        biaya += 8000
    if express:
        biaya += 20000
    if member:
        biaya *= 0.9  # Diskon 10%
    return int(biaya)

if __name__ == "__main__":
    berat = float(input("Masukkan berat paket (kg): "))
    jarak = float(input("Masukkan jarak pengiriman (km): "))
    express = input("Apakah ingin layanan express? (y/n): ").strip().lower() == 'y'
    member = input("Apakah Anda member? (y/n): ").strip().lower() == 'y'
    
    biaya = hitung_biaya_pengiriman(berat, jarak, express, member)
    
    print("\n===============================")
    print("RINCIAN BIAYA PENGIRIMAN PAKET")
    print("===============================")
    print(f"Biaya dasar: Rp 10.000")
    if berat > 5:
        print(f"Tambahan berat (>5kg): Rp 5.000")
    if jarak > 10:
        print(f"Tambahan jarak (>10km): Rp 8.000")
    if express:
        print(f"Tambahan express: Rp 20.000")
    subtotal = 10000 + (5000 if berat > 5 else 0) + (8000 if jarak > 10 else 0) + (20000 if express else 0)
    print(f"Subtotal: Rp {subtotal}")
    if member:
        diskon = int(subtotal * 0.1)
        print(f"Diskon member (10%): Rp {diskon}")
        subtotal -= diskon
    print("-------------------------------")
    print(f"TOTAL BIAYA: Rp {subtotal}")
    print("===============================")

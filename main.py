def hitung_biaya_pengiriman(berat, jarak, express=False, member=False):
    biaya_dasar = 10000
    tambahan_berat = 5000 if berat > 5 else 0
    tambahan_jarak = 8000 if jarak > 10 else 0
    tambahan_express = 20000 if express else 0
    
    total_biaya = biaya_dasar + tambahan_berat + tambahan_jarak + tambahan_express
    
    if member:
        total_biaya *= 0.9  # Diskon 10%
    
    return int(total_biaya)  # Mengembalikan nilai dalam bentuk integer

# Contoh penggunaan
print(hitung_biaya_pengiriman(6, 15, express=True, member=True))  # Output total biaya

# Hitung Biaya Pengiriman
=======================
Script ini menghitung total biaya pengiriman berdasarkan berat paket, jarak pengiriman, jenis layanan (biasa atau express), serta status keanggotaan pelanggan (member atau non-member).

Case:
-----
Sebuah jasa pengiriman memiliki aturan biaya yang mencakup beberapa aspek. Biaya dasar pengiriman ditetapkan sebesar Rp 10.000. Jika berat paket melebihi 5 kg, maka akan dikenakan tambahan biaya sebesar Rp 5.000. Selain itu, jika jarak pengiriman lebih dari 10 km, maka akan dikenakan tambahan biaya sebesar Rp 8.000. Pelanggan yang memilih layanan express akan dikenakan tambahan biaya sebesar Rp 20.000. Namun, bagi pelanggan yang merupakan member, mereka berhak mendapatkan diskon sebesar 10% dari total biaya yang dihitung sebelum diskon diterapkan. 

Requirements:
-------------
Program ini harus mampu menerima input berupa berat paket, jarak pengiriman, jenis layanan yang dipilih (biasa atau express), serta status keanggotaan pelanggan (member atau non-member). Setelah menerima input tersebut, program harus mampu menghitung total biaya pengiriman sesuai dengan aturan yang telah ditetapkan dan mengembalikan hasil dalam bentuk integer. Untuk kemudahan penggunaan, program juga harus menyediakan antarmuka berbasis Command Line Interface (CLI), sehingga pengguna dapat langsung memasukkan data yang diperlukan. Selain itu, kode harus didokumentasikan dengan baik agar mudah dipahami dan dikelola di kemudian hari.

Cara Penggunaan:
---------------
1. Pastikan Python telah terinstal di sistem Anda.
2. Simpan script ini sebagai `hitung_biaya_pengiriman.py`.
3. Jalankan script menggunakan Python dengan memanggil fungsi `hitung_biaya_pengiriman`.

Dokumentasi Fungsi:
-------------------
```python
hitung_biaya_pengiriman(berat: float, jarak: float, express: bool = False, member: bool = False) -> int
```

- **berat**: Berat paket dalam kilogram.
- **jarak**: Jarak pengiriman dalam kilometer.
- **express**: Jika `True`, layanan pengiriman akan dipercepat dengan biaya tambahan.
- **member**: Jika `True`, pelanggan akan mendapatkan diskon 10%.
- **return**: Mengembalikan total biaya pengiriman dalam bentuk integer.

Contoh Penggunaan:
------------------
```python
# Menghitung biaya pengiriman untuk paket 6 kg dengan jarak 15 km,
# menggunakan layanan express dan pelanggan adalah member
biaya = hitung_biaya_pengiriman(6, 15, express=True, member=True)
print(f"Total biaya pengiriman: Rp {biaya}")
```
'''
```
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
  ```
## Hasil  
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


### Tampilan Hasil
![image](https://github.com/user-attachments/assets/f51e8953-6e24-4d44-b8a0-ff5248014db8)


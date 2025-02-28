Hitung Biaya Pengiriman
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

Publikasi ke GitHub:
--------------------
1. Buat repository baru di GitHub.
2. Clone repository ke komputer lokal.
3. Tambahkan script ini ke dalam repository.
4. Jalankan perintah berikut untuk mengunggah ke GitHub:

   ```sh
   git init
   git add hitung_biaya_pengiriman.py
   git commit -m "Tambah script hitung biaya pengiriman"
   git branch -M main
   git remote add origin <URL_REPOSITORY>
   git push -u origin main
   ```

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

Implementasi CLI:
------------------
```python
if __name__ == "__main__":
    berat = float(input("Masukkan berat paket (kg): "))
    jarak = float(input("Masukkan jarak pengiriman (km): "))
    express = input("Apakah ingin layanan express? (y/n): ").strip().lower() == 'y'
    member = input("Apakah Anda member? (y/n): ").strip().lower() == 'y'
    
    biaya = hitung_biaya_pengiriman(berat, jarak, express, member)
    print(f"Total biaya pengiriman: Rp {biaya}")
```
'''

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
print(f"Total biaya pengiriman: Rp {hitung_biaya_pengiriman(6, 15, express=True, member=True)}")

# CLI untuk pengguna
if __name__ == "__main__":
    berat = float(input("Masukkan berat paket (kg): "))
    jarak = float(input("Masukkan jarak pengiriman (km): "))
    express = input("Apakah ingin layanan express? (y/n): ").strip().lower() == 'y'
    member = input("Apakah Anda member? (y/n): ").strip().lower() == 'y'
    
    biaya = hitung_biaya_pengiriman(berat, jarak, express, member)
    print(f"Total biaya pengiriman: Rp {biaya}")

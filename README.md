Berikut adalah template README.md untuk menjalankan dashboard Streamlit:

```markdown
# Bike Rental Dashboard

Dashboard ini menampilkan berbagai analisis terkait perilaku pengguna dan pola penyewaan sepeda berdasarkan dataset yang tersedia. Anda dapat mengeksplorasi berbagai visualisasi seperti analisis RFM, penyewaan berdasarkan musim, hari kerja, waktu dalam sehari, dan deteksi anomali.

## Fitur Dashboard

- *Analisis RFM*: Menampilkan metrik Recency, Frequency, dan Monetary untuk pengguna kasual dan terdaftar.
- **Total Penyewaan Berdasarkan Musim dan Cuaca**: Visualisasi penyewaan sepeda berdasarkan musim dan kondisi cuaca.
- **Penyewaan Berdasarkan Hari Kerja dan Hari Libur**: Membandingkan total penyewaan antara hari kerja dan hari libur.
- **Rata-rata Penyewaan Berdasarkan Musim dan Hari Kerja**: Rata-rata penyewaan berdasarkan kombinasi musim dan hari kerja.
- **Penyewaan Berdasarkan Jam, Musim, dan Hari Kerja**: Analisis pola penyewaan per jam berdasarkan musim dan hari kerja.
- **Deteksi Anomali pada Penyewaan Harian**: Mengidentifikasi hari-hari dengan jumlah penyewaan yang anomali.
- **Analisis Tren Mingguan**: Menampilkan tren penyewaan rata-rata berdasarkan hari dalam seminggu.
- **Penyewaan Berdasarkan Waktu dalam Sehari**: Visualisasi rata-rata penyewaan berdasarkan waktu (pagi, siang, sore, malam).

## Prasyarat

Sebelum menjalankan dashboard, pastikan Anda telah menginstal beberapa dependensi berikut:

1. Python 3.x
2. Streamlit
3. Pandas
4. Matplotlib
5. Seaborn

Anda dapat menginstal semua dependensi ini dengan menjalankan perintah berikut:

```bash
pip install streamlit pandas matplotlib seaborn
```

## Menjalankan Dashboard

1. Clone repository ini atau salin skrip yang disediakan ke dalam folder proyek Anda.
   
   ```bash
   git clone https://github.com/username/repo.git
   cd repo
   ```

2. Pastikan file CSV (`hour_cleaned.csv` dan `day_cleaned.csv`) telah berada di folder yang sama dengan skrip Python.

3. Jalankan aplikasi dengan perintah berikut:

   ```bash
   streamlit run dashboard.py
   ```

4. Dashboard akan terbuka secara otomatis di browser. Jika tidak, Anda dapat mengaksesnya melalui URL berikut:

   ```
   https://dicodingilhamme.streamlit.app/
   ```
   atau

# Bike Rental Dashboard

[Klik di sini untuk melihat demo live dashboard!](https://dicodingilhamme.streamlit.app/)


## Dataset

Dataset yang digunakan dalam dashboard ini terdiri dari dua file:

- **hour_cleaned.csv**: Data penyewaan berdasarkan jam.
- **day_cleaned.csv**: Data penyewaan berdasarkan hari.

Pastikan kedua file tersebut tersedia di direktori `dashboard/` sebelum menjalankan aplikasi.

## Struktur Proyek

```plaintext
📂 dashboard/
   ├── dashboard.py          # Skrip utama aplikasi Streamlit
   ├── README.md             # Panduan ini
   ├── hour_cleaned.csv       # Dataset penyewaan berdasarkan jam
   └── day_cleaned.csv        # Dataset penyewaan berdasarkan hari
```

## Penggunaan

Setelah dashboard berjalan, Anda dapat memilih pertanyaan analisis dari panel di sebelah kiri. Hasil visualisasi akan ditampilkan di area utama dashboard.

## Kontak

Jika Anda memiliki pertanyaan atau masalah terkait dengan proyek ini, jangan ragu untuk menghubungi:

- Nama: ilham
- Email: icahyosw@gmail.com

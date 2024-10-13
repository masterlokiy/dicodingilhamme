import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Memuat data
df_hour = pd.read_csv('dashboard/hour_cleaned.csv')
df_day = pd.read_csv('dashboard/day_cleaned.csv')

# Fungsi untuk Pertanyaan 1: Analisis RFM
def question_1():
    today = pd.to_datetime(df_day['dteday'].max())
    last_rental_casual = pd.to_datetime(df_day[df_day['casual'] > 0]['dteday'].max())
    last_rental_registered = pd.to_datetime(df_day[df_day['registered'] > 0]['dteday'].max())

    # Recency
    recency_casual = (today - last_rental_casual).days
    recency_registered = (today - last_rental_registered).days

    # Frequency
    frequency_casual = df_day['casual'].sum()
    frequency_registered = df_day['registered'].sum()

    # Monetary
    monetary_casual = df_day['casual'].sum()
    monetary_registered = df_day['registered'].sum()

    recency_values = [recency_casual, recency_registered]
    frequency_values = [frequency_casual, frequency_registered]
    monetary_values = [monetary_casual, monetary_registered]
    user_types = ['Pengguna Kasual', 'Pengguna Terdaftar']

    # Visualisasi RFM
    fig, ax = plt.subplots(1, 3, figsize=(18, 5))

    # Visualisasi Recency dengan warna yang disesuaikan
    ax[0].bar(user_types, recency_values, color=['#FF6347', '#90EE90'])  # Merah untuk recency tinggi (kurang aktif), hijau untuk rendah (lebih aktif)
    ax[0].set_title('Recency: Hari Sejak Penyewaan Terakhir')
    ax[0].set_xlabel('Tipe Pengguna')
    ax[0].set_ylabel('Hari Sejak Penyewaan Terakhir')

    # Visualisasi Frequency
    ax[1].bar(user_types, frequency_values, color=['#87CEFA', '#FFA07A'])  # Biru muda dan salmon
    ax[1].set_title('Frequency: Total Penyewaan')
    ax[1].set_xlabel('Tipe Pengguna')
    ax[1].set_ylabel('Total Penyewaan')

    # Visualisasi Monetary
    ax[2].bar(user_types, monetary_values, color=['#87CEFA', '#FFA07A'])  # Biru muda dan salmon
    ax[2].set_title('Monetary: Jumlah Penyewaan Total')
    ax[2].set_xlabel('Tipe Pengguna')
    ax[2].set_ylabel('Total Penyewaan')

    plt.tight_layout()
    return fig

# Fungsi untuk Pertanyaan 2: Total Penyewaan Berdasarkan Musim dan Cuaca
def question_2():
    seasonal_usage = df_day.groupby(['season', 'weather_situation']).agg({
        'count_cr': 'sum',
        'casual': 'sum',
        'registered': 'sum'
    }).reset_index()

    plt.figure(figsize=(12, 6))
    sns.barplot(data=seasonal_usage, x='season', y='count_cr', hue='weather_situation', palette='coolwarm')
    plt.title('Total Penyewaan Berdasarkan Musim dan Cuaca')
    plt.xlabel('Musim')
    plt.ylabel('Total Penyewaan')
    plt.xticks(ticks=[0, 1, 2, 3], labels=['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin'])
    plt.legend(title='Kondisi Cuaca', loc='upper right')
    return plt

# Fungsi untuk Pertanyaan 3: Penyewaan Berdasarkan Hari Kerja dan Hari Libur
def question_3():
    df_day['day_type'] = df_day['workingday'].map({0: 'Hari Libur', 1: 'Hari Kerja'})
    usage_by_day_type = df_day.groupby('day_type').agg({
        'casual': 'sum',
        'registered': 'sum',
        'count_cr': 'sum'
    }).reset_index()

    plt.figure(figsize=(10, 5))
    usage_by_day_type.set_index('day_type').plot(kind='bar', color=['#FFA07A', '#20B2AA', '#4682B4'])  # Warna yang disesuaikan untuk keterbacaan lebih baik
    plt.title('Perbandingan Penyewaan: Pengguna Kasual vs Terdaftar')
    plt.xlabel('Tipe Hari')
    plt.ylabel('Total Penyewaan')
    plt.xticks(rotation=0)
    plt.legend(title='Tipe Pengguna', labels=['Kasual', 'Terdaftar', 'Total'])
    plt.grid(axis='y')
    return plt

# Fungsi untuk Pertanyaan 4: Rata-rata Penyewaan Berdasarkan Musim dan Hari Kerja
def question_4():
    season_workingday_usage = df_day.groupby(['season', 'workingday']).agg({'count_cr': 'mean'}).reset_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(x='season', y='count_cr', hue='workingday', data=season_workingday_usage, palette='coolwarm')
    plt.title('Rata-rata Penyewaan Berdasarkan Musim dan Hari Kerja')
    plt.xlabel('Musim')
    plt.ylabel('Rata-rata Penyewaan')
    plt.xticks(ticks=[0, 1, 2, 3], labels=['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin'])
    plt.legend(title='Hari Kerja')
    return plt

# Fungsi untuk Pertanyaan 5: Penyewaan Berdasarkan Jam, Musim, dan Hari Kerja
def question_5():
    hourly_usage = df_hour.groupby(['season', 'workingday', 'hours']).agg({'count_cr': 'mean'}).reset_index()
    plt.figure(figsize=(14, 7))
    sns.lineplot(x='hours', y='count_cr', hue='season', style='workingday', data=hourly_usage, palette='coolwarm')
    plt.title('Penyewaan Berdasarkan Jam, Musim, dan Hari Kerja')
    plt.xlabel('Jam dalam Sehari')
    plt.ylabel('Rata-rata Penyewaan')
    plt.xticks(range(0, 24, 1))  # Menampilkan setiap jam dari 0 hingga 23
    plt.legend(title='Musim & Hari Kerja')
    return plt

# Fungsi untuk Pertanyaan 6: Deteksi Anomali pada Penyewaan Harian
def question_6():
    mean_cnt = df_day['count_cr'].mean()
    std_cnt = df_day['count_cr'].std()
    upper_bound = mean_cnt + 2 * std_cnt
    lower_bound = mean_cnt - 2 * std_cnt
    anomaly_days = df_day[(df_day['count_cr'] > upper_bound) | (df_day['count_cr'] < lower_bound)]

    plt.figure(figsize=(12, 6))
    plt.plot(df_day['dteday'], df_day['count_cr'], label='Total Penyewaan')
    plt.scatter(anomaly_days['dteday'], anomaly_days['count_cr'], color='red', label='Anomali', s=50)
    plt.axhline(y=upper_bound, color='green', linestyle='--', label='Batas Atas')
    plt.axhline(y=lower_bound, color='orange', linestyle='--', label='Batas Bawah')
    plt.title('Deteksi Anomali pada Penyewaan Harian')
    plt.xlabel('Tanggal')
    plt.ylabel('Total Penyewaan')
    plt.xticks(rotation=45)
    plt.legend()
    return plt

# Fungsi untuk Pertanyaan 7: Analisis Tren Mingguan
def question_7():
    df_day['weekdays'] = pd.to_datetime(df_day['dteday']).dt.day_name()
    weekly_trend = df_day.groupby('weekdays').agg({'count_cr': 'mean'}).reindex([
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']).reset_index()

    plt.figure(figsize=(10, 5))
    sns.lineplot(x='weekdays', y='count_cr', data=weekly_trend, marker='o', linestyle='-', color='blue')
    plt.title('Rata-rata Penyewaan Berdasarkan Hari dalam Seminggu')
    plt.xlabel('Hari dalam Seminggu')
    plt.ylabel('Rata-rata Penyewaan')
    plt.xticks(rotation=45)
    return plt

# Fungsi untuk Pertanyaan 8: Penyewaan Berdasarkan Waktu dalam Sehari
def question_8():
    def time_of_day(hour):
        if 5 <= hour < 12:
            return 'Pagi'
        elif 12 <= hour < 17:
            return 'Siang'
        elif 17 <= hour < 21:
            return 'Sore'
        else:
            return 'Malam'

    df_hour['time_of_day'] = df_hour['hours'].apply(time_of_day)
    time_of_day_order = ['Pagi', 'Siang', 'Sore', 'Malam']
    time_of_day_usage = df_hour.groupby('time_of_day').agg({'count_cr': 'mean'}).reindex(time_of_day_order).reset_index()

    plt.figure(figsize=(10, 5))
    sns.barplot(x='time_of_day', y='count_cr', data=time_of_day_usage, palette='coolwarm')
    plt.title('Rata-rata Penyewaan Berdasarkan Waktu dalam Sehari')
    plt.xlabel('Waktu dalam Sehari')
    plt.ylabel('Rata-rata Penyewaan')
    return plt

# Streamlit Sidebar
st.sidebar.title("Pertanyaan Analisis")
option = st.sidebar.selectbox(
    "Pilih pertanyaan:",
    (
        "Analisis RFM",
        "Total Penyewaan Berdasarkan Musim dan Cuaca",
        "Penyewaan Berdasarkan Hari Kerja dan Hari Libur",
        "Rata-rata Penyewaan Berdasarkan Musim dan Hari Kerja",
        "Penyewaan Berdasarkan Jam, Musim, dan Hari Kerja",
        "Deteksi Anomali pada Penyewaan Harian",
        "Analisis Tren Mingguan",
        "Penyewaan Berdasarkan Waktu dalam Sehari"
    )
)

# Menampilkan visualisasi berdasarkan pilihan pengguna
st.title(f"Analisis untuk: {option}")

if option == "Analisis RFM":
    st.pyplot(question_1())
    st.write('Pengguna Terdaftar adalah kelompok utama yang menggunakan layanan penyewaan sepeda, baik dari sisi frekuensi maupun total kontribusi penyewaan. Pengguna Kasual menggunakan layanan lebih sedikit dibandingkan pengguna terdaftar, meskipun mereka tetap aktif berdasarkan nilai recency yang sama.')
    
elif option == "Total Penyewaan Berdasarkan Musim dan Cuaca":
    st.pyplot(question_2())
    st.write('Musim semi adalah waktu paling populer untuk bersepeda, dengan cuaca cerah sangat memengaruhi keputusan orang untuk menyewa sepeda. Musim lainnya, terutama musim dingin, memiliki jumlah penyewaan yang jauh lebih sedikit, menunjukkan bahwa cuaca dan kondisi musim sangat memengaruhi kebiasaan bersepeda masyarakat.')

elif option == "Penyewaan Berdasarkan Hari Kerja dan Hari Libur":
    st.pyplot(question_3())
    st.write('Pengguna terdaftar cenderung lebih aktif pada hari kerja, sedangkan pengguna kasual lebih aktif pada hari libur. Ini dapat menjadi pertimbangan penting untuk strategi pemasaran dan promosi, seperti menawarkan paket atau diskon khusus untuk pengguna kasual pada akhir pekan atau hari libur')

elif option == "Rata-rata Penyewaan Berdasarkan Musim dan Hari Kerja":
    st.pyplot(question_4())
    st.write('Rata-rata penggunaan sepeda bervariasi tergantung pada musim dan jenis hari. Musim semi adalah waktu paling aktif untuk penyewaan sepeda, sementara musim dingin cenderung menjadi waktu dengan penyewaan terendah. Terdapat perbedaan yang jelas antara penggunaan sepeda pada hari kerja dan hari libur, dengan hari kerja menunjukkan angka yang lebih tinggi.')

elif option == "Penyewaan Berdasarkan Jam, Musim, dan Hari Kerja":
    st.pyplot(question_5())
    st.write('Cuaca (musim) dan status hari kerja sangat mempengaruhi pola penggunaan sepeda. Penggunaan sepeda meningkat pada jam commuting di hari kerja dan menurun di musim dingin. Di hari libur, meskipun tidak ada lonjakan signifikan di pagi atau sore hari, penggunaan sepeda lebih stabil sepanjang hari.')

elif option == "Deteksi Anomali pada Penyewaan Harian":
    st.pyplot(question_6())
    st.write('Pola penyewaan sepeda menunjukkan tren peningkatan dari awal 2011 hingga pertengahan 2012, diikuti oleh penurunan pada akhir 2012 hingga awal 2013. Anomali terdeteksi pada beberapa titik, baik sebagai penurunan signifikan (anomali bawah) maupun lonjakan tak terduga (anomali atas), yang kemungkinan disebabkan oleh faktor eksternal seperti cuaca, pemeliharaan, kebijakan lokal, atau acara khusus. Puncak penggunaan terjadi pada pertengahan 2012 sebelum tren mulai menurun, menunjukkan potensi faktor musiman yang memengaruhi penggunaan sepeda. Batas anomali memberikan panduan dalam mengidentifikasi penyewaan yang tidak biasa, baik terlalu tinggi maupun terlalu rendah.')

elif option == "Analisis Tren Mingguan":
    st.pyplot(question_7())
    st.write('Penggunaan sepeda paling optimal selama hari kerja, terutama menjelang akhir minggu. Ini bisa menjadi indikasi bahwa layanan penyewaan sepeda lebih banyak digunakan untuk kegiatan sehari-hari seperti pergi bekerja atau beraktivitas di kota, sementara pada akhir pekan, pengguna lebih jarang memanfaatkan layanan ini.')

elif option == "Penyewaan Berdasarkan Waktu dalam Sehari":
    st.pyplot(question_8())
    st.write('Waktu terbaik untuk layanan penyewaan sepeda adalah pada sore dan siang hari, dengan potensi penawaran promosi atau peningkatan layanan pada pagi hari. Di sisi lain, layanan pada malam hari mungkin bisa ditingkatkan jika ada kebutuhan khusus seperti acara malam atau peningkatan keamanan.')

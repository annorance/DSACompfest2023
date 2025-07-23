# Data Science Academy (DSA) 15 by COMPFEST UI 

Data Science Academy (DSA) merupakan rangkaian acara COMPFEST 15 yang diselenggarakan oleh Universitas Indonesia yang dibuat untuk mengantarkan pengetahuan dan aplikasi data science yang berperan penting dalam perancangan strategi bisnis. 

Data Science Academy terdiri dari tiga camp. Untuk setiap camp, peserta akan mendapatkan materi dari pembicara dan mentor yang berpengalaman dalam data science. 

Peserta juga mengikuti kegiatan mentoring dan mengerjakan case study yang akan diberikan pada akhir camp pertama dan camp kedua. Pada akhir camp, ketiga peserta akan melakukan presentasi final project yang telah diberikan pada minggu sebelumnya. 

Harapan dari hadirnya Data Science Academy COMPFEST 15 adalah para peserta dapat mengembangkan pengetahuan dan keterampilan yang dimiliki dalam bidang data science sehingga dapat memenuhi kebutuhan yang ada dalam industri bisnis. Terdapat total 3 projek yang diselesaikan dalam kegiatan pelatihan ini

## Tugas Khusus (Seleksi Awal): Analisis hubungan antara tingkat pendidikan penduduk dan frekuensi kejadian banjir di Jakarta
Model yang digunakan dalam penelitian ini adalah regresi linier, dengan mean squared error (MSE) sebagai metrik evaluasi. Hasil evaluasi model menunjukkan nilai MSE sebesar 1.93. Mengingat bahwa dalam MSE, semakin kecil nilainya maka semakin baik performa model, maka nilai ini mengindikasikan bahwa model yang dibangun memiliki performa yang cukup baik dalam memprediksi variabel target.

Selain menggunakan pendekatan regresi, kami juga melakukan pengujian hipotesis untuk mengetahui pengaruh tingkat pendidikan terhadap tingkat banjir di Jakarta. Terdapat dua variabel bebas yang digunakan, yaitu:
- X₁: Tingkat pendidikan "Tidak Bersekolah – Tamat SD"
- X₂: Tingkat pendidikan "SLTP – Strata III" Pada persamaan regresi yang dihasilkan, nilai koefisien untuk variabel X₂ (SLTP – Strata III) adalah negatif. Hal ini mengindikasikan bahwa peningkatan tingkat pendidikan hingga level SLTP ke atas tidak menunjukkan pengaruh positif yang signifikan terhadap penurunan atau peningkatan tingkat banjir. Hasil pengujian menunjukkan nilai:
- F hitung = 2,07146293
- F tabel = 3,49 (F{(0,95)(2), (20)}) Karena F hitung < F tabel, maka keputusan yang diambil adalah menerima H₀ dan menolak Hₐ, sehingga dapat disimpulkan bahwa tingkat pendidikan tidak memiliki pengaruh yang signifikan terhadap tingkat banjir di Jakarta.

Berdasarkan hasil analisis regresi dan pengujian hipotesis, dapat disimpulkan bahwa tidak terdapat hubungan yang signifikan antara tingkat pendidikan masyarakat dan tingkat kejadian banjir di Jakarta.

## Projek Akhir: Prediksi Harga Electric Vehicle
Kami memutuskan untuk mencari tahu apakah prediksi harga berdasarkan kapasitas baterai dan efisiensi dapat dijadikan dasar rekomendasi harga EV. Untuk itu, kami mengadakan uji hipotesis alternatif untuk membuktikan apakah dua variabel tersebut memengaruhi harga EV. H0 adalah Prediksi harga berdasarkan kapasitas baterai dan efesiensi tidak dapat dijadikan dasar rekomendasi harga EV sedangkan H1 adalah Prediksi harga berdasarkan kapasitas baterai dan efesiensi dapat dijadikan dasar rekomendasi harga EV. Diperoleh persamaan regresi linear Y = -1.124e+09 + 2.934e+07X1 + 1.156e+06X2. Dari hipotesis yang telah dianalisis, didapati bahwa harga yang diprediksi tidak terlalu naik disebabkan konstanta a menunjukkan angka yang negatif

Pada tahap pembangunan model, proses dimulai dengan preprocessing data. Berdasarkan hasil Exploratory Data Analysis (EDA), kami menemukan adanya outlier, namun nilai-nilai tersebut masih tergolong masuk akal dalam konteks kendaraan listrik, sehingga tidak dihapus dari dataset. Selain itu, analisis korelasi menggunakan Pearson correlation menunjukkan bahwa variabel Kapasitas Baterai (kWh) memiliki korelasi positif dengan Harga (Rp), dengan nilai korelasi absolut yang tergolong tinggi. Di sisi lain, variabel Efisiensi (Wh/km) juga menunjukkan korelasi positif terhadap harga, namun dengan nilai korelasi absolut yang lebih rendah dibandingkan dengan kapasitas baterai. Temuan ini mengindikasikan bahwa kapasitas baterai memiliki pengaruh yang lebih dominan terhadap harga EV dibandingkan efisiensi energi.

Model yang dibangun adalah Linear Regression dan Decision Tree Regressor, dengan konfigurasi terbaik menggunakan criterion = "entropy", max_depth = 3, dan min_samples_leaf = 5. Model ini mencapai akurasi tertinggi sebesar 83% dan Mean Squared Error (MSE) sebesar 0.4.

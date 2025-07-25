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

## Graduation Night: BREATHIFY
### Problem Definition
**Objective:** Significantly reduce air pollution levels in the Greater Jakarta (Jabodetabek) area and mitigate its adverse impacts on public health, the environment, and the economy.
**Main Problem Identified:** 
- Low public engagement and action
- Lack of effective public policy implementation
- Uncontrolled industrial and commercial emissions
**Root Cause:** Low public awareness and insufficient understanding of pollution sources and climate issues.
### Problem Validation
The data team conducted a multi-source analysis to validate the root problem using both expert data and public perception.
#### Discrepancy in Pollution Source Perception vs. Reality
KLHK (Indonesian Ministry of Environment and Forestry) reports the main sources of air pollution are:
1. Transportation
2. Industrial Energy
3. Commercial, Residential, and Manufacturing (equal contribution)
Katadata (Public Perception Survey) shows the public believes air pollution is primarily caused by:
1. Vehicle Emissions
2. Waste Burning
3. Cigarette Smoke
4. Forest Fires
5. Coal Power Plants
6. Building Construction
7. Household Emissions
8. Others
9. Don’t Know
    
**_Insight:_** This clear mismatch between actual and perceived sources of air pollution reveals a significant lack of public awareness.
#### Supporting Data on Emission Sources
**Vehicle Ownership (BPS 2020–2022):**
- Motorcycles: 79.5%
- Passenger Cars: 16.9%
- Trucks: 3.4%
- Buses: 0.0002%
**Waste Management (2022)**
- The most common method among the public is open burning, a major contributor to air pollution.
**Forest Fire Data (2019–2022)**
According to GlobalForestWatch, more than 25,000 hectares are affected by forest fires annually in Indonesia.

#### Climate Change Awareness Survey
_Source: Data for Good at Meta and Yale Program on Climate Change Communication (2022)_
-Public Knowledge on Climate Change
  - Little knowledge: 50.2%
  - A lot: 16.5%
  - Never heard of it: 15.6%
- Cause Perception: Most respondents believe climate change is caused by both human activity and nature.
- Perceived Severity: Majority say the impact is moderate.
- Global Perception: Surveyed countries (South Africa, South America, Australia, Brazil, China, India) agree that environmental issues pose serious problems. Only India and USA indicated that environmental protection is not a top priority.
  
#### PM2.5 Air Quality Data (Jan–Aug 2023)
_Location: Ancol, Angkasa Kemayoran, Regatta The Icon, Galur, LTC Glodok_
- PM2.5 levels have shown a sharp increase in the past eight months.
- Urgent action is required to curb this rise.

### Proposed Solution: Breathify
Breathify is a mobile application designed as a community engagement tool to tackle air pollution through behavioral change and awareness-building.

Key features:
- EcoPoint: A reward-based program to incentivize environmentally friendly actions.
- EcoChallenge: Actionable challenges to promote real-world change.
- EcoLearn: Educational resources to improve public understanding of environmental issues.
- Ecommunity: A platform to connect users with a like-minded environmental community.

Impact Goal: To bridge the gap between environmental knowledge and action, empowering individuals to contribute actively to pollution reduction and climate resilience.

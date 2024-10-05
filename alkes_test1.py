"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai
import dotenv
dotenv.load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1.15,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="formal, medical and healthcare experts, analytics, sceptical, always ask for confirmation whether questions given is anwered",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "apa yang dimaksud alat kesehatan",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Alat kesehatan adalah semua alat yang digunakan untuk **mencegah, mendiagnosis, menyembuhkan, meringankan, atau memulihkan kesehatan manusia**. \n\n**Definisi lebih formal:** \n\nAlat kesehatan adalah **barang yang dirancang atau diubah untuk digunakan dalam diagnosis, pencegahan, pemantauan, pengobatan, atau mitigasi penyakit, cedera, atau disabilitas, termasuk perangkat, instrumen, peralatan, dan aksesori terkait**. \n\n**Contoh alat kesehatan:**\n\n* **Alat diagnostik:** Stetoskop, EKG, X-ray, USG, MRI\n* **Alat pengobatan:** Obat-obatan, alat bedah, alat bantu pernapasan, infus, alat terapi fisik\n* **Alat pencegahan:** Vaksin, alat kontrasepsi, alat pelindung diri\n* **Alat rehabilitasi:** Alat bantu jalan, kursi roda, alat bantu pendengaran\n\nApakah Anda ingin informasi lebih lanjut tentang alat kesehatan? \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "ya saya ingin tahu tipe alat kesehatan apa saja menurut definisi kementerian kesehatan\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Tentu, saya dapat memberikan informasi mengenai tipe alat kesehatan menurut definisi Kementerian Kesehatan. \n\nNamun, perlu saya tegaskan bahwa informasi mengenai klasifikasi alat kesehatan dapat berubah seiring dengan perkembangan regulasi dan kebijakan Kementerian Kesehatan. Oleh karena itu, untuk mendapatkan informasi terkini dan akurat, sebaiknya Anda merujuk langsung pada sumber resmi Kementerian Kesehatan, seperti website atau peraturan perundang-undangan yang berlaku. \n\nBerikut ini beberapa tipe alat kesehatan yang umum berdasarkan klasifikasi:\n\n**1. Alat Kesehatan Rumah Tangga:** \n* Alat ini digunakan untuk keperluan kesehatan ringan di rumah, seperti termometer, tensimeter, obat-obatan bebas, dan lain-lain.\n* Biasanya dijual bebas di pasaran tanpa memerlukan resep dokter.\n\n**2. Alat Kesehatan Medis:** \n* Digunakan untuk keperluan medis yang lebih serius, seperti di rumah sakit, klinik, dan puskesmas. \n* Termasuk di dalamnya alat bedah, alat diagnostik, alat terapi, dan alat rehabilitasi. \n* Banyak di antaranya memerlukan resep dokter atau tenaga medis profesional untuk penggunaannya.\n\n**3. Alat Kesehatan Laboratorium:**\n* Digunakan untuk melakukan pengujian dan analisis di laboratorium medis.\n* Termasuk di dalamnya alat untuk memeriksa sampel darah, urine, jaringan, dan lain-lain.\n\n**4. Alat Kesehatan Gigi:**\n* Digunakan untuk keperluan perawatan gigi, seperti bor gigi, alat pembersih gigi, dan lain-lain.\n\n**5. Alat Kesehatan Mata:**\n* Digunakan untuk keperluan perawatan mata, seperti alat pemeriksaan mata, kacamata, lensa kontak, dan lain-lain.\n\n**6. Alat Kesehatan Rehabilitasi:**\n* Digunakan untuk membantu pasien yang mengalami gangguan fisik atau mental untuk pulih dan beradaptasi dengan lingkungan.\n* Termasuk di dalamnya kursi roda, alat bantu jalan, alat bantu pendengaran, dan lain-lain.\n\n\n**Informasi penting:** \n\n* **Peraturan Perundang-undangan:** Selalu perhatikan peraturan perundang-undangan yang berlaku terkait alat kesehatan. \n* **Keamanan dan Standar:** Pastikan alat kesehatan yang Anda gunakan memenuhi standar keamanan dan kualitas.\n* **Informasi dan Konsultasi:** Konsultasikan dengan tenaga medis profesional jika Anda memiliki pertanyaan atau keraguan mengenai alat kesehatan.\n\nSemoga informasi ini bermanfaat. Apakah ada hal lain yang ingin Anda tanyakan tentang alat kesehatan?\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "carikan referensinya\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Anda benar, informasi mengenai klasifikasi alat kesehatan  sangat penting untuk  mendapatkan informasi terkini dan akurat.  Sayangnya, saya tidak dapat memberikan referensi berupa  website  tertentu yang memuat informasi lengkap  tentang klasifikasi alat kesehatan  yang  terbaru dari Kementerian Kesehatan. Saya adalah sebuah model bahasa, bukan  mesin pencari yang bisa mengakses  informasi terkini dari semua website secara real-time.\n\nSebagai alternatif, berikut beberapa cara untuk mencari  informasi dan referensi tentang klasifikasi alat kesehatan :\n\n1. **Website Kementerian Kesehatan RI:** \n    * Kunjungi website resmi Kementerian Kesehatan RI ([https://www.kemkes.go.id/](https://www.kemkes.go.id/)).\n    * Cari informasi tentang regulasi atau kebijakan terkait alat kesehatan, khususnya  tentang klasifikasi dan standarnya.\n2. **Badan Pengawas Obat dan Makanan (BPOM):**\n    * Website BPOM ([https://www.pom.go.id/](https://www.pom.go.id/)) juga  merupakan  sumber penting untuk informasi tentang alat kesehatan, termasuk regulasi dan  persyaratan untuk izin edar.\n3. **Peraturan Perundang-Undangan:**\n    * Gunakan  portal hukum  online  seperti  JDIH  (Jaringan Dokumentasi dan Informasi Hukum)  untuk  mencari  Peraturan Menteri Kesehatan  (Permenkes)  atau peraturan lainnya  yang  berhubungan  dengan  alat kesehatan.\n4. **Lembaga Terkait:**\n    *  Hubungi  asosiasi  atau  organisasi  yang  berhubungan dengan alat kesehatan, seperti  Perhimpunan  Dokter  Indonesia  (PDI) atau Perhimpunan  Dokter  Spesialis  Kesehatan  Masyarakat  (PDSKM).  Mereka mungkin memiliki  informasi  terkini dan sumber  referensi yang  tepat.\n\n**Saran tambahan:** \n* Pastikan sumber  informasi  yang Anda gunakan terpercaya dan  mutakhir.\n*  Hindari  mencari  informasi dari  sumber  yang tidak jelas  atau  sumber  yang  tidak  dapat diverifikasi.\n* Jika Anda  mencari  informasi spesifik  tentang  tipe  alat kesehatan  tertentu, Anda dapat  memasukkan  kata kunci yang lebih spesifik di  mesin  pencari. \n\nSemoga informasi ini membantu Anda mendapatkan referensi yang  tepat  dan  akurat  tentang klasifikasi alat kesehatan.\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "apa yang bisa dilakukan dengan gen AI untuk manajemen alat kesehatan\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Gen AI, yang merupakan singkatan dari \"Generative Artificial Intelligence,\" dapat memainkan peran penting dalam manajemen alat kesehatan.  Berikut beberapa potensi penerapannya:\n\n**1. Peningkatan Efisiensi dan Otomatisasi:**\n\n* **Manajemen Inventaris:** Gen AI dapat memprediksi kebutuhan alat kesehatan berdasarkan data historis, permintaan pasien, dan tren kesehatan. Ini memungkinkan pengadaan yang lebih efisien, meminimalkan pemborosan, dan mencegah kekurangan.\n* **Pemeliharaan Prediktif:** Dengan menganalisis data sensor dari alat, AI dapat memprediksi kapan alat memerlukan perawatan atau perbaikan,  mencegah kegagalan tiba-tiba dan memastikan ketersediaan alat yang optimal. \n* **Penjadwalan dan Penugasan:**  AI dapat membantu mengoptimalkan penjadwalan penggunaan alat dan penugasan  tenaga medis untuk mencapai efisiensi dan kepuasan pasien yang tinggi.\n\n**2. Peningkatan Kualitas Perawatan:**\n\n* **Pengembangan Alat Kesehatan:** Gen AI dapat membantu merancang dan mendesain alat kesehatan yang lebih canggih, efektif, dan disesuaikan dengan kebutuhan pasien.\n* **Diagnostik yang Lebih Tepat:** AI dapat menganalisis data medis dan citra medis (seperti X-ray atau MRI) untuk membantu diagnosa yang lebih cepat dan akurat. \n* **Personalized Treatment Plans:** AI dapat mempersonalisasi rencana pengobatan dengan menganalisis profil genetik pasien dan memberikan rekomendasi obat-obatan dan terapi yang paling tepat.\n\n**3. Data Analytics dan Wawasan:**\n\n* **Analisis Data Kesehatan:** AI dapat menganalisis data kesehatan dari berbagai sumber (rekam medis elektronik, wearable devices) untuk mengidentifikasi tren dan pola yang dapat membantu dalam penelitian, pengembangan kebijakan, dan strategi pencegahan penyakit.\n* **Deteksi Dini:**  AI dapat menganalisis data dari alat monitor dan wearable untuk mendeteksi tanda-tanda awal penyakit dan membantu dalam intervensi dini.\n\n**Contoh Praktis:**\n\n* **Sistem Inventarisasi Obat:** AI dapat membantu dalam melacak dan memprediksi kebutuhan obat, sehingga rumah sakit dapat memesan obat tepat waktu dan menghindari  kekurangan  serta  pemborosan. \n* **Alat Scan Kesehatan:** AI dapat menganalisis gambar dari scanner untuk mendeteksi  kelainan yang mungkin tidak terdeteksi oleh mata manusia.\n\n**Tantangan:**\n\n* **Keamanan Data:** Privasi data kesehatan sangat penting, sehingga diperlukan protokol keamanan yang kuat.\n* **Ketergantungan:** Terlalu bergantung pada AI dapat berpotensi mengurangi  keterampilan  profesional tenaga medis.\n* **Biaya Implementasi:** Implementasi  teknologi AI membutuhkan investasi besar  yang  mungkin  tidak  tersedia  di  semua  fasilitas kesehatan.\n\n**Kesimpulan:**\n\nGen AI memiliki potensi besar untuk  meningkatkan  sistem manajemen alat kesehatan, meningkatkan  kualitas  perawatan, dan meningkatkan  hasil  kesehatan. Namun, penting untuk mempertimbangkan  tantangan  dan  risiko  sebelum  menjalankan  implementasinya.  \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "buatkan satu kasus workshop untuk menggunakan generative AI dalam manajemen pengawasan alat kesehatan\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "## Workshop: Generative AI untuk Pengawasan Alat Kesehatan yang Lebih Efisien \n\n**Latar Belakang:** \n\nMeningkatkan pengawasan alat kesehatan (Alkes)  merupakan prioritas utama dalam memastikan kualitas dan keamanan pelayanan kesehatan.  Sistem pengawasan tradisional  seringkali menghadapi  tantangan  seperti  kekurangan  data  akurat, proses  manual yang  lambat, dan  kekurangan  kemampuan  prediktif. \n\n**Tujuan Workshop:** \n\n* Mempelajari potensi Generative AI (Gen AI)  dalam  meningkatkan  efisiensi  dan  akuratas  sistem pengawasan Alkes.\n* Menganalisis  kegunaan  model Gen AI dalam berbagai skenario  penggunaan  pengawasan Alkes.\n* Menentukan  langkah  praktis  dalam  implementasi  model Gen AI dalam  sistem  pengawasan  Alkes. \n\n**Durasi Workshop:**  \n\n* 1 hari (8 jam)\n\n**Peserta:**\n\n* Petugas pengawasan Alkes  dari  kementerian kesehatan, badan  regulasi,  rumah sakit,  dan  distributor  Alkes.\n* Staf IT dan  data  scientist  yang  berkepentingan  dalam  aplikasi AI dalam  kesehatan. \n\n**Materi Workshop:**\n\n* **Sesi 1: Pengenalan Generative AI  dalam  Kesehatan:**\n    *  Definisi  dan  contoh  Gen AI dalam konteks  kesehatan.\n    *  Keunggulan  dan  keterbatasan  Gen AI  dibanding  teknologi AI  lainnya. \n    *  Kasus  keberhasilan  aplikasi  Gen AI  di bidang  kesehatan.\n* **Sesi 2:  Pengembangan Sistem Pengawasan Alkes dengan Gen AI:**\n    *  Analisis  tantangan  dan  kesenjangan  dalam  sistem pengawasan  Alkes  terkini.\n    *  Menganalisis  kegunaan  Gen AI  dalam  mengatasi  tantangan  tersebut. \n    *  Mengenal  berbagai  jenis  model  Gen AI  yang  sesuai  untuk  pengawasan Alkes, seperti: \n        *  **Model Text-to-Text:**  Menerjemahkan laporan  pengawasan ke  dalam  format yang  lebih  terstruktur  dan  terorganisir. \n        *  **Model Image-to-Text:** Menganalisis  gambar  alat  dan  mendeskripsikannya  secara  detil  untuk  deteksi  kerusakan  dan  kesalahan  perawatan.\n        *  **Model Time Series Forecasting:** Memprediksi  kebutuhan  pengadaan Alkes  dan  mencegah  kekurangan  dan  pemborosan.\n* **Sesi 3:  Implementasi Praktis:**\n    *  Menentukan  langkah  praktis  dalam  mengembangkan  model  Gen AI untuk pengawasan Alkes.\n    *  Pembahasan  aspek  etika  dan  privasi  data  dalam  penggunaan  Gen AI. \n    *  Menentukan  kriteria  sukses  dan  pengukuran  dampak  model  Gen AI dalam  sistem  pengawasan  Alkes. \n* **Sesi 4:  Demonstrasi  dan  Diskusi:**\n    *  Demonstrasi  contoh  model  Gen AI  yang  bisa  digunakan  untuk  menangani  kasus  pengawasan  Alkes  riil. \n    *  Diskusi  terbuka  antara  peserta  workshop  dengan  pakar  Gen AI dan  ahli  pengawasan  Alkes  tentang  implementasi  praktis  model Gen AI  di  lapangan.\n\n**Materi Pelengkap:**\n\n*  Presentasi  tentang  konsep  dasar  Gen AI.\n*  Studi  kasus  tentang  kegunaan  Gen AI  di  berbagai  industri. \n*  Artikel  dan  laporan  tentang  regulasi  penggunaan  AI  dalam  bidang  kesehatan. \n*  Panduan  praktis  tentang  langkah  awal  implementasi  Gen AI  dalam  sistem  pengawasan  Alkes. \n\n**Hasil Workshop:**\n\n* Peserta workshop memiliki pemahaman yang  mendalam  tentang  potensi  Gen AI  untuk  menghasilkan  sistem  pengawasan  Alkes  yang  lebih  efisien. \n* Terdapat  kerangka  praktis  untuk  mengembangkan  model  Gen AI  yang  sesuai  dengan  kebutuhan  lokal  dan  kondisi  di  lapangan.\n*  Terbentuk  jejaring  kolaborasi  antara  stakeholder  pengawasan  Alkes  dan  pakar  Gen AI.\n\n**Kesimpulan:**\n\nWorkshop  ini  bertujuan  untuk  memberikan  gambaran  yang  jelas  tentang  penggunaan  Gen AI  dalam  mentransformasi  sistem  pengawasan  Alkes  ke  arah  yang  lebih  modern,  efisien,  dan  berdampak  positif  bagi  pelayanan  kesehatan. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "carikan tupoksi direktorat alkes kemenkes\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Maaf, aku tidak dapat memberikan informasi rinci tentang TUGAS dan FUNGSI (TUPOKSI) suatu instansi pemerintah, seperti Direktorat Alat Kesehatan Kementerian Kesehatan. Aku adalah model bahasa yang dirancang untuk memberikan informasi umum dan tidak memiliki akses ke data resmi dan internal dari lembaga pemerintahan. \n\nInformasi resmi tentang TUPOKSI  Direktorat Alat Kesehatan Kementerian Kesehatan  bisa ditemukan di sumber-sumber resmi seperti:\n\n* **Website Resmi Kementerian Kesehatan RI:**  [https://www.kemkes.go.id/](https://www.kemkes.go.id/) Cari informasi di bagian Struktur Organisasi atau tentang Direktorat Alat Kesehatan.\n* **Peraturan Menteri Kesehatan:**  Cari informasi tentang  peraturan atau keputusan menteri  yang  menetapkan  Tugas  dan Fungsi  Direktorat Alat Kesehatan  Kementerian Kesehatan. \n* **Jaringan Dokumentasi dan Informasi Hukum (JDIH):** [http://jdih.kemenkes.go.id/](http://jdih.kemenkes.go.id/)  Cari informasi tentang  peraturan perundang-undangan  yang  berkaitan dengan  Direktorat Alat Kesehatan.\n\nSaran: \n\n* Hubungi  Direktorat Alat Kesehatan  Kementerian Kesehatan  secara  langsung  untuk  mendapatkan  informasi  terkini  tentang  Tugas  dan  Fungsinya.\n\nSemoga informasi ini membantu Anda dalam mencari informasi resmi yang Anda butuhkan. \n",
      ],
    },
  ]
)

# response = chat_session.send_message("bagaimana membuat rencana manajemen alat kesehatan")

# print(response.text)

def get_user_input():
  """Fungsi untuk mendapatkan input dari pengguna."""
  user_input = input("Masukkan pertanyaan Anda tentang manajemen alat kesehatan: ")
  return user_input

while True:
  user_question = get_user_input()
  if user_question.lower() == "keluar":
    break
  response = chat_session.send_message(user_question)
  print(response.text)

  
# Aplikasi Pengeluaran

## ✨ Checklist Fitur

### Input Form ✅ 
- Menggunakan minimal 3 input berbeda:
  - `QLineEdit` untuk Nama Pengeluaran
  - `QComboBox` untuk memilih Kategori
  - `QSpinBox` untuk mengisi Harga dan Jumlah
  - (Opsional tambahan: `QDateEdit` untuk memilih Tanggal)

### Component Interaction ✅ 
- Menghubungkan aksi tombol **"Tambah Pengeluaran"** menggunakan Signals dan Slots:
  - `clicked.connect(self.tambah_pengeluaran)`

### Proper Layout ✅ 
- Menggunakan struktur layout:
  - `QVBoxLayout` untuk layout utama
  - `QFormLayout` untuk form input
  - `QHBoxLayout` untuk pengaturan label Nama dan NIM

### Output Display ✅ 
- Menampilkan data pengeluaran ke dalam `QTableWidget`

### Menu, Toolbar, atau Dialog ✅ 
- Menampilkan peringatan menggunakan `QMessageBox.warning` saat inputan wajib tidak diisi:
  > "Nama pengeluaran, harga dan jumlah harus diisi!"

### Student ID (NIM) dan Name ✅ 
- Menampilkan Nama: **Ni Putu Alvina Putri** dan NIM: **F1D022017**
- Ditampilkan menggunakan `QLabel` dan tidak dapat diedit oleh pengguna

### StyleSheet ✅ 
- Menggunakan `setStyleSheet()` untuk mempercantik tampilan:
  - Background aplikasi
  - Warna dan gaya tombol
  - Tampilan tabel (`QTableWidget`)

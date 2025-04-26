from PyQt5 import QtWidgets, QtCore
import sys

class PengeluaranApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.total_belanja = 0  
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Aplikasi Pengeluaran')
        self.resize(600, 500)  
        
        
        self.layout = QtWidgets.QVBoxLayout()

        
        self.namaLabel = QtWidgets.QLabel("Nama: Ni Putu Alvina Putri")
        self.nimLabel = QtWidgets.QLabel("NIM: F1D022017")
        font = self.namaLabel.font()
        font.setPointSize(12)
        font.setBold(True)
        self.namaLabel.setFont(font)
        self.nimLabel.setFont(font)
        self.namaLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nimLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.namaLabel)
        self.layout.addWidget(self.nimLabel)

        
        formLayout = QtWidgets.QFormLayout()

        self.pengeluaranInput = QtWidgets.QLineEdit()
        formLayout.addRow("Nama Pengeluaran:", self.pengeluaranInput)

        self.hargaInput = QtWidgets.QSpinBox()
        self.hargaInput.setMinimum(0)
        self.hargaInput.setMaximum(1000000000)
        self.hargaInput.setSingleStep(1000)
        formLayout.addRow("Harga Item (Rp):", self.hargaInput)

        self.jumlahInput = QtWidgets.QSpinBox()
        self.jumlahInput.setMinimum(1)
        self.jumlahInput.setMaximum(10000)
        formLayout.addRow("Jumlah Item:", self.jumlahInput)

        self.kategoriComboBox = QtWidgets.QComboBox()
        self.kategoriComboBox.addItems(["Belanja", "Makanan", "Transportasi", "Lainnya"])
        formLayout.addRow("Kategori:", self.kategoriComboBox)

        self.tanggalInput = QtWidgets.QDateEdit()
        self.tanggalInput.setCalendarPopup(True)
        self.tanggalInput.setDate(QtCore.QDate.currentDate())
        formLayout.addRow("Tanggal:", self.tanggalInput)

        self.layout.addLayout(formLayout)

        self.tambahButton = QtWidgets.QPushButton("Tambah Pengeluaran")
        self.layout.addWidget(self.tambahButton)

        self.table = QtWidgets.QTableWidget()
        self.table.setRowCount(0)
        self.table.setColumnCount(5)  
        self.table.setHorizontalHeaderLabels(["Nama", "Harga", "Jumlah", "Kategori", "Tanggal"])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.layout.addWidget(self.table)

        self.totalLabel = QtWidgets.QLabel("Total Belanja: Rp 0")
        totalFont = self.totalLabel.font()
        totalFont.setPointSize(11)
        totalFont.setBold(True)
        self.totalLabel.setFont(totalFont)
        self.totalLabel.setAlignment(QtCore.Qt.AlignRight)
        self.layout.addWidget(self.totalLabel)

        self.setLayout(self.layout)

        self.tambahButton.clicked.connect(self.tambah_pengeluaran)

        self.setStyleSheet("""
            QWidget {
                background-color: #f4f4f4;
                font-size: 12pt;
                color: #333;
            }
            QLabel {
                color: #000000;
                font-weight: bold;
            }
            QFormLayout QLabel {
                color: black;
                font-weight: normal;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QTableWidget {
                border: 1px solid #ccc;
                background-color: #ffffff;
            }
        """)

    def tambah_pengeluaran(self):
        nama_pengeluaran = self.pengeluaranInput.text()
        harga = self.hargaInput.value()
        jumlah = self.jumlahInput.value()
        kategori = self.kategoriComboBox.currentText()
        tanggal = self.tanggalInput.date().toString("dd/MM/yyyy")

        if nama_pengeluaran == "" or harga == 0 or jumlah == 0:
            QtWidgets.QMessageBox.warning(self, "Peringatan", "Nama pengeluaran, harga dan jumlah harus diisi!")
            return

        total_harga = harga * jumlah

        rowPosition = self.table.rowCount()
        self.table.insertRow(rowPosition)
        self.table.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(nama_pengeluaran))
        self.table.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(f"Rp {harga:,}"))
        self.table.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(jumlah)))
        self.table.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(kategori))
        self.table.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(tanggal))

        self.total_belanja += total_harga
        self.totalLabel.setText(f"Total Belanja: Rp {self.total_belanja:,}")

        self.pengeluaranInput.clear()
        self.hargaInput.setValue(0)
        self.jumlahInput.setValue(1)
        self.kategoriComboBox.setCurrentIndex(0)
        self.tanggalInput.setDate(QtCore.QDate.currentDate())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = PengeluaranApp()
    window.show()
    sys.exit(app.exec_())

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import uic

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("MainWin.ui", self) #load window/ui file
        self.show()

        self.label.setAlignment(Qt.AlignCenter)

        self.jenisZakat.addItems(["-", "Fitrah", "Perniagaan", "Pendapatan"]) #add jenis zakat
        self.negeri() #add item/negeri
        
        self.jenisZakat.activated.connect(self.enable)
        self.pilihNegeri.activated.connect(self.enable_harga)

        self.pushButton.clicked.connect(self.kira_kadar_zakat)

    def kira_kadar_zakat(self):
        kadar = 0
        if self.jenisZakat.currentText() == "Fitrah":
            murah = 7.00
            biasa = 14.00
            mahal = 21.00
            bil_ahli_keluarga = int(self.spinBox.value())

            if self.hargaBeras.currentText() == "Murah":
                kadar = murah * bil_ahli_keluarga
            if self.hargaBeras.currentText() == "Biasa":
                kadar = biasa * bil_ahli_keluarga
            if self.hargaBeras.currentText() == "Mahal":
                kadar = mahal * bil_ahli_keluarga

            #special cases
            if self.pilihNegeri.currentText() == "Kuala Lumpur/Putrajaya/Labuan":
                murah = 5.00
                biasa = 7.00
                mahal = 14.00
                
                if self.hargaBeras.currentText() == "Murah":
                    kadar = murah * bil_ahli_keluarga
                if self.hargaBeras.currentText() == "Biasa":
                    kadar = biasa * bil_ahli_keluarga
                if self.hargaBeras.currentText() == "Mahal":
                    kadar = mahal * bil_ahli_keluarga

            if self.pilihNegeri.currentText() == "Kedah":
                murah = 5.00
                biasa = 7.00
                mahal = 14.00
                premium = 21.00
                
                if self.hargaBeras.currentText() == "Murah":
                    kadar = murah * bil_ahli_keluarga
                if self.hargaBeras.currentText() == "Biasa":
                    kadar = biasa * bil_ahli_keluarga
                if self.hargaBeras.currentText() == "Mahal":
                    kadar = mahal * bil_ahli_keluarga
                if self.hargaBeras.currentText() == "Terpaling Premium Yak Mat":
                    kadar = premium * bil_ahli_keluarga
            
            if self.pilihNegeri.currentText() == "Pulau Pinang":
                murah = 7.00
                biasa = 12.00
                mahal = 16.00

                if self.hargaBeras.currentText() == "Murah":
                    kadar = murah * bil_ahli_keluarga
                if self.hargaBeras.currentText() == "Biasa":
                    kadar = biasa * bil_ahli_keluarga
                if self.hargaBeras.currentText() == "Mahal":
                    kadar = mahal * bil_ahli_keluarga

            if self.pilihNegeri.currentText() == "Johor":
                murah = 7.00
                biasa = 10.00

                if self.hargaBeras.currentText() == "Murah":
                    kadar = murah * bil_ahli_keluarga
                if self.hargaBeras.currentText() == "Biasa":
                    kadar = biasa * bil_ahli_keluarga
            
            if self.pilihNegeri.currentText() == "Sabah":
                murah = 6.00
                biasa = 7.50

                if self.hargaBeras.currentText() == "Murah":
                    kadar = murah * kadar
                if self.hargaBeras.currentText() == "Biasa":
                    kadar = biasa * bil_ahli_keluarga
        
        if self.jenisZakat.currentText() == "Perniagaan":
            hasil = float(self.lineEdit_3.text())
            kadar = hasil * (25/100)

        if self.jenisZakat.currentText() == "Pendapatan":
            jumlah = float(self.inputJumlahPendapatan.text())
            kadar = jumlah * (2.5/100)

        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setText("RM{:.2f}".format(kadar))

    def negeri(self):

        self.pilihNegeri.addItem("-")

        #setiap negeri simpan nilai/pilihan harga beras
        self.pilihNegeri.addItem("Perlis", ["-", "Murah"])
        self.pilihNegeri.addItem("Negeri Sembilan", ["-", "Murah"])
        self.pilihNegeri.addItem("Pahang", ["-", "Murah"])
        self.pilihNegeri.addItem("Terengganu", ["-", "Murah"])
        self.pilihNegeri.addItem("Sarawak", ["-", "Murah"])

        self.pilihNegeri.addItem("Melaka", ["-", "Murah", "Biasa"])
        self.pilihNegeri.addItem("Johor", ["-", "Murah", "Biasa"])
        self.pilihNegeri.addItem("Sabah", ["-", "Murah", "Biasa"])

        self.pilihNegeri.addItem("Pulau Pinang", ["-", "Murah", "Biasa", "Mahal"])
        self.pilihNegeri.addItem("Perak", ["-", "Murah", "Biasa", "Mahal"])
        self.pilihNegeri.addItem("Selangor", ["-", "Murah", "Biasa", "Mahal"])
        self.pilihNegeri.addItem("Kelantan", ["-", "Murah", "Biasa", "Mahal"])
        self.pilihNegeri.addItem("Kuala Lumpur/Putrajaya/Labuan", ["-", "Murah", "Biasa", "Mahal"])

        self.pilihNegeri.addItem("Kedah", ["-", "Murah", "Biasa", "Mahal", "Terpaling Premium Yak Mat"])
        
        #bila dropdown list ditekan method manage dipanggil
        self.pilihNegeri.activated.connect(self.manage)

    def manage(self, index):
        #setiap kali tekan dropdown button negeri, list harga beras akan dibersihkan
        self.hargaBeras.clear()
        #selepas dibersihkan, harga beras yang baharu akan ditambah ke dalam comboBox
        self.hargaBeras.addItems(self.pilihNegeri.itemData(index))

    def enable_harga(self):
        self.hargaBeras.setEnabled(True)
        if self.jenisZakat.currentText() == "Fitrah":
            self.hargaBeras.setEnabled(True)
            self.spinBox.setEnabled(True)
            self.inputJumlahPendapatan.setEnabled(False)
        
        if self.jenisZakat.currentText() == "Pendapatan" or self.jenisZakat.currentText() == "Perniagaan":
            self.inputJumlahPendapatan.setEnabled(True)
            self.hargaBeras.setEnabled(False)
            self.spinBox.setEnabled(False)
        
        if self.jenisZakat.currentText() == "-":
            self.inputJumlahPendapatan.setEnabled(False)
            self.hargaBeras.setEnabled(False)
            self.spinBox.setEnabled(False)
            self.pilihNegeri.setEnabled(False)

        if self.pilihNegeri.currentText() == "-":
            self.inputJumlahPendapatan.setEnabled(False)
            self.hargaBeras.setEnabled(False)
            self.spinBox.setEnabled(False)

    def enable(self):
        self.pilihNegeri.setEnabled(True)

        if self.jenisZakat.currentText() == "Pendapatan":
            self.inputJumlahPendapatan.setEnabled(True)
            self.lineEdit_3.setEnabled(False)
            self.pilihNegeri.setEnabled(False)
            self.hargaBeras.setEnabled(False)
            self.spinBox.setEnabled(False)
        #bila pilihan = "Perniagaan", tempat kosong yang ketiga akan enabled
        if self.jenisZakat.currentText() == "Perniagaan":
            self.inputJumlahPendapatan.setEnabled(False)
            self.lineEdit_3.setEnabled(True)
            self.pilihNegeri.setEnabled(False)
            self.hargaBeras.setEnabled(False)
            self.spinBox.setEnabled(False)

        if self.jenisZakat.currentText() == "-":
            self.inputJumlahPendapatan.setEnabled(False)
            self.hargaBeras.setEnabled(False)
            self.spinBox.setEnabled(False)
            self.pilihNegeri.setEnabled(False)

        if self.pilihNegeri.currentText() == "-":
            self.hargaBeras.setEnabled(False)
            self.spinBox.setEnabled(False)

def main():
    app = QApplication([])

    window = Window()
    window.setWindowTitle("Kalkulator Zakat")

    app.exec_()

if __name__ == "__main__":
    main()
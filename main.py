from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QPushButton, QLabel, QLineEdit, QDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from author import Ui_Dialog_ario
from pytube import YouTube
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        
        uic.loadUi("main.ui", self)
        
        self.logo = self.findChild(QLabel, "yt_logo")
        self.link = self.findChild(QLineEdit, "link_yt")
        self.link_lokasi = self.findChild(QLineEdit, "link_lokasi")
        self.btn_getlink = self.findChild(QPushButton, "btn_getlink")
        self.btn_getlokasi = self.findChild(QPushButton, "btn_getlokasi")
        self.label_border = self.findChild(QLabel, "label_border")
        self.details = self.findChild(QLabel, "details")
        self.lokasi = self.findChild(QLabel, "lokasi")
        self.judul = self.findChild(QLabel, "judul")
        self.durasi = self.findChild(QLabel, "durasi")
        self.views = self.findChild(QLabel, "views")
        self.getjudul = self.findChild(QLabel, "getjudul")
        self.getdurasi = self.findChild(QLabel, "getdurasi")
        self.getviews = self.findChild(QLabel, "getviews")
        self.success = self.findChild(QLabel, "success")
        self.dvideo = self.findChild(QPushButton, "dvideo")
        self.daudio = self.findChild(QPushButton, "daudio")
        
        self.link_lokasi.hide()
        self.btn_getlokasi.hide()
        self.label_border.hide()
        self.details.hide()
        self.lokasi.hide()
        self.judul.hide()
        self.durasi.hide()
        self.views.hide()
        self.getjudul.hide()
        self.getdurasi.hide()
        self.getviews.hide()
        self.success.hide()
        self.dvideo.hide()
        self.daudio.hide()
        
        self.btn_getlink.clicked.connect(self.getLink)
        self.btn_getlokasi.clicked.connect(self.location)
        self.dvideo.clicked.connect(self.downloadVideo)
        self.daudio.clicked.connect(self.downloadAudio)
        
        self.show()
        
        self.actionAuthor.triggered.connect(self.authorInfo)
        self.actionPDIP.triggered.connect(self.pdip)
        
    def getLink(self):
        global yt
        url = self.link.text()
        yt = YouTube(url)
        
        self.link_lokasi.show()
        self.btn_getlokasi.show()
        self.label_border.show()
        self.details.show()
        self.lokasi.show()
        self.judul.show()
        self.durasi.show()
        self.views.show()
        self.getjudul.show()
        self.getdurasi.show()
        self.getviews.show()
        self.dvideo.show()
        self.daudio.show()
        
        self.getjudul.setText(yt.title)
        self.getdurasi.setText(str(yt.length) + " " + "detik")
        self.getviews.setText(str(yt.views))
        
    def location(self):
        global fname_field
        fname = str(QFileDialog.getExistingDirectory(self, "Pilih Lokasi Penyimpanan"))
        self.link_lokasi.setText(fname)
        fname_field = self.link_lokasi.text()
        
    def downloadVideo(self):
        ys = yt.streams.get_highest_resolution()
        ys.download(fname_field)
        self.success.show()
        self.success.setText("Berhasil")
        
    def downloadAudio(self):
        ys = yt.streams.filter(only_audio=True).first()
        ys.download(fname_field)
        self.success.setText("Berhasil")
        
    def authorInfo(self):
        self.modal = QDialog()
        self.author = Ui_Dialog_ario()
        self.author.setupUi(self.modal)
        self.modal.show()
        
    def pdip(self):
        self.pixmap = QPixmap("icon/pdip.png")
        self.logo.setPixmap(self.pixmap)
        self.setStyleSheet("background-color: rgb(219,32,22);")
        self.link.setStyleSheet("border-style: solid; border-width: 5px; border-color: rgb(20,10,9);")
        self.btn_getlink.setStyleSheet("border-style: solid; border-width: 5px; border-color: rgb(20,10,9);")
        self.label_border.setStyleSheet("border-style: solid; border-width: 5px; border-color: rgb(20,10,9);")
        self.link_lokasi.setStyleSheet("border-style: solid; border-width: 5px; border-color: rgb(20,10,9);")
        self.btn_getlokasi.setStyleSheet("border-style: solid; border-width: 5px; border-color: rgb(20,10,9);")
        self.dvideo.setStyleSheet("background-color: rgb(20,10,9); border-style: rounded; border-radius: 5px; color: white;")
        self.daudio.setStyleSheet("background-color: rgb(20,10,9); border-style: rounded; border-radius: 5px; color: white;")
        
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
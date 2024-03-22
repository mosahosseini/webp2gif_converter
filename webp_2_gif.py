# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 18:19:32 2024

@author: sasyn
"""

import sys , os 
from PyQt5.QtWidgets import QApplication , QMainWindow , QListWidget , QListWidgetItem , QPushButton
from PyQt5.QtCore import Qt , QUrl
import PIL 
from PIL import Image


class Listboxwidget(QListWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.resize(600,600)
        
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()
    
    def dragMoveEvent(self ,event):
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()
            
    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
            links = []
            
            for url in event.mimeData().urls():
                if url.isLocalFile():
                    links.append(str(url.toLocalFile()))
            self.addItems(links)
        
        else:
            event.ignore()
            

class AppDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1200,600)
        self.lst_box_view = Listboxwidget(self)
        
        self.btn = QPushButton("Convert" , self)
        self.btn.setGeometry(850,400,200,50)
        self.btn.clicked.connect(lambda : self.getSelectedItem())

    def getSelectedItem(self):
        items = [self.lst_box_view.item(x).text() for x in range(self.lst_box_view.count())] 
        status = {}
        
        for file_dir in items:
            if file_dir[-4:] == "webp":
                Image.open(file_dir).save(file_dir[:-4]+"gif", Format = "GIF" , save_all = True)
                status[file_dir.split("/")[-1]] =  "succeed"
            else : 
                status[file_dir.split("/")[-1]] =  "failed"
        
        
        for key ,val in status.items():
            print(key + " "*6 + val)
        
        
        
        
app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec_())
        
        
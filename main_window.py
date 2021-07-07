# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import constants


class Ui_Dialog(object):
    # in this group we add checkboxes to check if it's seleceted or not
    groupList = []
    ''' This dictionary will have checkboxes as key and 
    frame as definition to put enable = true or false if it's checked or not'''
    dict_check  = {}
  
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 522)



        self.grp_Type = QGroupBox(Dialog)
        self.grp_Type.setObjectName(u"grp_Type")
        self.grp_Type.setGeometry(QRect(22, 12, 441, 111))
        self.frm_Ping = QFrame(self.grp_Type)
        self.frm_Ping.setObjectName(u"frm_Ping")
        self.frm_Ping.setGeometry(QRect(110, 60, 321, 41))
        self.frm_Ping.setFrameShape(QFrame.StyledPanel)
        self.frm_Ping.setFrameShadow(QFrame.Raised)
        self.txt_From = QTextEdit(self.frm_Ping)
        self.txt_From.setObjectName(u"txt_From")
        self.txt_From.setGeometry(QRect(3, 10, 151, 21))
        font = QFont()
        font.setPointSize(8)
        self.txt_From.setFont(font)
        self.txt_From.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.txt_From.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lbl_Sep = QLabel(self.frm_Ping)
        self.lbl_Sep.setObjectName(u"lbl_Sep")
        self.lbl_Sep.setGeometry(QRect(156, 10, 21, 20))
        self.txt_Dest = QTextEdit(self.frm_Ping)
        self.txt_Dest.setObjectName(u"txt_Dest")
        self.txt_Dest.setGeometry(QRect(170, 10, 151, 21))
        self.txt_Dest.setFont(font)
        self.txt_Dest.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.txt_Dest.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.frm_Sniff = QFrame(self.grp_Type)
        self.frm_Sniff.setObjectName(u"frm_Sniff")
        self.frm_Sniff.setGeometry(QRect(110, 10, 321, 51))
        self.frm_Sniff.setFrameShape(QFrame.StyledPanel)
        self.frm_Sniff.setFrameShadow(QFrame.Raised)
        self.lbl_Time = QLabel(self.frm_Sniff)
        self.lbl_Time.setObjectName(u"lbl_Time")
        self.lbl_Time.setGeometry(QRect(4, 19, 29, 20))
        self.txt_time = QSpinBox(self.frm_Sniff)
        self.txt_time.setObjectName(u"txt_time")
        self.txt_time.setGeometry(QRect(40, 19, 61, 22))
        self.lbl_seconds = QLabel(self.frm_Sniff)
        self.lbl_seconds.setObjectName(u"lbl_seconds")
        self.lbl_seconds.setGeometry(QRect(117, 20, 61, 20))
        self.chk_Sniff = QRadioButton(self.grp_Type)
        self.chk_Sniff.setObjectName(u"chk_Sniff")
        self.chk_Sniff.setGeometry(QRect(10, 30, 85, 20))
        self.chk_Ping = QRadioButton(self.grp_Type)
        self.chk_Ping.setObjectName(u"chk_Ping")
        self.chk_Ping.setGeometry(QRect(10, 70, 95, 20))
        self.btn_OK = QPushButton(Dialog)
        self.btn_OK.setObjectName(u"btn_OK")
        self.btn_OK.setEnabled(True)
        self.btn_OK.setGeometry(QRect(80, 410, 93, 28))
        # self.lst_Result = QListWidget(Dialog)
        self.lst_Result = QTableWidget(Dialog)
        self.lst_Result.setObjectName(u"lst_Result")
        self.lst_Result.setGeometry(QRect(20, 150, 441, 231))
        self.progressBar = QProgressBar(Dialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(26, 470, 471, 23))
        self.progressBar.setValue(24)
        self.btn_Cancel = QPushButton(Dialog)
        self.btn_Cancel.setObjectName(u"btn_Cancel")
        self.btn_Cancel.setEnabled(True)
        self.btn_Cancel.setGeometry(QRect(320, 410, 93, 28))
        self.btn_Export = QPushButton(Dialog)
        self.btn_Export.setObjectName(u"btn_Export")
        self.btn_Export.setEnabled(False)
        self.btn_Export.setGeometry(QRect(200, 410, 93, 28))

        self.retranslateUi(Dialog)
        
        self.dict_check [self.chk_Sniff] = self.frm_Sniff
        self.dict_check [self.chk_Ping] = self.frm_Ping
        self.setValues()


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Security Devices Scanner", None))
        self.grp_Type.setTitle(QCoreApplication.translate("Dialog", u"Type", None))
        self.lbl_Sep.setText(QCoreApplication.translate("Dialog", u" - ", None))
        self.lbl_Time.setText(QCoreApplication.translate("Dialog", u"Time", None))
        self.lbl_seconds.setText(QCoreApplication.translate("Dialog", u"Seconds", None))
        self.chk_Sniff.setText(QCoreApplication.translate("Dialog", u"Free Scan", None))
        self.chk_Ping.setText(QCoreApplication.translate("Dialog", u"IP Range", None))
        self.btn_OK.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.btn_Cancel.setText(QCoreApplication.translate("Dialog", u"CANCEL", None))
        self.btn_Export.setText(QCoreApplication.translate("Dialog", u"EXPORT", None))
    # retranslateUi
    
    def setValues(self):
      self.progressBar.setValue(0)
      self.chk_Sniff.setChecked(True)
      self.txt_time.setValue(10)
      self.groupList.append(self.chk_Sniff)
      self.groupList.append(self.chk_Ping)
      
    

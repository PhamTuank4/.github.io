from functools import partial
from PyQt6 import QtCore, QtGui, QtWidgets
from gd_admin import Ui_MainWindow
import sys
from gd_user import Ui_Form
import giaodich

class MainWindow:
    def __init__(self):
        self.main_win = QtWidgets.QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)

        self.uic.pushButton.clicked.connect(self.taoTK)
        self.uic.pushButton_2.clicked.connect(self.moCuaSoGD)


    def moCuaSoGD(self):
        print("Ham mo cua so GD chay dung")
        self.Form1 = QtWidgets.QWidget()
        self.ui1 = Ui_Form()
        self.ui1.setupUi(self.Form1)
        self.Form1.show()

        self.Form2 = QtWidgets.QWidget()
        self.ui2 = Ui_Form()
        self.ui2.setupUi(self.Form2)
        self.Form2.show()

        self.ui1.pushButton.clicked.connect(partial(self.Login, self.ui1))
        self.ui2.pushButton.clicked.connect(partial(self.Login, self.ui2))

        self.ui1.pushButton_2.clicked.connect(partial(self.NapTienGD, self.ui1))
        self.ui2.pushButton_2.clicked.connect(partial(self.NapTienGD, self.ui2))

        self.ui1.pushButton_6.clicked.connect(partial(self.RutTienGD, self.ui1))
        self.ui2.pushButton_6.clicked.connect(partial(self.RutTienGD, self.ui2))

        self.ui1.pushButton_7.clicked.connect(partial(self.ChuyenTienGD, self.ui1, self.ui2))
        self.ui2.pushButton_7.clicked.connect(partial(self.ChuyenTienGD, self.ui2, self.ui1))

        
        self.ui1.pushButton_5.clicked.connect(partial(self.InChuoiKhoiGD, self.ui1))
        self.ui2.pushButton_5.clicked.connect(partial(self.InChuoiKhoiGD, self.ui2))

    def InChuoiKhoiGD(self, formGD):
        print("Done")
        ck = formGD.tk_hien_tai.InChuoiKhoiTongDai()
        formGD.textEdit_9.setText(ck)

    def NapTienGD(self, formGD):
        print("Done")
        # 1.lay so tien muon nap
        so_tien_nap = int(formGD.textEdit_4.toPlainText())
        # 2.Cap nhat so du vao tai khoan
        formGD.tk_hien_tai.NapTien(so_tien_nap)
        # 3.hien thi so du moi
        self.CapNhatSoDu(formGD)

        
    def RutTienGD(self, formGD):
        print("Done")
        # 1.lay so tien muon rut
        so_tien_rut = int(formGD.textEdit_10.toPlainText())
        # 2.Cap nhat so du vao tai khoan
        formGD.tk_hien_tai.RutTien(so_tien_rut)
        # 3.hien thi so du moi
        self.CapNhatSoDu(formGD)

    def ChuyenTienGD(self, formGD, form_dich):
        print("Done")
        # 1.lay so tien muon chuyen
        so_tien_chuyen = int(formGD.textEdit_12.toPlainText())
        #2.Chon tai khoan muon chuyen
        tk_dich = form_dich.tk_hien_tai
        # 3.Cap nhat so du vao tai khoan
        formGD.tk_hien_tai.ChuyenTien(so_tien_chuyen, tk_dich)
        # 4.hien thi so du moi
        self.CapNhatSoDu(formGD)
        self.CapNhatSoDu(form_dich)

    def LayTaiKhoan(self, ten_user):
        for tk in giaodich.danh_sach_TK:
            if tk.ten_chu_TK == ten_user:
                return tk

 
    def Login(self, formGD):
        print("Loading compeled")
        ten = formGD.textEdit.toPlainText()
        CMND = formGD.textEdit_2.toPlainText()

        for tk in giaodich.danh_sach_TK:
            if tk.ten_chu_TK == ten:
                if tk.so_CMND == CMND:
                    formGD.label_3.setText("Chúc mừng đăng nhập thành công")
                    formGD.tk_hien_tai = tk
                    self.CapNhatSoDu(formGD)
                    return
        formGD.label_3.setText("Vui lòng nhập lại thông tin")
    
    def CapNhatSoDu(self, formGD):
        so_du = formGD.tk_hien_tai.so_du_TK
        formGD.textEdit_3.setText(str(so_du))
        formGD.textEdit_11.setText(str(so_du))
        formGD.textEdit_14.setText(str(so_du))

    def taoTK(self):
        print("Ham tao tai khoan chay dung")
        ten = self.uic.textEdit.toPlainText()
        CMND = self.uic.textEdit_2.toPlainText()
        so_tien = int(self.uic.textEdit_3.toPlainText())
        tk = giaodich.TaiKhoan(so_tien, CMND, ten)
        giaodich.themTK(tk)

        print(giaodich.danh_sach_TK[0].so_CMND)
        print(giaodich.danh_sach_TK[0].ten_chu_TK)  

    def show(self):
        self.main_win.show()  

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
from datetime import datetime
import hashlib
from random import randint

class TaiKhoan:
    so_du_TK = 0
    so_CMND = "123456"
    ten_chu_TK = "tuan"
    so_tai_khoan = ""
    Lich_su_GD = []
    ds_khoi = {}

    def __init__(self, so_du, CMND, ten):
        self.so_du_TK = so_du
        self.so_CMND = CMND
        self.ten_chu_TK = ten
        self.TaoSoTK()
        self.Lich_su_GD = []
        self.ds_khoi = ChuoiKhoi()

    def LayChuoiKhoi(self):
        global chuoi_khoi_he_thong
        self.ds_khoi = chuoi_khoi_he_thong
    def themkhoiGD(self, gd):
        self.LayChuoiKhoi()
        khoi_hien_tai = KhoiGD()
        gd_ban_dau = self.LuuTruTThongTinO(gd)
        # ck = self.ds_khoi
        # k0 = ck.chuoi_khoi[ck.tong_so_khoi-1].bam_hien_tai
        # khoi_hien_tai.taokhoi(gd,k0)
        # khoi_hien_tai = self.sinhKhoiInternetA(gd)

        # 1.Mô phỏng quá trình bị tấn công
        biTanCong = randint(1,10)
        print("bien bi tan cong: ",biTanCong)
        if biTanCong > 5:
            khoi_hien_tai = self.sinhKhoiInternet(gd)
        else:
            khoi_hien_tai = self.sinhKhoiInternetA(gd)
        # 2.Phát hiện thâm nhập va phong thu
        kt = self.KiemTraBiTanCong_v1(khoi_hien_tai, gd_ban_dau)
        if kt == 1:
            print("Khoi da bi tan cong")
            self.themkhoiGD(gd_ban_dau)
        else: 
            print("Khoi khong bi tan cong")
            self.ds_khoi.themkhoi(khoi_hien_tai)


    def KiemTraBiTanCong_v1(self, khoi, gd_ban_dau):
        kt = 0
        if khoi.thong_tin_GD.so_tien !=gd_ban_dau.so_tien:
           kt = 1
        return kt

    def LuuTruTThongTinO(self, gd):
        giao_dich = ThongTinGD("", "", 0)
        giao_dich.tai_khoan_nguon = gd.tai_khoan_nguon
        giao_dich.tai_khoan_dich = gd.tai_khoan_dich
        giao_dich.so_tien = gd.so_tien
        giao_dich.thoi_gian_phat_sinh = gd.thoi_gian_phat_sinh
        return giao_dich


    def sinhKhoiInternetA(self, gd):
        self.LayChuoiKhoi()
        khoi_hien_tai = KhoiGD()
        ck = self.ds_khoi
        k0 = ck.chuoi_khoi[ck.tong_so_khoi-1].bam_hien_tai
        gd.so_tien = gd.so_tien * 2
        khoi_hien_tai.taokhoi(gd,k0)
        return khoi_hien_tai

    def sinhKhoiInternet(self, gd):
        self.LayChuoiKhoi()
        khoi_hien_tai = KhoiGD()
        ck = self.ds_khoi
        k0 = ck.chuoi_khoi[ck.tong_so_khoi-1].bam_hien_tai
        khoi_hien_tai.taokhoi(gd,k0)
        return khoi_hien_tai
  
    def TaoSoTK(self):
        self.so_tai_khoan = self.ten_chu_TK + " - " + self.so_CMND

    def NapTien(self, so_tien):
        self.so_du_TK = self.so_du_TK + so_tien
        gd = ThongTinGD(self.so_tai_khoan, self.so_tai_khoan, so_tien)
        self.Lich_su_GD.append(gd)
        self.themkhoiGD(gd)
      
    def RutTien(self, so_tien):
        self.so_du_TK = self.so_du_TK - so_tien
        gd = ThongTinGD(self.so_tai_khoan, self.so_tai_khoan, -1*so_tien)
        self.Lich_su_GD.append(gd)
        self.themkhoiGD(gd)

    def ChuyenTien(self, so_tien,tk_dich):
        self.so_du_TK = self.so_du_TK - so_tien
        tk_dich.so_du_TK = tk_dich.so_du_TK + so_tien
        gd = ThongTinGD(self.so_tai_khoan, tk_dich.so_tai_khoan, so_tien)
        self.Lich_su_GD.append(gd)
        self.themkhoiGD(gd)

    def InSaoKe(self):
        x = 1
        for gd in self.Lich_su_GD:
            print("Giao dich thu ", x)
            print(" - Tai khoan nguon la: ", gd.tai_khoan_nguon)
            print(" - Tai khoan dich la: ", gd.tai_khoan_dich)
            print(" - So tien: ", gd.so_tien)
            print(" - Thoi gian phat sinh: ", gd.thoi_gian_phat_sinh)
            x = x + 1
    def InChuoiKhoi(self):
        x = 1
        for khoi in self.ds_khoi.chuoi_khoi:
            print("Khoi giao dich so: ", x)
            print(" - Tai khoan nguon la: ", khoi.thong_tin_GD.tai_khoan_nguon)
            print(" - Tai khoan dich la: ", khoi.thong_tin_GD.tai_khoan_dich)
            print(" - So tien: ", khoi.thong_tin_GD.so_tien)
            print(" - Thoi gian phat sinh: ", khoi.thong_tin_GD.thoi_gian_phat_sinh)
            print(" - Gia tri bam hien tai:", khoi.bam_hien_tai)
            print(" - Gia tri bam truoc do:", khoi.bam_truoc_do)
            x = x + 1

    def InChuoiKhoiTongDai(self):
        x = 1
        ck = ""
        for khoi in self.ds_khoi.chuoi_khoi:
            # print("Khoi giao dich so: ", x)
            ck = ck + "Khoi giao dich so: " + str(x) + "\n"
            # print(" - Tai khoan nguon la: ", khoi.thong_tin_GD.tai_khoan_nguon)
            ck = ck + " - Tai khoan nguon la: " + khoi.thong_tin_GD.tai_khoan_nguon + "\n"
            # print(" - Tai khoan dich la: ", khoi.thong_tin_GD.tai_khoan_dich)
            ck = ck + " - Tai khoan dich la: " + khoi.thong_tin_GD.tai_khoan_dich + "\n"
            # print(" - So tien: ", khoi.thong_tin_GD.so_tien)
            ck = ck + " - So tien: " + str(khoi.thong_tin_GD.so_tien) + "\n"
            # print(" - Thoi gian phat sinh: ", khoi.thong_tin_GD.thoi_gian_phat_sinh)
            ck = ck + " - Thoi gian phat sinh: " + khoi.thong_tin_GD.thoi_gian_phat_sinh + "\n"
            # print(" - Gia tri bam hien tai:", khoi.bam_hien_tai)
            ck = ck + " - Gia tri bam hien tai:" + khoi.bam_hien_tai + "\n"
            # print(" - Gia tri bam truoc do:", khoi.bam_truoc_do)
            ck = ck + " - Gia tri bam truoc do:" + khoi.bam_truoc_do + "\n"
            x = x + 1
        return ck

            

class ThongTinGD:
    thoi_gian_phat_sinh = ""
    tai_khoan_nguon = ""
    tai_khoan_dich = ""
    so_tien = 0

    def __init__(self, tk_nguon, tk_dich, tien):
      self.tai_khoan_nguon = tk_nguon
      self.tai_khoan_dich = tk_dich
      self.so_tien = tien
      self.thoi_gian_phat_sinh = str(datetime.now())

class KhoiGD:
    thong_tin_GD = ThongTinGD("","",0)
    bam_hien_tai = ""
    bam_truoc_do = ""

    def __init__(self):
        return
    def taokhoi(self, giao_dich, gt_bam_khoi_truoc):
        self.thong_tin_GD = giao_dich
        self.bam_truoc_do = gt_bam_khoi_truoc
        self.bam_hien_tai = self.tao_gt_bam()
    def tao_gt_bam(self):
        d1 = self.thong_tin_GD.thoi_gian_phat_sinh
        d2 = self.thong_tin_GD.tai_khoan_nguon
        d3 = self.thong_tin_GD.tai_khoan_dich
        d4 = self.thong_tin_GD.so_tien 
        d5 = self.bam_truoc_do
        tong_hop = str(d1) + str(d2) + str(d3) + str(d4) + str(d5)
        ma_hoa_tong_hop = tong_hop.encode()
        kq = hashlib.sha256(ma_hoa_tong_hop).hexdigest()
        return kq

class ChuoiKhoi:
    tong_so_khoi = 0
    chuoi_khoi = []

    def __init__(self):
        return
    def themkhoi(self, khoi):
        self.chuoi_khoi.append(khoi)
        self.tong_so_khoi = self.tong_so_khoi + 1
#Luu tru sanh sach tao tai khoan he thong
danh_sach_TK  = []
def themTK(tk):
    global danh_sach_TK
    danh_sach_TK.append(tk)
#Tao chuoi khoi cho he thong
chuoi_khoi_he_thong = ChuoiKhoi()
khoi_root = KhoiGD()
khoi_root.bam_hien_tai = "0-0-0-0"
khoi_root.bam_truoc_do = ""
chuoi_khoi_he_thong.themkhoi(khoi_root)

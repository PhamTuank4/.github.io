import hashlib
from giaodich import ThongTinGD

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
        tong_hop = d1 + d2 + d3 + d4 + d5
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
#Tao chuoi khoi cho he thong
chuoi_khoi_he_thong = ChuoiKhoi()
khoi_root = KhoiGD()
khoi_root.bam_hien_tai = "0-0-0-0"
khoi_root.bam_truoc_do = ""
chuoi_khoi_he_thong.themkhoi(khoi_root)
# k1 = KhoiGD()
# print(k1.thong_tin_GD.thoi_gian_phat_sinh)
# print(k1.thong_tin_GD.tai_khoan_nguon)
# print(k1.thong_tin_GD.tai_khoan_dich)
# print(k1.thong_tin_GD.so_tien)
# print(k1.bam_truoc_do)
# print(k1.bam_hien_tai)


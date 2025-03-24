import giaodich
from giaodich import TaiKhoan
       
tk1 = TaiKhoan(1000, "02345", "diem")
giaodich.themTK(tk1)
print(giaodich.danh_sach_TK[0].so_CMND)
ten = tk1.ten_chu_TK
print("ten chu tai khoan la: ", ten)
stk = tk1.so_tai_khoan
print("so tai khoan la: ", stk)
print("So du truoc khi nap tien la:", tk1.so_du_TK)
tk1.NapTien(200)
print("So du sau khi nap tien la:", tk1.so_du_TK)
print("So du truoc khi rut tien la:", tk1.so_du_TK)
tk1.RutTien(500)
print("So du sau khi rut tien la:", tk1.so_du_TK)
tk2 = TaiKhoan(500, "02344", "nga")
print("so du truoc khi tk1 chuyen la: ", tk1.so_du_TK)
print("so du truoc khi tk2 nhan la: ", tk2.so_du_TK)
tk1.ChuyenTien(500, tk2)
print("so du sau khi tk1 chuyen la: ", tk1.so_du_TK)
print("so du sau khi tk2 nhan la: ", tk2.so_du_TK)
tk2.NapTien(100)
tk1.InSaoKe()
print("tk1")
tk1.InChuoiKhoi()
print("tk2")
tk2.InChuoiKhoi()

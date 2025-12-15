import pandas as pd
class monhoc():
    def __init__(self,mamonhoc,tenmonhoc,sotinchi):
        self.mamonhoc=mamonhoc
        self.tenmonhoc=tenmonhoc
        self.sotinchi=sotinchi
    def hienthithongtinmonhoc(self):
        print(f"ma mon hoc {self.mamonhoc}")
        print(f"ten mon hoc{self.tenmonhoc}")
        print(f"so tin chi{self.sotinchi}")
    def _str_(self):
        return ",".join([self.mamonhoc, self.tenmonhoc, self.sotinchi])
A=[]
def nhapthongtinhocsinh():
    while(True):
        mamonhoc, tenmonhoc, sotinchi= input("nhap ma mon hoc, ten mon hoc, so tin chi ").split(",")
        a=monhoc(mamonhoc, tenmonhoc, sotinchi)
        A.append(a)
        n=input("muốn nhập nữa không, không nhập nữa thì nhập -1:")
        if n=="-1":
            break
def hienthithongtincacmonhoc():
    z=0
    print("danh sach mon hoc la:")
    for i in A:
        z+=1
        print(f"\nmon hoc thu{z}:")
        i.hienthithongtinmonhoc()
def themmonhoc():
    while(True):
        n= input("ban co muốn thêm môn học nữa không nếu không muốn nữa thì nhâp -1:")
        if n =="-1":
           break
        print("nhap vao thong tin mon hoc can them:")
        mamonhoc, tenmonhoc, sotinchi= input("nhap ma mon hoc, ten mon hoc, so tin chi ").split(",")
        a=monhoc(mamonhoc, tenmonhoc, sotinchi)
        A.append(a)
        print(f"\nmon hoc da duoc them thanh cong")
def xoamonhoc():
    while(True):
         n= input("ban co muốn xóa  môn học nữa không nếu không muốn nữa thì nhâp -1:")
         if n =="-1":
             break
         mamonhocxoa=input("nhap ma mon ma ban muon xoa:").strip()
         k=-1
         found= False
         for i in A: 
             k+=1
             if mamonhocxoa==i.mamonhoc:
                 found=True
                 break
         if found:
             A.pop(k)
             print(f"Đã xóa môn học có mã:{mamonhocxoa}")
         else:
             print(f"không tìm thấy môn học có mã:{mamonhocxoa}")
def tiemkiemmonhoc():
    while (True):
        n= input("\nban co muốn tìm môn học nữa không nếu không muốn nữa thì nhâp -1:")
        if n =="-1":
            break
        found= False
        mamonhoctim=input("nhap ma mon ma ban muon tim:").strip()
        for i in A:
            if mamonhoctim==i.mamonhoc:
                found= True
                print(f"Đã tìm thấy môn học theo mã:{i.mamonhoc}\n")
                i.hienthithongtinmonhoc()
                break
        if found== False:
             print(f"Không tìm thấy môn học vui lòng nhập lại")
def ghivaofile():
    with open("haha.txt","a",encoding="utf-8") as file:
        for i in A:
            file.write(i._str_()+"\n")
def docthongtin():
     df= pd.read_csv("haha.txt",sep=",",header= None, names=["mã môn học","tên môn học","số tín chỉ"])
     print(df)
def main():
    nhapthongtinhocsinh()
    while(True):
            print("\n===== MENU QUẢN LÝ MÔN HỌC =====")
            print("1. Hiển thị danh sách môn học")
            print("2. Thêm môn học")
            print("3. Xóa môn học")
            print("4. Tìm môn học")
            print("5. Ghi file")
            print("6. Đọc file")
            print("7. Thoát")
        
            chon = input("Chọn chức năng: ").strip()
 
            if chon == "1":
                hienthithongtincacmonhoc()
            elif chon == "2":
                themmonhoc()
            elif chon == "3":
                xoamonhoc()
            elif chon == "4":
                tiemkiemmonhoc()
            elif chon == "5":
                ghivaofile()
            elif chon == "6":
                docthongtin()
            elif chon == "7":
                print("Thoát chương trình.")
                break
            else:
                print("Chọn sai, vui lòng nhập lại.")
main()



        




     
   






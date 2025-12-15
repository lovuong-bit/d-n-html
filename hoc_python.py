a=10
b=30
c= 45.5
s="xin chao"
print(" a la {0}, b la {1} , c la {2} va s {3} ".format(a, b, c, s ))

s="hoc cong nghe"
print(type(s))


#cappitalize() Viet hoa chu dau tien trong chuoi
print(s.capitalize())


# upper() chuyen chuoi sang chu in hoa 
print(s.upper())


#lower() Chuyen chuoi tu chu in hoa sang chu thuong 
print(s.lower())


# tittle() chuyen ki tu dau moi chuoi con sang in hoa 
print(s.title())


# strip() xoa ki tu dc chi dinh o dau va moi chuoi
s="****hoc cong nghe****"
print(s.strip("*"))
s="   hoc cong nghe   "
print(s.strip()) # mac dinh xoa dau cach


# lstrip() xoa ki tu dc chi dinh o ben trai cua chuoi
s="****hoc cong nghe****"
print(s.lstrip("*"))


# split() tach cac ki tu trong chuoi 
# chuoi.split(char,n)


s1="Xin chao cac ban "
print(s1.split(" ",-1) )# tach cái gì thì để trong ngoăc kép là cái đó , muốn tách vô hạn thì để -1 


#count() dem số lần xuất hiện của 1 chuỗi con trong 1 chuoi goc 
s2="how are you i am thang"
print(s2.count("how"))
s2="how how are you i am thang"
print(s2.count("how"))


a=5e2 #5x10^2
print(a)


a= 10==11
b=10!=11
print(a)
print(b)

#and, or , not 
b=11
c=11
a=10
d=b>c and b>a 
print(d)

b=11
c=11
a=10
d=b>c or b>a 
print(d)


d= not(b>c) 
s= 0 

#list
m=list()
for i in range(1,11,1):
    m.append(i)
    i=i+1
print(m)
print(len(m))
print(m[0:11])
# them phan tu vao danh sach o vi tri bat ki 
m.insert(3,3.5)
print(m)
# xoa phan tu trong danh sach
m.__delitem__(3)
print(m)
m.remove(1)#xoa gia tri số 1 đầu tiên  trong danh sách 
print(m)
#sorted(danh sach ) sắp xếp theo giá trị tăng dần 
#sum( danh sach ) tính tổng giá trị trong danh sách 
#sorted(danh sach, reverse = True )sắp xếp theo giá trị giảm dần 

# bai tap doi cho giua phan tu dau va cuoi va phan tu thu 2 voi phan tu thu n-1
#x=list(map(int,input("nhap di thang em").split(",")))
#n=len(x)
#for i in range(n//2):
      #tmp=x[i]
      #x[i]=x[n-1-i]
      #x[n-1-i]=tmp
#print(x)






#kieu tu dien dict <key> : <value> 
#vd: ten: pham duc thang, ma hs: 1
thongtinsv= {"ten" : "pham duc thang",
             "ma hoc sing" :1, }
print(type(thongtinsv))
thongtinsv= dict({"ma sinh vien": 1,"ten sinh vien": "pham duc thang"})
print(thongtinsv)
#truy cap phan tu trong dict
#<ten bien>[<key>]
print(thongtinsv["ten sinh vien"])
#<ten bien>.get(<key>)
print(thongtinsv.get("ma sinh vien"))
#<tenbien>.values()
print(thongtinsv.values())
#<tenbien>.keys()
print(thongtinsv.keys())
# duyet qua tat ca cac phan tu trong kieu tu dien 
for i in thongtinsv:
    print(i,":", thongtinsv[i])
# nhap gia tri cho kieu tu dien 
thongtinsv1=dict({})

#n=int(input("nhap n ="))

#for i in range(n):
   # keys = input()
    #values= input()
   # thongtinsv1[keys]= values 
#print(thongtinsv1)
# xoa 1 cap key values 
# <ten bien>.__delitem__(<key>)

# xoa toan bo gia tri
#<ten bien>.clear()
thongtinsv.clear
print(thongtinsv)
#n=int(input("so mat hang hien co : "))
#dshh_lonhon60=[]
#tsl=0
#for i in range(n):
    #hang={"ten ":"","so luong":"","gia ban" : ""}

    #for j in hang:
        #print("nhap",j,":",end="")
        #giatri=input()
        #hang[j]=giatri
    #tsl+=int(hang["so luong"])
    #if int(hang["so luong"]) < 10:
       #dshh_nhohon10.append(hang)
    #if int(hang["so luong"]) > 60:
       #dshh_lonhon60.append(hang)
#print("tong so luong:",tsl)
#print("danh sach cac mat hang nho hon 10")
#for i in (dshh_nhohon10):
    #print(i)
#print("danh sach cac mat hang lon hon 60")
#for i in (dshh_lonhon60):
   # print(i)


#xay dung 1 ham 
# def ten_ham([ds_ tham _ so]):
      #ds_ cac _ lenh 
      #return


#def giaithua(a) :
     #s=1
    #for i in range(1,a +1):
        ##return s
#kq=giaithua(5)/(giaithua(3)*giaithua(5-3))
#print(kq)


#truyen tham so voi cac gia tri bat buoc
#def hoanvi(a,b):
    #a,b=b,a
    #return a,b

#def main():
    #print(hoanvi(10,20))
#main()
#truyen tham so voi gia tri mac dinh 

#import math 
#def dtdt(r=0):
    #s=math.pi*math.pow(r,2)
    #return s
#def main():
   # print("dien tich hinh tron la:", dtdt())
#main()

# Truyen tham so bang tu khoa
def tdthcn(a,b):
    s=a*b
    return s
def main():
    print("dien tich hinh chu nhat:", tdthcn(a= 4, b=5))
main()
# truyen tham so tuy y 
# tim gia tri lon nhat trong cac gia tri nhap vao ban phim
def Maxgt(*a):
    n=len(a)
    if(n==0):
      return
    else:
        max=a[0]
        for i in range(1,n):
            if max <a[i]:
               max=a[i]
    return max
#def main():
    #n= list(map(int,input("nhap gia tri:").split()))
    #for i in n:
                #k= Maxgt(i)
   # print("gia tri lon nhat la:",k)
#main()




#import math as mt
#def snt(n):
    #for i in range(2,int(mt.sqrt(n))+1):
        #if n%i==0:
           #return False
    #return True
#def main():
    #s=[]
    #a= int(input("nhap vao a= "))
    #b= int(input("nhap vao b= "))
    #for i in range(a,b+1):
        #snt(i)
        #if snt(i)== True:
          # s.append(i)
    #print("danh sach so nguyen to tu",a,"den ",b,"la",s)
#main()

s=list(map(int,input("nhap di thang em:").split(",")))
def inra(s):
    for i in s:
        print(i)
    return()
def main():
    print("danh sach hoc sinh la",inra(s))
main()

# bai tap quan ly hoc sinh 
def nhapTTHS():
    # nhap ma hs 
    while (True):
        mahs = input("nhập mã đi thằng lol: ")
        if(len(mahs.strip()))>0:
            break 
    # nhap ten hs 
    while ( True):
        tenhs= input("nhập tên đi thằng lol: ")
        if(len(tenhs.strip()))>0:
           break 
    while(True):
        diemtoan  = float(input(" nhập điểm toán đi thằng óc cak: "))
        if 0<= diemtoan <=10:
            break 
    while( True):
        diemvan =float(input(" nhập điểm văn  đi thằng óc cak: "))
        if 0<= diemvan <=10:
            break 
    return{"mã học sinh":mahs,"tên học sinh":tenhs,"điểm toán": diemtoan, "điểm văn":diemvan}
def nhapdshs():
    dshs= []
    while(True):
        n = int(input("nhap so hoc sinh:"))
        if n >0:
            break 
    for i in range(1, n+1):
        print("nhap thong tin hoc sinh thu", i ,":")
        dshs.append(nhapTTHS())
    return dshs
def diemtb(diemtoan, diemvan):
     return (diemtoan + diemvan)/2
def xeploai(dtb):
    xl=""
    if 9<= dtb <= 10:
        xl = "xuat sac "
    elif 8<= dtb < 9:
        xl = "gioi"
    elif 7<= dtb <8 :
        xl ="kha"
    elif 5<= dtb < 7 :
        xl = "trung binh "
    else: xl = "yeu "
    return xl 
def inTTHS(dshs):
    for i in range(len(dshs)):
        print ("thong tin cua hoc sinh thu", i+1)
        print("ma hc sinh",dshs[i]["mã học sinh"])
        print("ten hoc sinh",dshs[i]["tên học sinh"])
        print("diem toan", dshs[i]["điểm toán"])
        print("diem van", dshs[i]["điểm văn"])
        dtb = diemtb(dshs[i]["điểm toán"], dshs[i]["điểm văn"])
        print("diem trung binh",dtb)
        xl = xeploai(dtb)
        print("xep loai", xl)
def main():
    dshs = nhapdshs()
    inTTHS(dshs)
main()






    
def nhappt():
pt ={}
while(True):
        mu =int(input("nhap mu:"))
        if mu==-1:
            break 
        hso =float(input("nhap he so:"))
        if hso!=0:
            pt[mu]=hso
return pt
def hienthi(pt):
chuoidathuc=""
for mu in sorted(pt.keys()):
    if(pt[mu]>0):
        chuoidathuc+="+"+str(pt[mu]) + "*x^"+ str(mu)
    else:
        chuoidathuc+=str(pt[mu]) + "*x^"+ str(mu)
print("p=",chuoidathuc)
def tong(pt1,pt2):
pttong= {}
# XÉT MŨ CÓ TRONG PT 1 
for mu in pt1:
    if( mu in pt2):
        pttong[mu]= pt1[mu] + pt2[mu]
    else:
        pttong[mu]=  pt1[mu]
    # XÉT MŨ CÓ TRONG PT 2 
for  mu in pt2:
        if( mu not in pt1):
            pttong[mu]= pt2[mu] 
return pttong 
def tinhgtdt(pt,x ):
return sum(pt[mu]*(x** mu) for mu in pt )
def main():
print("nhap da thuc 1")
pt1= nhappt()
print("nhap da thuc 2")
pt2= nhappt()


print("tong 2 da thuc")
pttong= tong(pt1, pt2)
hienthi(pt1)
hienthi(pt2)
hienthi(pttong)
    
x= int(input("nhap x đi thằng em:"))

print("gia tri cua da thuc 1 tai x =",x,"la", tinhgtdt(pt1,x))
main()


# baì tập nhập và lưu vào file text thông tin học sinh

def shs():
    while(True):
          a= int(input("nhap di thang em:"))
          if a > 0: 
            break 
    return a 
def nhapthongtin():
    # nhap ma hoc sinh:
    while(True):
        ma=input("nhap ma di thang lon:")
        if len(ma)> 0:
            break 
    # nhap ten hoc sinh:
    while(True):
        ten=str(input("nhap ten di thang lon :"))
        if len(ten)>0:
            break 
    # nhap que quan 
    while(True):
        que =str(input("nhap ten di thang lon :"))
        if len(que)>0 :
            break 
    # nhap năm sinh
    while(True):
        namsinh= input("nhap nam sinh di thang lon:")
        if len(namsinh)>0:
            break 
    return{"ma hoc sinh":ma,"ten hoc sinh":ten, "que quan":que,"nam sinh": namsinh}
def nhapdshs():
    s=[]
    n= shs()
    for i in range(1, n+1):
        print("nhap thong tin hs thu ",i,":")
        s.append(nhapthongtin())
    return(s)
def luuthongtin():
    file= open("haha.txt",'a',encoding='utf-8')
    for i in nhapdshs():
        file.write(str(i)+"\n")
    file.close()
def main():
    luuthongtin()
main()

# cach 2:
n = int(input(" nhap di thang em:"))
for i in range(n):
    with open("haha.txt","a",encoding= "utf-8") as file:
    ma= input("nhap ma:")+"\n"
    ten= input("nhap ten:")+"\n"
    que = input("nhap que:")+"\n"
    namsinh = input("nhap nam sinh:")+"\n"
    filewritelines([ma,ten,que,namsinh])

import pandas as pd 

df=pd.read_csv("haha.csv",sep =",", header= None, names= ["ma","ten","lop","que quan"])
print(df)
#df1=pd.read_excel("haha.xlsx",sheet_name="Sheet2",header =None)
df1=df.sort_values(["lop"], ascending = False  )
print(df1)



import pandas as pd 

df=pd.read_csv("haha.csv",sep =",", header= None, names= ["ma","ten","lop","que quan"])
print(df)
#df1=pd.read_excel("haha.xlsx",sheet_name="Sheet2",header =None)
qq=["Thai Nguyen","NamDinh"]
df1=df.query('`que quan` in @qq')
print(df1)


import pandas as pd 
import math as mt 
n= int(input("nhap so can ho:"))
def nhapthongtin():
    while(True):
        maho= input("nhap ma ho:")
        if len(maho.strip()) >0:
            break
    while(True):
        tenchuho= input("nhap ten chu ho:")
        if len(tenchuho.strip())>0:
            break
    while(True):
        diachi= input("nhap dia chi:")
        if len(diachi.strip())>0:
            break 
    while(True):
        kw= input("nhap so KW :")
        if float(kw) >= 0:
            break 
    return[maho,tenchuho,diachi,kw]
def tinhtien(k):
    z=(10/100,)
    if k <= 100:
        k *=1500
    elif k > 100 and k<200:
         k-=100
         k= k*2000+100*1500
    elif k>200 and k <300:
         k-=200
         k=k*2500+ 100*(1500+2000)
    else:
         k-=300 
         k=k*3000+ 100*(1500+2000+2500)
    k += z[0]*k 
    return(k)
def luuthongtin():
    with open("data.txt","a",encoding="utf-8") as file:
         # số hộ bằng số lần nhập
         for i in range(1,n+1):
             z=nhapthongtin() # nhập thông tin mỗi hộ này 
             z.append(str(tinhtien(float(z[3])))) # chuyển số kw nhập vào từ kiểu dữ liệu str qua float dùng hàm tinhtien()
                                                   #tính rồi chuyển lại thành str và thêm vào danh sách 
             l=",".join(z) # dùng lệnh "sep".join(list hoặc tupple)( chỉ dùng để ghép các chuỗi str , không dành cho int, float)
             file.write(l+"\n") 
def bangthongtin():
    df=pd.read_csv("data.txt",sep =",", header= None, names= ["ma ho","ten chu ho","dia chi","so kw dung","so tien phai tra"])
    print(df)
def main():
    luuthongtin()
    bangthongtin()
main()


class SinhVien:
    def __init__(self, hoten, quequan, lop , diempython, diemtkweb):
        self.hoten= hoten
        self.quequan=quequan
        self.lop=lop
        self.diempython= diempython
        self.diemtkweb = diemtkweb
sv1= SinhVien("pham duc thang","ninh binh","A1",8 , 9)
print(type(sv1))
print(sv1.hoten)








# Membuat lis kosong agar data tidak tumpang tindih

listpilihan=[]
listjb=[]
listharga=[]
listjenis=[]
listtb=[]
listbonus=[]

totalitem=0
totalkesewluruhan=0

def garis():
    print("="*150)

print("TOKO HERBAL ALIBABA".center(70))
garis()
print("1. MADU HUTAN")
print("2. TEH HIJAU")
print("3. SARI KURMA")
garis()
kasir=input("Nama Kasir : ")
j=int(input("Masukan jumlah data : "))

for i in range(j):
    print("Data ke :", i+1)
    pilihan=int(input("Pilihan[1/2/3] :"))
    listpilihan.append(pilihan)
    jb=int(input("Jumlah Beli :"))
    listjb.append(jb)

if(listpilihan[i]==1):
    listjenis.append ("Madu Hutan")
    listharga.append (120000)
elif (listpilihan[i]==2):
    listjenis.append("Teh Hijau")
    listharga.append(20000)
else : 
    listjenis.append("Sari Kurma")
    listharga.append(80000)

listtb.append(listjb[i]*listharga[i])

if listjb[i]>=10:
    listbonus.append("Pounch Cantik")
else:
    listbonus.append("Tidak Dapat Bonus")

print("TOKO HERBAL ALIBABA".center(70))
print("Kasir", kasir)
garis()
print("No.Jenis  Harga  Jumlah Beli  Total Bayar")
garis()

for i in range(j):
    print("%d %s  Rp.%d  %d  Rp.%d  %s"%(j+1,listjenis[i],listharga[i],listtb[i],listtb[i],listbonus[i]))
    totalitem=totalitem+listjb[i]
    totalkesewluruhan=totalkesewluruhan+listtb[i]

garis()
print("Total Item=%d"%totalitem)
print("Total Keseluruhan Rp.%d"%totalkesewluruhan)
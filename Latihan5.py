v_nim=[]
v_nama=[]
v_tugas=[]
v_uts=[]
v_uas=[]
v_akhir=[]

def judul():
    print("======================================")
    print("Program Input Data")
    print("======================================")

def menu():
    judul()
    print("======================================")
    print("|1. Lihat Data Mahasiswa             |")
    print("|2. Tambah Data Mahasiswa            |")
    print("|3. Ubah Data Mahasiswa              |")
    print("|4. Hapus Data Mahasiswa             |")
    print("|5. Cari Data Mahasiswa              |")
    print("|6. Keluar                           |")
    print("======================================")
    pilih2=input("pilih menu : ")
    if pilih2 == "1":
        lihat()
    elif pilih2 == "2":
        tambah()
    elif pilih2 == "3":
        ubah()
    elif pilih2 == "4":
        hapus()
    elif pilih2 == "5":
        cari()
    elif pilih2 == "6":
        keluar()
    else:
        tidak = input("menu tidak tersedia")
        menu()


def lihat():
    judul()

    for i in range (len(v_nim)):
        print("%d. Nim        :%s" %(i+1, v_nim[i]))
        print(" Nama         :%s" %v_nama[i])
        print(" Nilai Tugas  :%s" %v_tugas[i])
        print(" Nilai UTS    :%s" %v_uts[i])
        print(" Nilai UAS    :%s" %v_uas[i])
        print(" Niali Akhir  :%s" %v_akhir[i])
        print("_________________________________________")
        print("Daftar Nilai")
        print("=========================================")
        print(" No.  NiM   Nama.  Tugas   UTS  UAS  AKHIR  ")
        print("=========================================")

    kembali= input("kembalai tekan [enter]")
    menu()

def tambah():
    judul()
    print("Tambahkan Data Mahasiswa".center(40))
    print("========================================")
    nama= input("Nama : ")
    v_nama.append(nama)
    nim= input (" NIM : ")
    v_nim.append(nim)
    tugas=float(input("Niali Tugas : "))
    n_tugas= tugas*(30/100)
    v_tugas.append(n_tugas)
    uts=float(input("Niali UTS : "))
    n_uts= uts*(35/100)
    v_uts.append(n_uts)
    uas=float(input("Niali UAS : "))
    n_uas= uas*(35/100)
    v_uas.append(n_uas)
    total= n_tugas + n_uts + n_uas
    v_akhir.append(total)
    print("Simpan Data".center(40))
    kembali= input ("kembali[enter]")
    menu()

def ubah():
    rubah = input ("Ubah Biodata / niali :")
    if rubah == "B" or rubah == "b" :
        i = int(input("Masukan id : "))
        if (i > len(v_nim[i])):
            print ("id salah")
        else :
            nama_baru=input("Nama : ")
            v_nama[i]= nama_baru
            nim_baru=input("NIM : ")
            v_nim[i]= nim_baru

    else :
        i=int(input("Masukan id : "))
        if(i>len(v_nim[i])):
            print ("id salah")
        else:
            tugas_baru=float(input("Niali Tugas : "))
            n_tugasbaru = tugas_baru * (30 / 100)
            v_tugas[i]=n_tugasbaru
            uts_baru=float(input("Nilai UTS : "))
            n_utsbaru= uts_baru * (35/100)
            v_uts[i]=n_utsbaru
            uasbaru=float(input("Nilai UAS : "))
            n_uasbaru=uasbaru * (35/100)
            v_uas[i]=n_uasbaru
            totalbaru= n_tugasbaru + n_utsbaru + n_uasbaru
            v_akhir[i]=totalbaru

    kembali = input("kembali[enter]")
    menu()

def hapus():
    judul()
    print("Hapus Data Mahasiswa".center(40))
    print("=================================================")
    i=int(input("Masukan id : "))
    if (i>len(v_nim[i])):
        tidak = input ("Nim Tidak Ada")
        hapus()
    else:
        v_nim.remove(v_nim[i])
        v_nama.remove(v_nama[i])
        v_tugas.remove(v_tugas[i])
        v_uts.remove(v_uts[i])
        v_uas.remove(v_uas[i])
        v_akhir.remove(v_akhir[i])

    print("Data berhasil dihapus")
    kembali= input("kembali[enter]")
    menu()
def cari():
    judul()
    print("Cari Data Mahasiswa".center(40))
    print("======================================================")
    i=int(input("Masukan id"))
    if (i>len(v_nim[i])):
        tidak = input("Nim Tidak Ada")
        cari()
    else:
        lihat()

    print("Data Mahasiswa Ditampilkan")
    kembali= input("kembali[enter]")
    menu()

def keluar():
    menu()

menu()

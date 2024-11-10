from list import *

# DEFINISI DAN SPESIFIKASI TYPE
# type Mhs : <nim:string, nama:string, kelas;character, nilai:list of integer>
# 	{type Mhs terdiri atas nim, nama, dan kelas mahasiswa, serta kumpulan nilai kuis yang pernah dikerjakan, dengan maksimal jumlah mengerjakan adalah 10 kali. Nilai mahasiswa memiliki rentang antara 0-100}

# DEFINISI DAN SPESIFIKASI SELEKTOR
# GetNIM : Mhs --> string
# 	{Selektor untuk mengambil elemen NIM dari type Mhs}

# GetNama : Mhs --> string
# 	{Selektor untuk mengambil elemen Nama dari type Mhs}

# GetKelas : Mhs --> char
# 	{Selektor untuk mengambil elemen Kelas dari type Mhs}

# GetNilai : Mhs --> list of integer
# 	{Selektor untuk mengambil elemen Nama dari type Mhs}

# Realisasi
def GetNIM (MHS):
    return MHS [0]

def GetNama (MHS):
    return MHS [1]

def GetKelas (MHS):
    return MHS [2]

def GetNilai (MHS):
    return MHS [3]

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakeMhs: string, string, character, list of integer  --> Mhs
#   {MakeMhs(nim, nama, kelas, nilai) membentuk sebuah mahasiswa dengan dengan nim, nama, kelas dan nilai berbentuk list of integer.

# Realisasi
def MakeMHS (nim,nama,kelas,nilai):
    return [nim,nama,kelas,nilai]

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakeSetMhs: Mhs, set_of_mhs  --> set_of_mhs
#   {MakeSetMhs(M,H) Menambahkan mahasiswa mhs ke dalam setMHS dengan syarat saat menambahkan elemen mahasiswa baru harus menggunakan nim yang unik.

# Realisasi 
def MakeSetMhs(M,H):
    if IsEmpty(H):
        return [M]
    else:
        if GetNIM(M) == GetNIM(FirstElmt(H)):
            return H
        else:
            return Konso(FirstElmt(H), MakeSetMhs(M,Tail(H)))

# DEFINISI DAN SPESIFIKASI OPERATOR
# Jumlah_Lulus: set_of_mhs --> set_of_mhs 
#   {Jumlah_Lulus(HM) Mengembalikan banyaknya mahasiswa yang lulus (nilai rata-rata >= 70) dari semua kelas

# NotQuiz: Charcater, set_of_mhs --> set_of_mhs
#   {NotQuiz(Cls,HM) Mengembalikan himpunan mahasiswa yang tidak mengerjakan kuis di kela.}

# NilaiTertinggi: set_of_mhs --> integer
# {NilaiTertinggi(HM) Mengembalikan nilai tertinggi dari semua kelas.}

# TertinggiKelas: Charracter, set_of_mhs --> set_of_mhs
# {Mengembalikan mahasiswa yang mendapatkan nilai tertinggi di kelas class_name.}

# Jumlah_Tidak_Mengerjakan: set_of_mhs: --> integer
# {Mengembalikan banyaknya mahasiswa yang tidak mengerjakan kuis dari semua kelas.}

# Lulus: set_of_mhs --> set_of_mhs
# { Lulus(set_of_mhs ) Mengembalikan himpunan mahasiswa yang lulus (nilai rata-rata >= 70).


def Jumlah_Lulus(HM):
    if IsEmpty(HM):
        return []
    else:
        if AvgElmt(GetNilai(FirstElmt(HM))) >= 70:
            return MakeSetMhs(FirstElmt(HM),Jumlah_Lulus(Tail(HM)))
        else:
            return Jumlah_Lulus(Tail(HM))
        
def NotQuiz(Cls,HM):
    if IsEmpty(HM):
        return []
    else:
        if GetKelas(FirstElmt(HM)) == Cls and IsEmpty(GetNilai(FirstElmt(HM))):
            return MakeSetMhs(FirstElmt(HM),NotQuiz(Cls,Tail(HM)))
        else:
            return NotQuiz(Cls,Tail(HM))
        
def NilaiTertinggi(HM):
    if IsOneElmt(HM):
        return AvgElmt(GetNilai(FirstElmt(HM)))
    else:
        if AvgElmt(GetNilai(FirstElmt(HM))) <= AvgElmt(GetNilai(FirstElmt(Tail(HM)))):
            return NilaiTertinggi(Tail(HM))
        else:
            return NilaiTertinggi(MakeSetMhs(FirstElmt(HM),Tail(Tail(HM))))
        
def TertinggiKelas(Cls,HM):
    if IsOneElmt(HM):
        if GetKelas(FirstElmt(HM)) == Cls:
            return FirstElmt(HM)
    else:
        if GetKelas(FirstElmt(HM)) == Cls:
            if AvgElmt(GetNilai(FirstElmt(HM))) <= AvgElmt(GetNilai(FirstElmt(Tail(HM)))):
                return TertinggiKelas(Cls,Tail(HM))
            else:
                return TertinggiKelas(Cls,MakeSetMhs(FirstElmt(HM),Tail(Tail(HM))))
        else:
            return TertinggiKelas(Cls,Tail(HM))
        
def Jumlah_Tidak_Mengerjakan(HM):
    if IsEmpty(HM):
        return 0
    else:
        if IsEmpty(GetNilai(FirstElmt(HM))):
            return 1 + Jumlah_Tidak_Mengerjakan(Tail(HM))
        else:
            return Jumlah_Tidak_Mengerjakan(Tail(HM))
        
def Lulus(HM):
    if IsEmpty(HM):
        return 0
    else:
        if AvgElmt(GetNilai(FirstElmt(HM))) >= 70:
            return 1 + Lulus(Tail(HM))
        else:
            return Lulus(Tail(HM))


print(Jumlah_Lulus([["24001", "Budi", 'A', [85,99,90]], ["24002", "Ayu", 'B', [22,11,73]],  ["24003", "Dewi", 'C', [11,100,100]]]))
print(NotQuiz('A',[["24001", "Budi", 'A', [85,99,90] ], ["24002", "Ayu", 'B', [22,11,73]],  ["24003", "Dewi", 'C', []]]))
print(NilaiTertinggi([["24001", "Budi", 'A', [85,99,90]], ["24002", "Ayu", 'B', [22,11,73]],  ["24003", "Dewi", 'C', [11,100,100]]]))
print(TertinggiKelas('C',[['24001', "Budi", 'A', [85,99,90]], ["24002", "Ayu", 'C', [22,11,73]] , ["24003", "Dewi", 'C', [100,100,100]]]))
print(Jumlah_Tidak_Mengerjakan([["24001", "Budi", 'A',[]], ["24002", "Ayu", 'B', [22,11,73]] , ["24003", "Dewi", 'C', [100,100,100]]]) )
print(Lulus([["[24001", "Budi", 'A', [5,9,9]], ["24002", "Ayu", 'B', [22,11,73]] , ["24003", "Dewi", 'C', [100,100,100]]]) )

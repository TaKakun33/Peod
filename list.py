# Nama File: list.py
# Deskripsi: berisi type dan operasi list
# Pembuat: Akmal Kafli Anan
# Tanggal: 28 Oktober 2024

# DEFINISI DAN SPESIFIKASI TYPE
# Konstruktor menambahkan elemen di awal, notasi prefix
# type List: () atau [e o List]
# Konstruktor menambahkan elemen di akhir, notasi postfis
# type List: () atau [List o e]

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# Konso: elemen, List -> List
#   {Konso(e,L) menghasilkan sebuah list dari e dan L dengan e sebagai elemen pertama}
# 
# Konsi: List, elemen -> List
#   {Konsi (L,e) -> menghasilkan sebah list dari L dan e dengan e sebagai elemen terakhir}

# Realisasi
def Konso(e,L):
    return [e] + L

def Konsi(L,e):
    return L + [e]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstElmt: List tidak kosong -> elemen
#   {FirstElmt(L) Menghasilkan elemen pertama list L}
# 
# LastElmt: List tidak kosong -> elemen
#   {LastElmt(L): mengembalikan elemen terakhir terakhir list L}
# 
# Tail: List tidak kosong -> List
#   {Tail(L): Menghasilkan list tanpa elemen pertama list L, mungkin kosong}
# 
# Head: List tidak kosong -> List
#   {Head(L): Menghasilkan list tanpa elemen terakhir list L, mungkin kosong}

# Realisasi
def FirstElmt(L):
    return L[0]

def LastElmt(L):
    return L[-1]

def Tail(L):
    return L[1:]

def Head(L):
    return L[:-1]
        
# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEmpty List -> boolean
#   {IsEmpty(L) benar jika list kosong}
# 
# IsOneElmt: List -> boolean
#   {IsOneElmt (X,L) adalah benar jika list L hanya mempunyai satu elemen}
# 
# IsMember: elemen, List -> boolean
#   {Ismember (X,L) adalah benar jika X adalah elemen list L}
# 
# IsPalindrom(L): List of character -> boolean
#   {IsPalindrom(L) benar jika L merupakan kata palindrom yaitu kata yang sama jika dibaca dari kiri atau kanan}

# Realisasi
def IsEmpety(L):
    return L == []
        
def IsOneElmt(L):
    if IsEmpety(L):
        return False
    else:
        return Tail(L) == [] and Head(L) == []
        
def IsMember(X,L):
    if IsEmpety(L):
        return False
    else:
        if FirstElmt(L) == X:
            return True
        else:
            return IsMember(X,Tail(L))
        
def IsPalindrom(L):
    if IsEmpety(L):
        return True
    elif IsOneElmt(L):
        return True
    else:
         return FirstElmt(L) == LastElmt(L) and IsPalindrom(Head(Tail(L)))
    
# DEFINISI DAN SPESIFIKASI FUNGSI YANG MENGOPERASIKAN LIST
# NbElmt: List → integer
#   {NbElmt (L): Menghasilkan banyaknya elemen list, nol jika kosong}
# 
# ElmtkeN: integer 20, List elemen
#   {ElmtkeN (N, L): Mengirimkan elemen list yang ke N, N≤ NbELmt (L) dan N>=0}
# 
# IsMember: elemen, List boolean
#   {Ismember (X,L) adalah benar jika X adalah elemen list L}
# 
# Copy: List → List
#   {Copy(L): Menghasilkan list yang identik dengan list asal}
# 
# Inverse: List -> List
#   (Inverse(L): Menghasilkan list L yang dibalik, yaitu yang urutan elemennya adalah kebalikan dari list asal)
# 
# Konkat: 2 List -> List
#   {Konkat (L1,L2): Menghasilkan konkatenasi 2 buah list, dengan list L2 "sesudah" list L1}
# 
# SumElmt: List of integer -> integer
#   {SumElmt(L) menghasilkan jumlahan dari setiap elemen di list L}
# 
# AvgElmt: List of integer -> integer
#   {AvgEmlt(L) menghasilkan nilai rata-rata}
# 
# MaxElmt (L): List of integer -> integer 
#   {MaxElmt(L) mengembalikan elemen maksimum dari list L}
# 
# NbOcc: integer, list of integer -> integer > 0
#   {NbOcc(X, Li) yaitu banyaknya kemunculan nilai X pada Li}
# 
# MaxNB: List of integer -> <integer, integer>
#   {MaxNB(L) menghasilkan <max, countMax> dengan max adalah elemen maksimum list L dan countMax adalah banyaknya kemunculan max di list L}
# 
# AddList: 2 List of integer -> List of integer
#   {AddList (L1, L2) menghasilkan list baru yang setiap elemennya adalah hasil penjumlahan setiap elemen di L1 dan L2 pada posisi yang sama}
        
# Realisasi
def NbElmt(L):
    if IsEmpety(L):
        return 0
    else:
        return 1 + NbElmt(Tail(L))

def ElmtkeN(n,L):
    if n == 1:
        return L[0]
    else:
        return ElmtkeN(n-1,Tail(L))
        
def Copy(L):
    if IsEmpety(L):
        return []
    else:
        return Konso(FirstElmt(L),Copy(Tail(L)))
        
def Inverse(L):
    if IsEmpety(L):
        return []
    else:
        return Konsi(Inverse(Tail(L)), FirstElmt(L))
    
def Konkat(L1,L2):
    if IsEmpety(L2):
        return L1
    else:
        return Konsi(Konkat(L1,Tail(L2)),FirstElmt(L2))
    
def SumElmt(L):
    if IsEmpety(L):
        return 0
    else:
        return FirstElmt(L) + SumElmt(Tail(L))
    
def AvgElmt(L):
    if IsEmpety(L):
        return 0
    else:
        return SumElmt(L) / NbElmt(L)   
    
def MaxElmt(L):
    if IsOneElmt(L):
        return FirstElmt(L)
    else:
        if FirstElmt(L) <= FirstElmt(Tail(L)):
            return MaxElmt(Tail(L))
        else:
            return MaxElmt(Konso(FirstElmt(L),Tail(Tail(L))))

def NbOcc(x,L):
    if IsOneElmt(L):
        if x == FirstElmt(L):
            return 1
        else:
            return 0
    else:
        if x == FirstElmt(L):
            return 1 + NbOcc(x,Tail(L))
        else:
            return  NbOcc(x,Tail(L))

def MaxNB(L):
    if IsEmpety(L):
        return [0,0]
    else:
        return [MaxElmt(L),NbOcc(MaxElmt(L),L)]

def AddList(L1,L2):
    if IsEmpety(L1) and IsEmpety(L2):
        return []
    elif IsEmpety(L1) and not IsEmpety(L2):
        return L2
    elif not IsEmpety(L1) and IsEmpety(L2):
        return L1
    else:
        return Konso(FirstElmt(L1) + FirstElmt(L2), AddList(Tail(L1),Tail(L2)))
    
# Aplikasi
print(IsEmpety([]))
print(IsOneElmt([2]))
print(IsMember(2,[4,5,6,7,8,9,0]))
print(IsPalindrom(['t','e','n','e','t']))

print(ElmtkeN(3,[4,5,6,7,8,9,0]))
print(Copy([4,5,6,7,8,9,0]))
print(Inverse([4,5,6,7,8,9,0]))
print(Konkat([1,2,3],[9,8,7]))
print(SumElmt([1,2,3,5,6]))
print(AvgElmt([1,2,3]))
print(MaxElmt([1,1,1,1]))
print(NbOcc(7,[1,2,7,7,9,9,5,5,9]))
print(MaxNB([1,2,7,7,9,9,5,5,9]))
print(AddList([1,2,3,10],[4,7,6]))
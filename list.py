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
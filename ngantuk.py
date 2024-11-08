from list import *

def MakeMHS (nim,nama,kelas,nilai):
    return [nim,nama,kelas,nilai]

def GetNIM (MHS):
    return MHS [0]

def GetNama (MHS):
    return MHS [1]

def GetKelas (MHS):
    return MHS [2]

def GetNilai (MHS):
    return MHS [3]

def MakeSetMhs(M,H):
    if IsEmpty(H):
        return [M]
    else:
        if GetNIM(M) == GetNIM(FirstElmt(H)):
            return H
        else:
            return Konso(FirstElmt(H), MakeSetMhs(M,Tail(H)))
        
def avg(HM):
    if IsEmpty(HM):
        return []
    else:
        if AvgElmt(GetNilai(FirstElmt(HM))) >= 70:
            return MakeSetMhs(FirstElmt(HM),avg(Tail(HM)))
        else:
            return avg(Tail(HM))
        
def MaxMHS(HM):
    if IsOneElmt(HM):
        return HM
    else:
        if AvgElmt(GetNilai(FirstElmt(HM))) <= AvgElmt(GetNilai(FirstElmt(Tail(HM)))):
            return MaxMHS(Tail(HM))
        else:
            return MaxMHS(MakeSetMhs(FirstElmt(HM),Tail(Tail(HM))))
        
def NotQuiz(Cls,HM):
    if IsEmpty(HM):
        return []
    else:
        if GetKelas(FirstElmt(HM)) == Cls and IsEmpty(GetNilai(FirstElmt(HM))):
            return MakeSetMhs(FirstElmt(HM),NotQuiz(Cls,Tail(HM)))
        else:
            return NotQuiz(Cls,Tail(HM))
        
def MaxMHS2(Cls,HM):
    if IsOneElmt(HM):
        if GetKelas(FirstElmt(HM)) == Cls:
            return HM
        else:
            []
    else:
        if AvgElmt(GetNilai(FirstElmt(HM))) <= AvgElmt(GetNilai(FirstElmt(Tail(HM)))) and GetKelas(FirstElmt(HM)) != Cls:
            return MaxMHS2(Cls,Tail(HM))
        else:
            return MaxMHS2(Cls,MakeSetMhs(FirstElmt(HM),Tail(Tail(HM))))
        
def NotQuizAll(HM):
    if IsEmpty(HM):
        return 0
    else:
        if IsEmpty(GetNilai(FirstElmt(HM))):
            return 1 + NotQuizAll(Tail(HM))
        else:
            return NotQuizAll(Tail(HM))
        
def TotalMHSLulus(HM):
    if IsEmpty(HM):
        return 0
    else:
        if AvgElmt(GetNilai(FirstElmt(HM))) >= 70:
            return 1 + TotalMHSLulus(Tail(HM))
        else:
            return TotalMHSLulus(Tail(HM))


usop = MakeMHS('24120024','sopi','c',[90,66,78])
fel = MakeMHS('12345','Supi','a',[])

print(GetNIM(usop))
print(GetNama(usop))
print(GetKelas(usop))
print(GetNilai(usop))
print(MakeSetMhs(usop,[['12345','Supi','a',[]],['665564','basil','b',[99,98]]]))
print(MakeSetMhs(fel,[['12345','Supi','a',[]],['665564','basil','b',[99,98]]]))

mmmm = (MakeSetMhs(usop,[['12345','Supi','a',[]],['665564','basil','b',[99,98]]]))
print(avg(mmmm))
print(MaxMHS(mmmm))

heheheh = [['12345','fery','a',[20,30,40]],['8887','dert','a',[]],['4432','asil','b',[]],['86778','dder','b',[]],['243244','fuad','b',[100,100,100]]]
print(NotQuiz('a',heheheh))
print(NotQuiz('b',heheheh))

print(MaxMHS2('a',heheheh))
print(MaxMHS2('b',heheheh))

print(NotQuizAll(heheheh))

print(TotalMHSLulus(heheheh))
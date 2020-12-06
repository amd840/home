from Pyfhel import Pyfhel,PyCtxt,PyPtxt


def getP():
    # need to generate Pk here
    p = 10
    return p

def getEncInt(p, m,i):
    HE = Pyfhel.Pyfhel()
    HE.contextGen(p=p, m=m, base=3, flagBatching=True)  # Generating context.
    HE.keyGen()
    return HE.encryptInt(i)

def getDecInt(p,m,i):
    HE = Pyfhel.Pyfhel()
    HE.contextGen(p=p, m=m, base=3, flagBatching=True)  # Generating context.
    HE.keyGen()
    return HE.decryptInt(i)

def getEncArray(txt):
    strArr = []
    for x in txt:
        strArr.append(HE.encryptInt(ord(x)))
    return strArr

def getDecryptedString(arr):
    strResult = ""
    for x in arr:
        strResult+=(chr(HE.decryptInt(x)))
    return strResult

def txtToInt(str):
    intvalue = 0
    count = 0
    n = 3

    for x in str:
        intvalue = intvalue * 10000 + ord(x)
        count += 1
    return intvalue

def intTotxt(intger):
    n = 4

    strInt = str(intger)
    if((len(strInt)%4)==1):
        strInt = "0" + strInt
    elif((len(strInt)%4)==2):
        strInt = "00" + strInt
    elif ((len(strInt) % 4) == 3):
        strInt = "000" + strInt
    result = ""
    for x in range(int(len(str(intger)) / n + 1)):
        index = x * n
        result += chr(int(strInt[index:index + n]))
    return result

first = txtToInt("ahmed")
print(first)
print(intTotxt(first))


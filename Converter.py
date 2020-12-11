def Encode(txt):
    intvalue = 0
    for x in txt:
        intvalue = intvalue*1000 + ord(x)
    return intvalue

def Decode(number):
    number="0"+str(number)
    result=""
    for x in range(int(len(number[1:])/3)+1):
        index = x*3
        result += chr(int(number[index:index+3]))
    return result





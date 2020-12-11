import json
import random
from paillier.crypto import secure_addition, scalar_multiplication, secure_subtraction


def lineLen(len):
    if(len<10):
        return '00'+str(len)
    elif(len<100):
        return '0'+str(len)
    else:
        return str(len)



def addFile(filename,pk):
    id = -1
    wrongRand = True
    fileContent = None
    files = None

    while wrongRand:
        wrongRand = False
        id = random.randint(10000000,99999999)

        fileContent = {"id":id,
            "filename":filename,
            "content":[""],
            "pk":pk  
            }
        fileContent = json.dumps(fileContent)
        file =  open("server.js")
        files = file.read()
        files = json.loads(files)
        
        for f in files:
            if(f["id"]==id):
                wrongRand = True
        print(fileContent)
    files.append(json.loads(fileContent))
    file =  open("server.js","w")
    json.dump(files,file)
    print("FIle",files)
    file.close
    return id


#addFile("123",[123,212])

def openfile(id,pk):
    file =  open("server.js")
    files = file.read()
    files = json.loads(files)
    for f in files:
        if(f["id"]==id and f["pk"]==pk):
            return f

def saveFile(file):
    files = file.read()
    files = json.loads(files)
    files.append(json.loads(file))
    file =  open("server.js","w")
    json.dump(files,file)




def replace(file,linenum,newtext,linelen):
    fileCon = file["content"]
    if(len(fileCon)<=linenum):
        fileCon[linenum-1] = newtext + ':'+lineLen(linelen)
        file["content"] = fileCon
        return file
    else:
        return None
def appendNewLine(file,newtext,linelen):
    fileCon = file["content"]
    print(len(fileCon))
    if(fileCon[len(fileCon)-1]==''):
        fileCon[len(fileCon)-1] = newtext + ':'+ lineLen(linelen)
    else:
        fileCon.append(newtext + ':'+lineLen(linelen))
    file["content"] = fileCon
    return file

#Need To be Homo
def appendAtTheEnd(file,newtext,linelen):
    fileCon = file["content"]  
    n =  len(fileCon[len(fileCon)-1]) - fileCon[len(fileCon)-1].index(':') - 1
    print(n)
    #len is encrypted

    oldlen = int(fileCon[len(fileCon)-1][-n:])
    #ask client to get new length encrypted
    enclen = 999 # from the client
    #ask client to get new length decrypted
    declen = 10 # from the client
    if(declen<200):
        Scale = 10**(declen+1)
        oldtext = fileCon[len(fileCon)-1][:-n]
        oldtext = scalar_multiplication(oldtext, Scale, file["pk"][0])
        fileCon[len(fileCon)-1] = secure_addition(oldtext, newtext, n) + ':'+ enclen
        file["content"] = fileCon
        return file
    else:
        return None
#Need To be Homo
def appendAtTheEndOfLine(file,linenum,newtext,linelen):
    fileCon = file["content"]  
    n =  len(fileCon[linenum-1]) - fileCon[linenum-1].index(':') - 1
    print(n)
    #len is encrypted

    oldlen = int(fileCon[linenum-1][-n:])
    #ask client to get new length encrypted
    enclen = 999 # from the client
    #ask client to get new length decrypted
    declen = 10 # from the client
    if(declen<200):
        Scale = 10**(declen+1)
        oldtext = fileCon[linenum-1][:-n]
        oldtext = scalar_multiplication(oldtext, Scale, file["pk"][0])
        fileCon[linenum-1] = secure_addition(oldtext, newtext, n) + ':'+ enclen
        file["content"] = fileCon
        return file
    else:
        return None
def insert(file,linenum,newtext,linelen):
    fileCon = file["content"]
    if(linelen<200):
        fileCon.insert(linenum,newtext + lineLen(linelen))
        file["content"] = fileCon
        return file
    else:
        return None
def remove(file,linenum):
    fileCon = file["content"]
    if(linelen<200):
        fileCon.remove(linenum,newtext + lineLen(linelen))
        file["content"] = fileCon
        return file
    else:
        return None

def editfile(file,fanction,linenum,text,linelen):
    if(fanction=="replace"):
        file = replace(file,linenum,text,linelen)
    elif(fanction=="appendAE"):
        file = appendAtTheEnd(file,text,linelen)
    elif(fanction=="appendNL"):
        file = appendNewLine(file,text,linelen)
    elif(fanction=="appendAL"):
        file = appendAtTheEndOfLine(file,linenum,text,linelen)
    elif(fanction=="insert"):
        file = insert(file,linenum,text,linelen)
    elif(fanction=="remove"):
        file = remove(file,text)
        x = 0
    elif(fanction=="clear"):
        file["contect"] = ['']
    
    openJS = open("server.js").read()
    files = json.loads(openJS)
    c = 0
    for f in files:
        
        print("before",f)
        print(file)
        if(f["id"]==file["id"]):
            files[c]=file
            print("after",f)

            break
        c+=15
    
    
    newfile =  open("server.js","w")
    json.dump(files,newfile)


#test the methods
file = openfile(26041844 , [123, 212])
editfile(file,"replace",1,"test text",100)

print("FILE AFTER SAVING",file)

# file =  appendNewLine(file,"text",1)
# print(file)

# file =  replace(file,1,"text2",1)
# print(file)

# file = appendAtTheEnd(file,"text3",3)
# print("appendAtTheEnd",file)
# file =  appendNewLine(file,"text",1)
# file = appendAtTheEndOfLine(file,2,"line2",3)
# print(file)
# file = insert(file,1,"XXX",3)
# print(file)
import json
import random
random
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


addFile("123",[123,212])

def openfile(id,pk):
    file =  open("server.js")
    files = file.read()
    files = json.loads(files)
    for f in files:
        if(f["id"]==id and f["pk"]==pk):
            return f

def saveFile(file):
    file =  open("server.js")
    files = file.read()
    files = json.loads(files)
    files.append(json.loads(file))
    file =  open("server.js","w")
    json.dump(files,file)

from paillier.crypto import secure_addition, scalar_multiplication, secure_subtraction
from paillier.keygen import generate_keys
from paillier.crypto import encrypt, decrypt
from Converter import *
import json
pk, sk = generate_keys()
n = pk[0]

PlainText_1 = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
PlainText_2 = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY"

print("Enrypting and joining the following text",
      PlainText_1, PlainText_2, sep="\n")
print("len",len(PlainText_1))


# Encode
Coded_1 = Encode(PlainText_1)
Coded_2 = Encode(PlainText_2)


# Encrypte
cipherText_1 = encrypt(pk, Coded_1)
print("Cipher",cipherText_1,"Len",len(str(cipherText_1)))
cipherText_2 = encrypt(pk, Coded_2)

# Scalar multiplication
# note the Scale is not encrypted
# how many digits we are going to add-> +1 for the 0 digit on the left of the second number
Scale = 10**(len(str(Coded_2))+1)
# multiply the first number by the sclaer to add the other text to it
cipherText_1 = scalar_multiplication(cipherText_1, Scale, n)

# Add the two numbers
sum = secure_addition(cipherText_1, cipherText_2, n)
print("sum",sum,"sum",len(str(sum)))

# Print the cipherText
print("cipherText:\n", sum)
# Print the decrypted cipherText
print("Final Added:\n", Decode(decrypt(pk, sk, sum)))


def openFile(filename):
    file = open("js.json").read()
    jsonContent = json.loads(file)
    fileC = json
    for fileInfo in jsonContent:
        if(fileInfo["filename"]==filename):
            fileC = fileInfo
    
    return fileC["id"] , fileC["sk"], fileC["pk"]

print(openFile("John0"))
def createFile(filename,id,pk,sk):
    file = open("js.json").read()
    jsonContent = json.loads(file)   
    data = '{"filename" : "'+filename+'", "id": "'+str(id)+'", "sk": '+str(sk)+', "pk": '+str(pk)+' }'    
    fileInfo = json.loads(data)
    jsonContent.append(fileInfo)
    filesave = open("js.json","w")
    json.dump(jsonContent, filesave)
    
    # filesave = open("js.json","w")
    # filesave.write(str(jsonContent))
    # filesave.close
    #jsonContent.append

createFile("nyname0",2,3,4)


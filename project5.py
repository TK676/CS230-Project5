
#The following code is a very crude version, but does as intended. The decrypted message outputs with no spaces between the words, but still otherwise outputs the message fully decrypted. 



#Code below (line 3-12) takes the key text file and puts the left column into a plainTextList and puts the right column into a cipherTextList
def makeListsFromKeyFile(filename):
    inputFile = open(filename, "r")
    plainTextList = []
    cipherTextList = []
    
    for line in inputFile:
        parts = line.split()
        plainTextList.append(parts[0].strip())
        cipherTextList.append(parts[1].strip())
    return plainTextList, cipherTextList

plainTextList, cipherTextList = makeListsFromKeyFile("key.txt")


key_file_name = "key.txt"
key = dict()

encryptedCharacters = []
decryptedCharacters = []
decryptedMessage = []

#Code below (line 25-31) reads the encrypted text and puts it into a list one character at a time
inputFile = open("encrypted.txt", "r")
with open("encrypted.txt") as inputFile:
  while True:
    character = inputFile.read(1)
    if not character:
      break
    encryptedCharacters.append(character)


plainTextList.append(" ")
plainTextList.append(" ")
cipherTextList.append(" ")
cipherTextList.append(" ")

locationOfLetters = []

#Finds and prints the location of the encryptedCharacters in the plainTextList
for i in range(len(encryptedCharacters)):
  print(plainTextList.index(encryptedCharacters[i]))
  locationOfLetters.append(plainTextList.index(encryptedCharacters[i]))


for i in range(len(locationOfLetters)):
    decryptedCharacters.append(locationOfLetters[i]-1)

print(plainTextList)
print(cipherTextList)
print(decryptedCharacters)


for i in range(len(decryptedCharacters)):
    decryptedMessage.append((plainTextList[locationOfLetters[i]-1]))

for character in decryptedMessage:
    if character == "Z":
        decryptedMessage.remove(character)
print(decryptedMessage)


decryptedString = ""
for character in decryptedMessage:
    decryptedString += character

print(decryptedString)


outputFile = open("decrypted.txt", "w")
outputFile.write(decryptedString)
outputFile.close()
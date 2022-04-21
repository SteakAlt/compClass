word = input("Enter word: ")

vowels = ['a', 'e', 'i', 'o', 'u']

uCount = 0
lCount = 0
vCount = 0
dCount = 0

print("Number of letters of the word is: ", len(word))

for i in word:
    if(i.lower() in vowels):
        vCount+=1
    if(48 <= ord(i) <= 57):
        dCount += 1
        continue
    if(65 <= ord(i) <= 90):
        uCount += 1
    if(97<= ord(i) <= 122):
        lCount += 1
print("The word had " + str(uCount) + " Upper case characters, " + str(lCount) + " lower case characters, " + str(vCount) + " vowels and " + str(dCount) + " digits.")

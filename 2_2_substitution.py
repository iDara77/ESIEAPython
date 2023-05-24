def printSubstitutionResult(result):
    col=4
    header = "{}{}{}{}".format("L".center(col),"I".center(col),"J".center(col),"F".center(col))
    print(header)

    print("-"*len(header))
    
    for step in result["steps"]:
        print(f"{step[0].center(col,'.')}{str(step[1]).center(col,'.')}{str(step[2]).center(col,'.')}{step[3].center(col,'.')}")
    print("-"*len(header))
    print(result['word'])
    print(result['encrypted'])
    
# 2.2.1 Chiffre Atbash
def chiffreAtbash(word):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet2 = "zyxwvutsrqponmlkjihgfedcba"
    word = word.lower()
    encrypted = ""
    for letter in word:
        i = alphabet.index(letter)
        encrypted += alphabet2[i]
    
    return {"word": word, "encrypted": encrypted}


result = chiffreAtbash("ESIEA")
print(" Chiffre Atbash ".center(90,"*"))
print(result['word'])
print(result['encrypted'])

# 2.2.2 Chiffre César
def chiffreCesar(word, dec):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    word = word.lower()
    encrypted = ""
    steps = []
    for letter in word:
        i = alphabet.index(letter)
        j = (i + dec) % len(alphabet)
        encrypted += alphabet[j]
        steps.append((letter, i, j, alphabet[j]))
    
    return {"word": word, "encrypted": encrypted, "steps": steps}

result = chiffreCesar("ESIEA", 10)
print(" Chiffre Cesar ".center(90,"*"))
printSubstitutionResult(result)

print("*"*90)




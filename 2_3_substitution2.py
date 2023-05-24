ALPH1 = "abcdefghijklmnopqrstuvwxyz"
ALPH2 = "zyxwvutsrqponmlkjihgfedcba"
class Encryptor:
    def __init__(self, alpha1=ALPH1, alpha2=ALPH2, dec=5) -> None:
        self.alpha1 = alpha1
        self.alpha2 = alpha2
        self.dec = dec

    def chiffreAtbash(self, word):
        word = word.lower()
        encrypted = ""
        for letter in word:
            i = self.alpha1.index(letter)
            encrypted += self.alpha2[i]
        
        return {"word": word, "encrypted": encrypted}

    def chiffreCesar(self, word):
        word = word.lower()
        encrypted = ""
        steps = []
        for letter in word:
            i = self.alpha1.index(letter)
            j = (i + self.dec) % len(self.alpha1)
            encrypted += self.alpha1[j]
            steps.append((letter, i, j, self.alpha1[j]))
        
        return {"word": word, "encrypted": encrypted, "steps": steps}

    def polySubstitution(self, word):
        word = word.lower()
        encrypted = ""
        steps = []
        dec=self.dec
        for letter in word:
            i = self.alpha1.index(letter)
            j = (i + dec) % len(self.alpha1)
            encrypted += self.alpha2[j]
            steps.append((letter, i, j, self.alpha2[j]))
            dec+=1
        
        return {"word": word, "encrypted": encrypted, "steps": steps}

    @classmethod
    def printSubstitutionResult(cls, result):
        col=4
        header = "{}{}{}{}".format("L".center(col),"I".center(col),"J".center(col),"F".center(col))
        print(header)

        print("-"*len(header))
        
        for step in result["steps"]:
            print(f"{step[0].center(col,'.')}{str(step[1]).center(col,'.')}{str(step[2]).center(col,'.')}{step[3].center(col,'.')}")
        print("-"*len(header))
        print(result['word'])
        print(result['encrypted'])



enc1 = Encryptor()
enc2 = Encryptor(dec=10)
print(" Chiffre Atbash ".center(90,"*"))
result = enc1.chiffreAtbash("ESIEA")
print(result['word'])
print("ENC1", result['encrypted'])
result = enc2.chiffreAtbash("ESIEA")
print("ENC2", result['encrypted'])

print(" Chiffre Cesar ".center(90,"*"))
result = enc1.chiffreCesar("ESIEA")
Encryptor.printSubstitutionResult(result)
result = enc2.chiffreCesar("ESIEA")
Encryptor.printSubstitutionResult(result)


print(" SUBSTITUTION POLYALPHABETIQUE ".center(90,"*"))
result = enc1.polySubstitution("AAAAA")
Encryptor.printSubstitutionResult(result)
result = enc2.polySubstitution("AAAAA")
Encryptor.printSubstitutionResult(result)

print("*"*90)
    
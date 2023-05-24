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
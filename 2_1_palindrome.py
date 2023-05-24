# 2.1 Palindromes
# « À révéler mon nom, mon nom relèvera » (Cyrano de Bergerac)
# 2.1.1 Mots
print("="*8 + " 2.1.1 Mots " + "="*8)
word = "hannah"
word1 = word[0:3]
word2 = word[3:]

word2inv = word2[::-1]
word3 = word[-1:2:-1]

print(f"""{word} 
{word} >> {word1} {word2}
{'-'*16}
{word2} >> {word2inv} ou
{word2} >> {word3}
{'-'*16}
{word2inv} == {word1} is {word2inv == word1}\n""")

# 2.1.2 Phrases
print("="*8 + " 2.1.2 Phrases " + "="*8)
phrase = "la mariee ira mal"
phrase_no_space = phrase.replace(" ","")
psn1 = phrase_no_space[0:7]
psn2 = phrase_no_space[7:]

psn2inv = psn2[::-1]
psn3 = phrase_no_space[-1:6:-1]

print(f"{phrase}\n" \
        f"{phrase} >> {phrase_no_space}\n" \
        f"{phrase_no_space} >> {psn1} {psn2}\n" \
        f"{'-'*16}\n" \
        f"{psn2} >> {psn2inv} ou\n" \
        f"{psn2} >> {psn3}\n" \
        f"{'-'*16}\n" \
        f"{psn2inv} == {psn1} is {psn2inv == psn1}\n")

# 2.1.3 Impaires
print("="*8 + " 2.1.3 Les Impaires " + "="*8)
word = "radar"
word1 = word[:2]
word2 = word[-1:2:-1]

print(f"""{word} 
{word} >> {word1} {word2}
{word2} == {word1} is {word2 == word1}\n""")

# 2.1.4 Généralisation
print("="*8 + " 2.1.4 Généralisation " + "="*8)
def palinCheckNoPrint(word):
	_orig = word
	word = word.lower()
	word = word.replace(" ","")
	lenword = len(word) // 2
	modword = 1 - len(word) % 2 
	word1 = word[:lenword]
	word2 = word[-1:lenword-modword:-1]
	return word1, word2

def palinCheck(word):
    _orig = word
    word1,word2 = palinCheckNoPrint(word)
    print(f"""{_orig} 
	{word} >> {word1} {word2}
	{word2} == {word1} is {word2 == word1}\n""")

palinCheck("RaDaR")
palinCheck("Hannah")
palinCheck("La mariee ira mal")
palinCheck("A reveler mon nom mon nom relevera")


import timeit
def palinCheck2NoPrint(word):
	word = word.lower()
	word = word.replace(" ","")
	word2 = word[::-1]
	
	return word, word2

def palinCheck2(word):
    _orig = word
    word, word2 = palinCheck2NoPrint(word)
    print(f"""{_orig} 
    {word2} == {word} is {word2 == word}\n""")

palinCheck2("RaDaR")
palinCheck2("Hannah")
palinCheck2("La mariee ira mal")
palinCheck2("A reveler mon nom mon nom relevera")

def testPlainCheck(): 
	palinCheckNoPrint("RaDaR")
	palinCheckNoPrint("Hannah")
	palinCheckNoPrint("La mariee ira mal")
	palinCheckNoPrint("A reveler mon nom mon nom relevera")
  
def testPlainCheck2(): 
	palinCheck2NoPrint("RaDaR")
	palinCheck2NoPrint("Hannah")
	palinCheck2NoPrint("La mariee ira mal")
	palinCheck2NoPrint("A reveler mon nom mon nom relevera")
 
print('testPlainCheck ',timeit.timeit(testPlainCheck,number=100000), ' seconds')
print('testPlainCheck2 ',timeit.timeit(testPlainCheck2,number=100000), ' seconds')

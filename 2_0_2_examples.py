### IF, ELIF, ELSE ###
i=0
true_val = True
if true_val == True:
    print(i, "true_val is True")

i+=1
false_val = False
if false_val != True:
    print(i, "false_val is False")
else:
    print(i, "disaster")

i+=1
letter = "b"
if letter == "a":
    print(i, "disaster")
elif letter == "b":
    print(i, "letter is b")
else:
    print(i, "disaster")
    
### WHILE ###
i+=1
print (i, "WHILE x < 5")
x = 0
while x < 5:
    print(i, "x = %d" % x)
    x+=1

i+=1
print (i, "WHILE / BREAK / CONTINUE")
x = 0
while True:
    x+=1
    if x % 2 == 0:
        continue # omettre les nombres pairs
    print(i, "x = %d" % x)
    if x >= 10:
        print(i, "BREAK")
        break

i+=1
print (i, "WHILE / ELSE")
x=0
while x < 5:
    print(i, "x = %d" % x)
    x+=1
else:
    print(i,"Pas de break")
while x < 5: # x est deja == 5 donc pas de boucle
    print(i, "x = %d" % x)
    x+=1
else:
    print(i,"Pas de break non plus")
while x < 10: # x est deja == 5 donc pas de boucle
    if x % 2 == 0:
        print(i, "BREAK: x = %d" % x)
        break
    x+=1
else:
    print(i,"Jamais imprimée")
    
### FOR ... IN ###
i+=1
print(i, "FOR ... IN list")
liste = ["a",2,("c",3)]
for item in liste:
    print(i, item)
for index,item in enumerate(liste):
    print(i, index,item)

i+=1
print(i, "FOR ... IN dict")
dicto = {"a":"Alpha",2: "Bravo",("c",3):"Charlie"}
for key in dicto:
    print(i, key)

for key,val in dicto.items():
    print(i, key, val)
    
i+=1
print(i, "FOR ... IN range")
for x in range(0,3):
    print(i, "range(0,3)", x)

for x in range(0,5,2):
    print(i, "range(0,5,2)", x)
    
for x in range(5,-1,-2):
    print(i, "range(5,-1,-2)", x)

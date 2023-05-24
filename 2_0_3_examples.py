def printSeparator(head=True, title=None):
    if head:
        print("#"*5 + f" {title} " + "#"*5)
    else:
        print("#"*20 + "\n")
        
printSeparator(title=" printHello ")
def printHello():
    print("Hello")
print("Appel à printHello")
printHello()
print("type de printHello ", printHello)
a = printHello
print("Appel à 'a'")
a()
print("type de 'a' ", type(a))
printSeparator(head=False)

printSeparator(title=" printX ")
def printX(x):
    print(f"x = {x}")
printX(1)
printX("a")
printX(["a",1])
printSeparator(head=False)

printSeparator(title=" divAB ")
def divAB(a,b,dec=False,mod=False):
    if dec:
        response =  a / b
    elif mod:
        response = a // b , a % b
    else:
        response =  a // b
        
    return response

print(f"divAB(4,2) : 4 / 2 = {divAB(4,2)}")
print(f"divAB(5,2) : 5 / 2 = {divAB(5,2)} (sans decimal)")
print(f"divAB(5,2,False,True) : 5 / 2 = {divAB(5,2,False,True)} (sans decimal, avec reste)")
print(f"divAB(5,2,mod=True) : 5 / 2 = {divAB(5,2,mod=True)} (sans decimal, avec reste)")
print(f"divAB(mod=True, b=2, a=5) : 5 / 2 = {divAB(mod=True, b=2, a=5)} (sans decimal, avec reste)")
printSeparator(head=False)

printSeparator(title=" *args et **kwargs ")
def maFunc(a, *args, **kwargs):
    print(a, args, kwargs)

maFunc(1)
maFunc(1,2,3)
maFunc(1,b=4,c=5)
maFunc(1,2,3,b=4,c=5)
printSeparator(head=False)

printSeparator(title=" inner ")
def outer(a, b):
    x=10
    def inner(c, d):
        print(f"a={a},b={b},x={x}")
        return c * d
    return inner(a, b)

print(f"outer: {outer(4,5)}")

def closure():
    def inner():
        return "I am inner"
    return inner

a = closure()
print("Type de 'a': " + str(type(a)))
print("Appel à 'a': " + a())
printSeparator(head=False)
# 1.1 Aussi simple que
print("Hello World")

# 1.2 Une variable
print("=" * 8 + "1.2" + "=" * 8)
msg = "1.2 Hello World"
print(msg)

# 1.3 Concatenation des strings
print("=" * 8 + "1.3" + "=" * 8)
msg = "Hello" + " World"
print("1.3 "+msg)

# 1.4 Formattage des strings - 1
ver = 1.4
print("=" * 8 + str(ver) + "=" * 8)
msg = "Hello World"
print("%s %s" % (ver,msg))

# 1.5 Formattage des strings - 2
ver = ver + 0.1
msg = "Hello World"
print("=" * 8 + str(ver) + "=" * 8)
print("{} {}".format(ver, msg))
print("{} {}".format(msg,ver))
print("{1} {0}".format(msg,ver))

# 1.6 Formattage des strings - 3
ver += 0.1
msg = "Hello World"
print("=" * 8 + f"{ver}" + "=" * 8)
print(f"{ver} {msg}")

#1.7 Types
ver = 1
subver = 7
msg = "Hello World"
print("=" * 8 + f"{ver}.{subver}" + "=" * 8)
print(f"ver est un.e {type(ver)}")
print(f"msg est un.e {type(msg)}")
print(f"print est un.e {type(print)}")

print(ver + subver)
print(ver + subver/10)
print(f"1.7.1 ver est un.e {type(ver)}")
print(f"1.7.2 subver est un.e {type(subver)}")
print(f"1.7.3 subver/10 est un.e {type(subver/10)}")

try:
    print(ver + msg)
except Exception as e:
    print("1.7.4 ERREUR: %s" % e)

sver = str(ver)
try:
    print(sver + msg)
except Exception as e:
    print("1.7.5 ERREUR: %s" % e)
print(f"1.7.6 sver est un.e {type(sver)}")
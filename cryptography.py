# CODE BY OMKAR NAIK
# DESIGNED TO IMPLEMENT THE WORKING OF CRYPTOGRAPHY

def PrintTable(l1):
    for z in range(26):
        print(z + 1, end="\t")
        for i in l1:
            print(i, end="  ")
        print()
        t = l1[25]
        l1.insert(0, t)
        l1.pop()

def KeyWise(l1):
    q = 1
    key = 0
    while q:
        key = int(input("ENTER KEY: "))
        if key > 26 or key < 1:
            print("WRONG KEY VALUE!")
            print()
        else:
            q = 0
    for z in range(1, 27):
        if z == 1 or z == key:
            print(z, end="\t")
            for i in l1:
                print(i, end="  ")
            print()
        t = l1[25]
        l1.insert(0, t)
        l1.pop()

def Encrypt(l1):

    msg1 = input("\nENTER PLAIN TEXT: ")
    msg = msg1.upper()
    key = int(input("ENTER KEY: "))
    print()

    l2 = []
    for z in range(26):
        if z == key - 1:
            for i in l1:
                l2.append(i)
        t = l1[25]
        l1.insert(0, t)
        l1.pop()

    print("ENCRYPTED MESSAGE: ", end="")
    for i in msg:
         if i == " ":
            print(end=" ")
         else:
            temp = l1.index(i)
            s = l2[temp]
            print(s, end="")
    print()

def Decrypt(l1):
    msg1 = input("\nENTER CIPHER TEXT: ")
    msg = msg1.upper()
    key = int(input("ENTER KEY: "))
    print()

    l2 = []
    for z in range(26):
        if z == key - 1:
            for i in l1:
                l2.append(i)
        t = l1[25]
        l1.insert(0, t)
        l1.pop()

    print("DECRYPTED MESSAGE: ", end="")
    for i in msg:
        if i == " ":
            print(end=" ")
        else:
            temp = l2.index(i)
            s = l1[temp]
            print(s, end="")
    print()

l1 = []
for i in range(65, 91):
    l1.append(chr(i))
key = 0
while True:
    print("\n1. PRINT CRYPTOGRAPHY TABLE\n2. PRINT KEY WISE TABLE\n3. ENCRYPTION\n4. DECRYPTION\n5. EXIT (PRESS ENTER)")
    p = input("ENTER CHOICE: ")
    if p == '1':
        PrintTable(l1)
    elif p == '2':
        KeyWise(l1)
    elif p == '3':
        Encrypt(l1)
    elif p == '4':
        Decrypt(l1)
    elif p == '5' or p == '':
        print("THANK YOU <3")
        exit()
    else:
        print("WRONG CHOICE!")

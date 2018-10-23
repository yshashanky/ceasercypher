#ENCRYPTION
#input of plain text
p=input("Enter the plain text:")
#print(p)
#input of key
k=int(input("Enter the key:"))
#print(k)
w=""
for i in p:
    c=i
    x=ord(c)
    x+=k
    if(x<=122):
        chr(x)
        #print(chr(x))
    else:
        x-=26
        chr(x)
        #print(chr(x))
    w+=chr(x);
print("Encrypted text is:",w)

#DECRYPTION
#P=input("Enter the encrypted text:")
P=w
K=int(input("Enter the key:"))
W=""
for j in P:
    C=j
    X=ord(C)
    X-=K
    if(X>=97):
        chr(X)
    else:
        X+=26
        chr(X)
    W+=chr(X)
print("Decrypted code is:",W)
#for 'space' it may show different symbol 
#after decryption as compare to plain text

Plaintext="abcdefghijkl"
keye=4
offset=1

offset=offset%(2*keye-1) # offset at most can be twice the key minus 1

Plaintext='*'*offset+Plaintext
Cipher=['']*keye

Len=len(Plaintext)
index=0
inc= True
i=0
while  i < Len:    
    Cipher[index]=Cipher[index]+ Plaintext[i]
    if inc is True:
        index=index+1
    else:
        index=index-1

    if (index==keye-1):
        inc=False
    if index==0:
        inc =True
    i=i+1
    
print (''.join(Cipher)[offset:])

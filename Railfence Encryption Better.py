

Plaintext="abcdefghijkl" # the data used can be programmed to be from the user
keye=4 # the key
offset=1 # the offset

offset=offset%(2*keye-1) # offset at most can be twice the key minus 1



Plaintext='*'*offset+Plaintext # populating the plaintext with a string of length ==offset

Cipher=['']*keye 

Len=len(Plaintext)
index=0
inc=True # this is useful to control the path of the iteration from down to up and viceversa
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

for i in range(keye):
    Cipher[i]=Cipher[i].replace('*','')
  
print(''.join(Cipher))
print(Plaintext[offset:])



Plaintext="abcdefghijkl" # the data used can be programmed to be from the user
keye=4 # the key
offset=1 # the offset

offset=offset%(2*keye-1) # offset at most can be twice the key minus 1

ch='*'
for i in range(33,47):
    if Plaintext.find(ch):
        break
    ch=chr(i)

Plaintext=ch*offset+Plaintext # populating the plaintext with a string made up of a character that
# doesnt exist in the plaintext

Cipher=['']*keye 

Len=len(Plaintext)
index=0
inc=True # this is useful to control the path of the iteration from down to up and viceversa
i=0

while  i < Len:    
    Cipher[index]=Cipher[index]+ Plaintext[i]
    #just build the cipher with all the characters 

    if inc is True: # if the path is up it increases else it decreases
        index=index+1 
    else:
        index=index-1


    if (index==keye-1): # if at the bottom, it starts goig up. if at up, going down
        inc=False
    if index==0:
        inc =True
    i=i+1

for i in range(keye): # removing added characters from the build string
    Cipher[i]=Cipher[i].replace(ch,'')
  
print(''.join(Cipher)) # join the separated strings
print(Plaintext[offset:])


# the data used can be programmed to be from the user
Plaintext="abcdefghijkl"
keye=4
offset=1
space=True

if space is not True:
    Plaintext=Plaintext.replace(' ','')
    # if you want space inclusion 

offset=offset%(2*keye-1) # offset at most can be twice the key minus 1


ch='*'
for i in range(33,47):
    if Plaintext.find(ch):
        break
    ch=chr(i)

Plaintext=ch*offset+Plaintext

Len=len(Plaintext)
G=2*(keye)-1 # this is the distance between the two sharp edges of the fence
Cipher=""


if keye >= offset:
    E=keye
else:
    E= (keye-(offset%(keye-1)))-1


for i in range(keye):
    #There are two cases :when the character is at the bottom or top of the fence and when it is not  
    j=i
    if i==keye-1 or i==0:
       while j < Len:
            if i==j and i< offset:
                j=j+G-1
                continue
            else:
                Cipher=Cipher+(Plaintext[j])
                j=j+G-1
    
    else:
       while j <Len:
            if i==j and i < offset:
                j=j+G-1-2*i
            else:
                Cipher=Cipher+(Plaintext[j])
                j=j+G-1-2*i

            
            if j<Len:
                if i==j-(G-2*i) and i>E and offset>keye:
                    j=j+2*i
                else:
                    Cipher=Cipher+(Plaintext[j])
                    j=j+2*i


print(Cipher)
print(Plaintext[offset:])




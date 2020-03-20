# the data used can be programmed to be from the user
Cipher_text="flaegkbdhjci"
keye=4 # the length of the key 
offset=1 # the offset

ch='*'

    #looking for a character that doesnt exist in the plantext

Len=len(Cipher_text)+ offset # total length assumed with offset in mind
offset=offset%(2*keye-1) # offset at most can be twice the key minus 1
Plain=[None]*(Len)
G=2*(keye-1) # this is the distance between the two sharp edges of the fence
E= keye-(offset%(keye-1))-1
inc=0

for i in range(keye):
    #Two cases are assumed:when the character is at the bottom or top of the fence and when it is not  
    j=i
    if j>0 and j<keye-1:
        while j <Len:
            if i==j and i <offset:
                Plain[j]=ch
                
            else:
                Plain[j]=(Cipher_text[inc])
                inc=inc+1
                
            j=j+G-2*i
            if j<Len:
                if i>E and i==j-(G-2*i) and offset>keye:
                    Plain[j]=ch
                
                else:
                    Plain[j]=(Cipher_text[inc])
                    inc=inc+1
                
                j=j+2*i

    else:
        while j < Len:
            if i==j and i < offset:
                Plain[j]=ch
            else:
                Plain[j]=(Cipher_text[inc])
                inc=inc+1            
            j=j+G
            
print(''.join(Plain).replace(ch,''))


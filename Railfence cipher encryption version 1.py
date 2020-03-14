
# the data used can be programmed to be from the user
Plaintext="You can use it for learning programming"
keye=5 
offset=6
space=True

if space is not True:
    Plaintext=Plaintext.replace(' ','')
    # if you want space inclusion 



Plaintext='*'*offset+Plaintext # filling with dummy character at the front
offset=offset%(2*keye-1) # offset at most can be twice the key minus 1
Len=len(Plaintext)
G=2*(keye-1) # this is the distance between the two sharp edges of the fence
Cipher=""



if keye >= offset:
    E=keye
else:
    E= (keye-(offset%(keye-1)))-1

for i in range(keye):
    #There are two cases :when the character is at the bottom or top of the fence and when it is not  
    j=i
    if j==keye-1 or j==0: 
       while j < Len:
            if i!=j or i>=offset:
                Cipher=Cipher+(Plaintext[j])                     
            j=j+G

    else:
       while j <Len:
            if i!=j or  i >= offset:
                Cipher=Cipher+(Plaintext[j])                      
            j=j+G-2*i          
                
            if j<Len:
                if i<=E or i!=j-(G-2*i) or offset<=keye:
                    Cipher=Cipher+(Plaintext[j])                                                 
                j=j+2*i
   
        
   

print(Cipher)


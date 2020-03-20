Cipher="rnLaecifel"
keye=4
offset=5
offset=offset%(2*keye-1) # offset at most can be twice the key minus 1


'''

the final algorithm

determine the number of characters on each row
construct a total of 'k' strings whose for each row
the fill in the constructed spaces with the charcters from the cipher
//by now if the constructed strings are printer on the array, it somehow resembles the visual
build a downward string
reverse odd strings
attach last characters of odd ones to even ones and intitials of even ones to next ones
reverse all characters 

'''


clean=Cipher
Cipher=offset*'*'+Cipher
Plaintext=""

Len=len(Cipher)
Col=[0]*keye # to count the distribution of chracters on a row
index=0
inc=True # this is useful to control the path of the iteration from down to up and viceversa
i=0

#determining the number of characters on a single row on the rail CO
while  i < Len:    
    Col[index]=Col[index]+1
    if inc is True: 
        index=index+1
    else:
        index=index-1

    if (index==keye-1):
        inc=False
    if index==0:
        inc =True
    i=i+1

iterator=0
Result=[None]*keye
master=''
maxrow=0


if offset < keye:
    for r in range(keye): # placing cipher to bring unfiltered cipher
        Result[r]=[None]*Col[r]
        maxrow=max(maxrow,Col[r])
        
        for q in range(Col[r]):
            if q==0 and r < offset:     # first element of and disturbed row
                Result[r][q]='*'
            else:
                Result[r][q]=clean[iterator]
                iterator=iterator+1
   
else:
    
    O=keye - (offset-keye)-1
    rr=keye-1
    while rr>=0: # placing cipher to bring unfiltered cipher
        Result[rr]=[None]*Col[rr]
        maxrow=max(maxrow,Col[rr])

        for jj in range(1,Col[rr]):       
            if jj == 0 and rr >=O:# first element of and disturbed row
                Result[rr][jj]='*'
            else:
                Result[rr][jj]=clean[iterator]
                iterator=iterator+1
            
        rr=rr-1
    
    

      
     


z=0
index=0
inc = True
col=0
some=5

we=0
#printing result
for we in range(keye):
    print(Result[we])



Answer=[""]*maxrow
#create a downward string
for columun in range(maxrow): 
    for init in range(keye):    
        try:
            ch=Result[init][columun]
            Answer[columun]=Answer[columun]+ch
        except:
            continue      
        
    print(Answer[columun])        

# before reversing
for ss in range(1,maxrow-2):    

    if ss % 2 !=0:
       Answer[ss+1]=Answer[ss+1]+Answer[ss][-1]
       Answer[ss]=Answer[ss][:-1]
    else:
        Answer[ss+1]=Answer[ss][0]+Answer[ss+1]
        Answer[ss]=Answer[ss][1:]
    


#reverese the odd pattern
for us in range(maxrow):    
    if (us%2!=0):
        Answer[us]=Answer[us][::-1]

inc=True



grand=""
for wee in range(maxrow):
    grand=grand+Answer[wee]



print(grand[offset:])







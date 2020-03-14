in="flaegkbdhjci"
keye=4
offset=1
offset=offset%(2*keye-1) # offset at most can be twice the key minus 1

Input='*'*offset+Input
Output=['']*keye

Len=len(Input)
index=0
inc= True
i=offset
while  i < Len:
    if i>keye or :
        
    else:
        Output[index]=Output[index]+ Input[i]
    if inc is True:
        index=index+1
    else:
        index=index-1

    if (index==keye-1):
        inc=False
    if index==0:
        inc =True
    i=i+1
    
print (''.join(Output)[offset:])


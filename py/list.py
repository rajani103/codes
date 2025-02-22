# names= ["a", "b", "c", "b"] 
# for i,j in enumerate(names):
#     if j == "b":
#       #  print ("indexes if b are :", b[])
#         print ("name with b: ", i,j )


names= ["a", "b", "c", "b"] 
for p,q in enumerate(names):
    if q == "c":
        print ("indx id :" , p)
        
        
a = [1,2,3,4]
for i,j in enumerate(a):
    if j==3:
        print ("index of 3 :" , i)
 
    
a = [1,2,3,4]
for i,j in enumerate(a):
    if j==3:
        print ("index of 3 :" , i)
        
#find nos of sum 3

for p, i in enumerate(a):
    r = 0
    for q, j in enumerate(a):
        c=i+j
        if c == 3:
            r = 1
            print (p,q)
    if(r==1):
        break

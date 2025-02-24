# # # stored in non volatile memory- HDD
# # open file 
# # red/write file
# # close the file

# f = open('data.txt')
# for i in f:
#     print(i)
# print(f.read()) 
# f.readline()

# print (f.readline()) 
# print (f.readline()) 

# print(f.write())  

# import os

# # Get the current working directory
# print("Current Working Directory:", os.getcwd())

# # Check if file exists
# if os.path.exists("data.txt"):
#     print("File exists ✅")
# else:
#     print("File not found ❌")

# f.close()


# for not closing this repetitive times use with 
# with open('data.txt') as f:
#     # for i in f:
        
#     #     print(i)
        
#     print(f.read(5))
#     f.seek(0)
#     print(f.read(2))


# write operation in file
list = ['d\n','f\n']
with open('data.txt','a') as f:
    f.write('pp\n\n')
    f.writelines(list)
    print(f)
    
a = "anndsegdsggkkskk"
result = ""

for p, char in enumerate(a):
    r = 0
    for q, res_char in enumerate(result):
        if char == res_char:
            r = 1
            break
    if r == 0:
        result = result + char

print(result)


# a = "abbbsssddfghhbjjj"

# for p, i in enumerate(a):
#     r = 0
#     for q, j in enumerate(a):
#         if i == j:
#             r = 1
#             print (p,q)
#     if(r==1):
#         break
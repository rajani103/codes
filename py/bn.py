c = "aabbbsssfff"
result = ""
#step 1- i="a", result = "". check i is in result or not, if present con
for i, j in enumerate(c):
    t=0
    for k, l in enumerate(result):
        if j == l:
            t=1
            break
    if t==0:
        result += j

print(result)
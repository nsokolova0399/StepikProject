import numpy as np
def duplicates(lst, item, j):
    return [i for i, x in enumerate(lst) if x == item]

startList = []
res = True


# план супермаркета
s = input()
if s.islower() and len(s)>=1 and len(s) <= 10**5 and s.isalpha():
    q = input()
    if q.isdigit() and int(q) >= 1 and int(q) <= 10**5:
        for i in range(int(q)):
            l, r = input().split()
            if int(l) <= int(r) and int(r) <= len(s):
                startList.extend([l, r])
            else: res = False
    else:res = False
else: res = False

left, rigth = 0, 0
substrList = []
if res:
    for i in range(len(startList)-1):
        if i % 2 == 0:
            left = int(startList[i])
            rigth = int(startList[i+1])
            substrList.extend([s[(left-1) : rigth]])
    print(substrList)


    for i in range(len(substrList)):
        sorted_chars = sorted(substrList[i])
        sorted_string = ''.join(sorted_chars)
        print(sorted_string)

        posDubl = []
        for j in range(len(sorted_string)):
            position = duplicates(substrList[i], sorted_string[j], j)
            if position not in posDubl:
                posDubl.extend([duplicates(substrList[i], sorted_string[j], j)])
        posDubl = [item for sublist in posDubl for item in sublist]
        print(posDubl)

        j = 1
            while substrList[i][j-1]<substrList[i][j] and j!= len(substrList[i]):
                res+=i-(i-1)
                print(res)

            else:
                res+=1
                print(res)





# print(s, q, startList)




# hello
# 3
# 1 5
# 1 2
# 2 5

# hellol
# 3
# 1 6
# 1 2
# 2 5

# laptopp
# 2
# 1 7
# 1 2
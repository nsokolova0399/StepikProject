n, q = input().split()
n, q = int(n), int(q)
people, request = [], []
if n >= 1 and n <= 10**6 and q >= 1 and q <= 10**4:
    for i in range(n):
        people.append(input())
    for i in range(q):
        request.append(input().split())
    list = []
    for i in request:
        if len(i) == 2 and i[0].isdigit() and i[1].isalpha() and i[1].islower():
            if len(i[0]) >= 1 and len(i[0]) <= 10**9 and len(i[1]) >= 1 and len(i[1]) <= 10**3:
                for j in range(n):
                    if people[j].isalpha() and len(people[j]) <= 10**6 and people[j].islower():
                        if i[1] in people[j] and i[1][0] == people[j][0] and len(people[j]) >= int(i[0]):
                            list.append([i[0], i[1], people[j]])
                        else:
                            list.append([i[0], i[1], '-1'])

    list.sort()
    list.reverse()
    k = 0
    for i in request:
        k = 1
        for j in range(len(list)):
            if i[0] == list[j][0] and k == 1 and list[j][2] !='-1':
                print(people.index(list[j][2])+1)
                k += 1
            elif i[0] == list[j][0] and k == 1 and list[j][2] =='-1':
                print(-1)
                k += 1
else: print('Неверный формат данных')

# 5 3
# ad
# a
# abc
# aboba
# b
# 3 a
# 2 ab
# 1 b

# 5 3
# ad
# ad
# a
# ab
# b
# 3 a
# 2 ab
# 1 b

# 5 3
# ad
# ad
# a
# abc
# bf
# 3 a
# 2 ad
# 1 b

# 5 3
# ad
# abb
# a
# abc
# bf
# 3 a
# 2 ad
# 1 b

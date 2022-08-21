def LeftRigth(i):
    position = i.find('=')
    wordLeft, wordRigth = '', ''
    for letter in range(position): wordLeft += i[letter]
    for letter in range(position + 1, len(i)): wordRigth += i[letter]
    return wordLeft, wordRigth

startList = []
# необходимо в конце нажать Enter
while len(startList) <= 10**5:
    line = input()
    if line == '':
        break
    else:
        startList.extend([k for k in line.split()])

# проверим входные значения и склеим их в один список
if len(startList) <= 10**5:
    pair = []
    lft, rgt = 0, 0
    for i in startList:
        if i != '' and i.find(' ') == -1 and (i.find('=') != -1 or i.find('{') != -1 or i.find('}') != -1):
            wordLeft, wordRight = LeftRigth(i)
            if ((wordRight[0] =='-' and wordRight[1:].isdigit()) or wordRight.isdigit()) and abs(int(wordRight)) <= 10**9:
                pair.extend([wordLeft, wordRight])
            elif len(wordRight) <= 10 and wordRight.islower() and len(wordLeft) <= 10 and wordLeft.islower():
                pair.extend([wordLeft, wordRight])
            elif i == '{':
                lft += 1
                pair.append(i)
            elif i == '}':
                rgt += 1
                pair.append(i)
    # если количество открываюющихся и закрывающихся скобок равно 0
    if lft - rgt == 0:
        dictionaryMain, dictionaryNoMain = {}, {}
        bracket = 0
        for i in range(len(pair)):
            if pair[i] == '{':
                bracket += 1
            elif pair[i] == '}':
                bracket -= 1
            else:
                # если число находится на нечетной позиции, то добавляем его в словарь
                if (i + bracket) % 2 != 0 and (pair[i].isdigit() or pair[i][0] == '-'):
                    if bracket == 0: dictionaryMain[pair[i - 1]] = pair[i]
                    else: dictionaryNoMain[pair[i - 1]] = pair[i]
                # если переменная находится на нечетной позиции,то добавляем его в основной или не основной словарь
                elif (i + bracket) % 2 != 0 and (pair[i].isdigit() != True or pair[i][0] != '-'):
                    if bracket == 0:
                        if pair[i] in dictionaryMain:
                            dictionaryMain[pair[i - 1]] = dictionaryMain[pair[i]]
                            print(dictionaryMain[pair[i]])
                        else:
                            dictionaryMain[pair[i - 1]] = '0'
                            print(0)
                    elif pair[i] in dictionaryNoMain:
                            dictionaryNoMain[pair[i - 1]] = dictionaryNoMain[pair[i]]
                            print(dictionaryNoMain[pair[i]])
                    elif pair[i] in dictionaryMain:
                            dictionaryNoMain[pair[i - 1]] = dictionaryMain[pair[i]]
                            print(dictionaryMain[pair[i]])
                    else:
                        dictionaryNoMain[pair[i - 1]] = '0'
                        print(0)
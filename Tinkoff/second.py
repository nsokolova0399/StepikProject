import numpy as np
check, quantityList = [True], []
# вводим количество лет
n = input()
if n.isdigit():
    n = int(n)
    if (n >= 1 and n <= 10**3):
        oldList, newList, quantityList = [], [], []
        for i in range(n):
            # вводим имена победителей
            oldList.append(input().split())
            if len(oldList[i]) == 3 and all(check):
                if len(oldList[i][0]) >= 1 and len(oldList[i][0]) <= 10 and len(oldList[i][1]) >= 1 and len(oldList[i][1]) <= 10 and len(
                        oldList[i][2]) >= 1 and len(oldList[i][2]) <= 10:
                    if oldList[i][0].isupper() and oldList[i][1].isupper() and oldList[i][2].isupper() and oldList[i][0].isalpha() and oldList[i][1].isalpha() and oldList[i][2].isalpha():
                        newList.append(sorted(oldList[i]))
                        quantityList.append(newList.count(newList[i]))
            else: check.extend([False])
    if quantityList != [] and all(check): print(max(quantityList))
    else: print('Неверный формат данных')
else: print('Неверный формат данных')

# 5
# MIKHAIL VLADISLAV GRIGORY
# VLADISLAV MIKHAIL GRIGORY
# IVAN ILYA VLADIMIR
# ANDREY VLADIMIR ILYA
# VLADIMIR IVAN ANDREY

# 5
# VLADISLAV MIKHAIL GRIGORY
# ILYA VLADIMIR ANDREY
# ANDREY VLADIMIR ILYA
# VLADIMIR ILYA ANDREY
# MIKHAIL VLADISLAV GRIGORY
# MIKHAIL GRIGORY VLADISLAV

# 2
# G H T T
# G H F
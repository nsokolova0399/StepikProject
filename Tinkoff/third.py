# число дней, данные за которые у вас есть данные
n = input()
if n.isdigit():
    n = int(n)
    if (2 <= n and n <= 10**5):
        # количество подключенных/отмененных подписок
        startList = input().split()
        if len(startList) == n:
            profit = 0
            differenceList = []
            for i in range(1,n):
                if int(startList[i-1]) >= 1 and int(startList[i]) >= 1 and int(startList[i-1]) <=10**3 and int(startList[i]) <=10**3 :
                    if i % 2 != 0:
                        differenceList.append(int(startList[i - 1]) - int(startList[i]))
            if differenceList != []:
                # минимальная разность
                min_difference = min(differenceList)
                # индекс минимальной разницы
                ind_min_dif = differenceList.index(min_difference)
                if min_difference < 0:
                    if ind_min_dif == 0:
                        startList[0], startList[1] = startList[1], startList[0]
                    else:
                        startList[2 ** ind_min_dif], startList[2 ** ind_min_dif + 1] = startList[2 ** ind_min_dif + 1], startList[2 ** ind_min_dif]
                for i in range(n):
                    profit += (-1)**(i)*int(startList[i])
                print(profit)
        else:
            print('Неверный формат данных')
    else:
        print('Неверный формат данных')
else: print('Неверный формат данных')
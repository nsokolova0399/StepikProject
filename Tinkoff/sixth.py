import numpy as np
# находим позицию элемента, который находится на четном месте(по индексу) и его значение совпадает с искомым
def duplicates(lst, item, j):
    return [i for i, x in enumerate(lst) if x == item and i % 2 == 0 and j-1 != i]
# вводим количество лифтов
n = input()
# объявляем списки
# исходный список входных  значений, где хранятся номера нижнего и верхнего этажа соотвественно
upplowElevator = []
# вспомогательный список, куда по порядку записываются пары ['2','2'], ['2','5']
listElevator = []
# вспомогательный список, который разделяет на пары исходный список, при этом учитываются повторения
# и вхождения в этот в список, т е пример [['2','2'],['2','5']]
resultUpplowElevator = []
# список позиций необходимого нам элемента, на четном месте(по индексу)
position = []
# готовый список, где объединены пары [['2','2'],['2','5'],['2','5'],['5','6']]
result = []
# число повторений, если есть одинаковые пары
numberRepeat = 0
# список повторений
numberRepeatList = []
if n.isdigit():
    n = int(n)
    if n >= 1 and n <= 10**5:
        for i in range(n):
            a, b = input().split()
            upplowElevator.extend([a,b])
        # составим список пар, которые подходят друг другу
        for i in range(1,len(upplowElevator)):
            if upplowElevator[i-1].isdigit():
                if int(upplowElevator[i-1]) >= 0 and int(upplowElevator[i-1]) <= 10**9 and upplowElevator[i-1] <= upplowElevator[i]:
                    if i % 2 != 0:
                        position = duplicates(upplowElevator, upplowElevator[i],i)
                        for number in range(len(position)):
                            listElevator = []
                            if [upplowElevator[i - 1], upplowElevator[i]] == [upplowElevator[position[number]], upplowElevator[position[number] + 1]]:
                                numberRepeat += 1
                            elif listElevator not in resultUpplowElevator:
                                if numberRepeat!=0:numberRepeatList.append(numberRepeat)
                                numberRepeat = 0
                                # составляем пары
                                listElevator.append([upplowElevator[i - 1], upplowElevator[i]])
                                listElevator.append([upplowElevator[position[number]], upplowElevator[position[number] + 1]])
                                resultUpplowElevator.extend([listElevator])

        resultUpplowElevator.sort()
        max = 0
        # соединяем пары и составляем цепь
        for item in resultUpplowElevator:
            for jtem in resultUpplowElevator:
                if result == []: result.extend([item[0], item[1]])
                if item[1] == jtem[0] and result[len(result)-1] == jtem[0]:
                    result.extend([jtem[0],jtem[1]])
                    max += 1

        if numberRepeatList == []:print(len(result) // 2 + 1)
        else: print(len(numberRepeatList) + len(result) // 2)
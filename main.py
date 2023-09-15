
stroka = list(input('Напишите строкой количество разыгранных орлов и решек(ОРОРРОРРРРОРРРР):'))
print(stroka)

counterer = 0
spisok = []

for i in range(len(stroka)):
    if stroka[i] == 'Р':
        counterer += 1
        spisok.append(counterer)
    if stroka[i] != len(stroka):
        if stroka[i] == 'О':
            counterer = 0

print(max(spisok))

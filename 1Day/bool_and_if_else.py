rating = 4.9
if rating > 4.7:
    print('Фильм крут')

print('Проверка окончена')







rating = 4.9

if rating > 4.7:
    print('Фильм крут')
else:

    print('Так себе киношечка')

print('Проверка окончена') 


#!!!  OR

bridge_1 = 'сведён'
bridge_2 = 'разведён'

if bridge_1 == 'сведён' or bridge_2 == 'сведён':
    print('Программист доберётся до дома')
else:
    print('Программист ночует в офисе') 



#  AND

x = -2
y = 5

if y >= 0 and x >= 0:
    print('Первая четверть')

elif y < 0 and x >= 0:
    print('Четвертая четверть')

elif y >= 0 and x < 0:
 print('Вторая четверть')

else:
    print('Третья четверть')
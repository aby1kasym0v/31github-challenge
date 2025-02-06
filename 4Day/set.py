toys = {'куклы', 'кубики', 'странная штука', 'самолетики', 'мелки'}
for toy in toys:
    print(toy)





movies = ['Матрица', 'Сеть', 'Хакеры', 'Трон', 'Тихушники', 'Сеть', 'Трон']
uniq_movies = set(movies)
print(uniq_movies)



num_string_1 = '100 13 2 143 12 3 55 4 64 18 56'

num_string_2 = '234 2 56 432 3 100 12 99 43 18 31 64'

overlap = set(num_string_1.split()) & set(num_string_2.split())
print(len(overlap))
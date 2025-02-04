name_movie = 'Матрица'

for symbol in name_movie:
    print((symbol + ' | ') * 7)

    print('——  ' * 7)








recommended_movies = ['Хатико', '23', 'Достучаться до небес',
                      'Хакеры', 'Трон', '1408']

hackers_movies = ['Трон', 'Военные игры', 'Тихушники',
                  'Джонни Мнемоник', 'Хакеры', 'Нирвана',
                  '23', 'Враг государства', 'Взлом',
                  'Пароль рыба-меч', 'Сеть', 'Кто я']

for movie in recommended_movies:
    if movie in hackers_movies:

        print(f'Разработчикам рекомендуем посмотреть фильм "{movie}"')







from random import choice

movies = ['Матрица', 'Хакеры', 'Трон', 'Тихушники', 'Сеть']

movie = choice(movies) 

print('Какой фильм мы будем смотреть?')
print(movies)
answer = input()  

while answer != movie: 
    answer = input('Попробуй еще: ')  

print('Молодец, угадал!')
 
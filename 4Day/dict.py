empty_dict = {}
print(empty_dict)




movies = [('Матрица', 4.7), ('Трон', 3.8)]
movies_dict = dict(movies)
print(movies_dict)





movies = {
    'Матрица': 4.7,
    'Хакеры': 4.3,
    'Трон': 3.8,
}
new_movies = {
    'Сеть': 4.1,
'23': 4.3, }
movies.update(new_movies)
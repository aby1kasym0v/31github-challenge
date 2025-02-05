movie_ratings = [4.7, 5.0, 4.3, 3.8]
new_movie_ratings = [rating + 0.2 for rating in movie_ratings]
print(new_movie_ratings)











numbers = [number ** 2 for number in range(1, 11)]

print(numbers)






movies = ['Матрица', 'Тихушники', 'Хакеры', 'Трон']
movie = movies.pop(2)
print(movie)
#Хакеры

print(movies)

#['Матрица', 'Тихушники', 'Трон']







force_words = ['сила', 'пребудет', 'с', 'тобой', 'Да']
print(id(force_words))

last = force_words.pop(-1)

first = force_words.pop(0)

force_words.insert(0, last)

force_words.append(first)

print(force_words)

# Убедимся, что это тот же объект, что и в начале программы

print(id(force_words))
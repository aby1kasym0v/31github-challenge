
# twelve = 4 * 3
# print('twelve =', twelve)


# two = 10 / 5
# print('two =', two)


# response = 424562

# # Переведите полученное значение в необходимые единицы измерения

# sec_in_days = 60 * 60 * 24

# sec_in_hours = 60 * 60

# sec_in_minutes = 60

# days = response // sec_in_days

# response = response % sec_in_days
# hours = response // sec_in_hours

# response = response % sec_in_hours

# minutes = response // sec_in_minutes

# seconds = response % sec_in_minutes

# print(days, hours, minutes, seconds)







weight = 75  # Вес

height = 175 # Рост

dist = 9.75  # Расстояние в км

hours = 2    # Время движения в часах


spent_calories = (0.035 * weight + (0.029 * weight) * (((dist/hours) ** 2) / height)) * hours * 60

print(spent_calories) 
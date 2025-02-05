package = ('2:00:01', 15000)
print(package)
print(type(package))





days = ('пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс')
steps = [1500, 3445, 13222, 10000, 12555, 1300, 6000]
def fabric():
    new_list = []
    count = 0
    for day in days:
        new_list.append((day, steps[count]))
        count += 1

    return new_list
result = fabric()
# Место для вашего кода
print(result)

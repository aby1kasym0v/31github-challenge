# Параметры функции - а и b
def never_print_result(a, b):
    pass




def get_mod_diff(a, b):
    diff = abs(a - b)
    return diff

x = 3
y = 4
print(get_mod_diff(x))



def test_range(start, end, *numbers): 
    result = []
    for i in numbers:
        if start <= i <= end:
            result.append(i)
        else:
            print('Число за границами диапазона')
    return result
start = 4
end = 12
print(test_range(start, end, 5, 16, 32, 6, 7, 1))

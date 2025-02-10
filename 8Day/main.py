# Парадигмы в Python

numbers: list = [1, 2, 3, 4, 5]
result: int = 0
for i in numbers:
    result += i
print(result) 




# Декларативный подход
def number_sum(data: list) -> int:
    result: int = 0
    for i in data:
        result += i
    return result

print(number_sum([1, 2, 3, 4, 5])) 


print(sum([1, 2, 3, 4, 5])) 
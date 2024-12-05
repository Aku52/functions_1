
print ('Введите радиус')
r =int(input ())
π = 3.14 # Постоянная

def square (r):
    
    return  (π*r**2)
result_1 = square (r)
print('Площадь круга равна', result_1)
# Площадь круга считаем по формуле

def length (r):
    
    return  (π*2*r)
result_2 = length (r)
# Длина окружности считаем по формуле

print('Длина окружности  равна', result_2)
# Выводим результат
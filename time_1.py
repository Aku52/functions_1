print ('Введите количество часов')
h =int(input ())
m = 60
s = 3600

def time (h):
    return h*m
result_1 = time (h)
print('В минутах', result_1)

def time (h):
    return h*s
result_2 = time (h)
print('В секундах', result_2)
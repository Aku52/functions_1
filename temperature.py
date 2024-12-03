print ('Введите градусы по Цельсия')
a =float(input ())

p = 1.8 
s = 32

def tem (a):
    return (a * p + s)

result = tem (a)
print('В системе Фаренгейту', result)
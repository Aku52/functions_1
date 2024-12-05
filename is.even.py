print ('Введите число')
a =int(input ())

def ch (a): 
    if (a % 2 == 0 ): # При делении на два остаток 0
        a = 'четное'
        return a
    else: # В противном случае 
        a = 'нечетное'
        return a
result = ch (a)
print(result)
# Выводим результат

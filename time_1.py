print ('Введите время через дефис')
user_input=input ()

# split - делит строку на элементы
user_input_1 = user_input.split('-')

list_el = list
# Создаем новый список и закидываем туда преобразованные элементы  
for i in range (0,len(user_input_1)):
    element = int(user_input_1[i])
    list_el.append(element)
      
# Понадобятся данные
m = 60 # В минуте количество секунд
h = 3600 # В часу количество секунд

# Считаем сумму элементов, переводя их в секунды
def tim (list_el):
    return list_el[0]*h + list_el[1]*m + list_el[2]
result = tim (list_el)

print ('Сумма часов, минут, секунд в секундах',result)
# Выводим результат
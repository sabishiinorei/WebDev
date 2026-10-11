print("\t -Задание №1-\n")
my_list = [1, 2, 3]
print("Было:", my_list)
my_list[0] = 100
print("Стало:", my_list)  
# Списки изменяемые, поэтому элемент поменялся без проблем

print("\t -Задание №2-\n")
my_tuple = (1, 2, 3)
print("Было:", my_tuple)
my_tuple[0] = 100  
# Кортежи неизменяемые, вылетит ошибка TypeError

print("\t -Задание №3-\n")
my_string = "cat"
print("Было:", my_string)
my_string[0] = "b"  
# Строки тоже неизменяемые, здесь будет такая же ошибка TypeError
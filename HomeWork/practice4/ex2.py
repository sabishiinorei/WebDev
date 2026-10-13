import math

x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))

dx = x1 - x2
dy = y1 - y2
distance = math.sqrt(dx**2 + dy**2)

print("Расстояние между точками:", distance)
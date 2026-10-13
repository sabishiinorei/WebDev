import math

angle_degrees = float(input("Введите угол в градусах: "))
angle_rad = math.radians(angle_degrees)

sin_val = math.sin(angle_rad)
cos_val = math.cos(angle_rad)
tan_val = math.tan(angle_rad)

result = sin_val + cos_val + tan_val ** 2
print("Ответ:", result)
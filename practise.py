# import math 
# seat_number = int(input("Введите номер места: "))
# carriage_number = (seat_number - 1) // 4 + 1
# print(f"Номер вагона: {carriage_number}")

# SEATS_PER_COMPARTMENT = 4

# seat_number = int(input("Введите номер места: "))
# compartment_number = (seat_number - 1) // SEATS_PER_COMPARTMENT + 1

# print(f"Номер купе: {compartment_number}")

# import math

# x1, y1 = map(float, input("Введите координаты 1-й точки (x1 y1): ").split())

# x2, y2 = map(float, input("Введите координаты 2-й точки (x2 y2): ").split())

# distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# print(f"Евклидово расстояние: {distance:.2f} метра")

import math


def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


x1, y1 = map(float, input("Введите координаты 1-й точки (x1 y1) через пробел: ").split())
x2, y2 = map(float, input("Введите координаты 2-й точки (x2 y2) через пробел: ").split())

distance = calculate_distance(x1, y1, x2, y2)

print(f"Евклидово расстояние между точками: {distance:.2f}")
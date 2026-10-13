students = int(input("Сколько студентов? "))
mandarins = int(input("Сколько мандаринов? "))

per_student = mandarins // students
remainder = mandarins % students

print("Каждому:", per_student)
print("Остаток:", remainder)
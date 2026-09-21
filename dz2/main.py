import random

#мини игра с компьютером
secret_number = random.randint(1, 100)
attempts = 0 

print("ИГРА: УГАДАЙ ЧИСЛО")
print("Я загадал число от 1 до 100. Попробуй угадать его!")


while True:

    user_guess = int(input("\nВведите ваше число: "))
    attempts += 1 

    if user_guess < secret_number:
        print("Загаданное число БОЛЬШЕ.")
    elif user_guess > secret_number:
        print("Загаданное число МЕНЬШЕ.")
    else:
        print(f"\n🎉 ПОЗДРАВЛЯЮ! Вы угадали число {secret_number}!")
        print(f"Количество затраченных попыток: {attempts}")
        break

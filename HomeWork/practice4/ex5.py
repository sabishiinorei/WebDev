total_minutes = int(input("Введите минуты: "))
hours = total_minutes // 60
remaining_minutes = total_minutes % 60

print(total_minutes, "минут - это", hours, "час", remaining_minutes, "минут")
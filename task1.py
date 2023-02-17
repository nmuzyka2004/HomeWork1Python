# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input("Введите число: "))
digit1 = number % 10
digit2 = number // 10 % 10
digit3 = number // 100
print(f"Сумма цифр числа {number} равна {digit1 + digit2 + digit3}")

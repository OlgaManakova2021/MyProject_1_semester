# Напишите программу, которая запрашивает у пользователя его
# возраст и выводит сообщение "Вы совершеннолетний(я)" или "Вы
# несовершеннолетний(я)", в зависимости от значения возраста (18 и больше
# - совершеннолетие).

print("Привет! Программа определит Ваше совершеннолетие!")
age = int(input("Введите Ваш возраст: "))
if 0 < age < 18:
    print("Вы несовершеннолетний(я)")
elif age >= 18:
    print("Вы совершеннолетний(я)")
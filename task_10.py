# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

amount_coins = int(input("Введите кол-во монеток: "))
if amount_coins<1:
    exit("Число монет должно быть больше 0")
position_coins = []
count0 = 0
count1 = 0

for i in range(amount_coins):
    position_coins.append(int(input("Укажите положение монетки(орел - 1 , решка - 0): ")))
    if position_coins[i] < 0 or position_coins[i] >1  :
        print("Введено неккоректное значение")
        break
    elif position_coins[i] == 0:
        count0 += 1
    else:
        count1 +=1


if count0>count1:
    print(f"Переверните {count1} монет с орла на решку")
elif count0==count1:
    print(f"Переверните {count1} монет с орла на решку")
else:
    print(f"Переверните {count0} монет с решки на орла")
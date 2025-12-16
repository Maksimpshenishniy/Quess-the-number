import random

secret_number = random.randint(1, 100)

attempts = 7

print("Вгадай число від 1 до 100. У тебе 7 спроб!")

while attempts > 0:
    guess = int(input("Введи свою спробу: "))
    attempts -= 1

    if guess == secret_number:
        print("Вітаю! Ти вгадав число!")
        break
    elif guess < secret_number:
        print("Більше")
    else:
        print("Менше")
    
    print(f"Залишилось спроб: {attempts}")

if attempts == 0 and guess != secret_number:
    print(f"Гру закінчено! Загадане число було: {secret_number}")
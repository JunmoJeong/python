import random

number = random.randint(1, 99)


chance = 10
count = 0

while count < chance:
    count += 1
    user_input = input("몇 일까요?")
    if number == user_input:
        print("정답")
        break
    else:
        print("아닙니다.")

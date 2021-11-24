import random
# 실행이 되면 화면을 깔끔하게 하고 싶다.
import os

number = random.randint(1, 99)
os.system("cls")  # 실행 화면 깨끗이
print("1부터 99까지의 숫자를 10번 안에 맞춰 보세요.")


def input_check(msg, casting=int):
    while True:
        try:
            user_input = casting(input("몇 일까요? "))
            return user_input
        except:
            continue


chance = 10
count = 0

while count < chance:
    count += 1
    user_input = input_check("몇 일까요?")
    if number == user_input:
        break
    elif user_input < number:
        print("{}보다 큰 숫자입니다.".format(user_input))
    elif user_input > number:
        print("{}보다 작은 숫자 입니다.".format(user_input))

if user_input == number:
    print("성공! {}이 맞습니다.".format(number))

else:
    print("실패, 정답은 {}입니다.".format(number))

import random
import os

numbers = []
number = str(random.randint(0, 9))  # 관리 편하기 위해서 문자로 관리

for i in range(3):
    while number in numbers:
        number = str(random.randint(0, 9))
    numbers.append(number)

so.system("cls")
# 사용자에게 입력 받는다.
print("*" * 60)
print("야구 게임을 싲가합니다.")
print("*" * 60)

count_strike = 0
count_ball = 0

while count_strike < 3:
    count_strike = 0
    count_ball = 0
    num = str(input("숫자 3자리를 입력하세요> "))
# str로 처리 했기 때문에 아니라 값이 아니라 문자열로 받기 때문에 편하다
    if len(num) == 3:
        for i in range(0, 3):
            for j in range(0, 3):
                if num[i] == num[j] and i == j:
                    count_strike += 1
                elif num[i] == numbers[j] and i != j:
                    count_ball += 1
        if count_strike == 0 and count_ball == 0:
            print("3 아웃!")
        else:
            output = ""
            if count_strike > 0:
                output += "{} 스트라이크.format(count_strike)"
            if count_ball > 0:
                output += "{} 볼".format(count_ball)

            print(output.strip())

print("게임 성공1")

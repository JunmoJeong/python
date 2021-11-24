import random

numbers = []
number = str(random.randint(0, 9))  # 관리 편하기 위해서 문자로 관리

for i in range(3):
    while number in numbers:
        number = str(random.randint(0, 9))
    numbers.append(number)

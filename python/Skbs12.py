import math

radius = float(input("원의 반지름을 입력하세요: "))
if radius > 0:
    area = math.pi * radius ** 2
    print(f"원의 넓이:)  {area:.2f}")
else:
    print("잘못된 값입니다.")
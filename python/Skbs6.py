import math

x1 = float(input("x1 입력: "))
y1 = float(input("y1 입력: "))
x2 = float(input("x2 입력: "))
y2 = float(input("y2 입력: "))

distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
print("두 점 사이 거리:", round(distance, 2))
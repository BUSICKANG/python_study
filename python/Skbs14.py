# 사용자로부터 키와 나이를 입력받음
height = int(input("키를 입력하세요 (cm): "))
age = int(input("나이를 입력하세요: "))

# 조건에 따라 입장 가능 여부 판단
if height >= 140 and age >= 10:
    print("입장 가능")
else:
    print("입장 불가")
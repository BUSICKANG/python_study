# 사용자로부터 키를 입력받음
height = int(input("키를 입력하세요 (cm): "))

# 표준 체중 계산
standard_weight = (height - 100) * 0.9
print(f"표준 체중은 {standard_weight}kg 입니다.")

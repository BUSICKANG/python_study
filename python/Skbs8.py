num = int(input("100000에서 999999 사이의 숫자 입력:"))
if 100000 <= num <= 999999:
    print("쉽표 구분 출력:", format(num, ","))
else:
    print("범위를 벗어난 숫자입니다.")
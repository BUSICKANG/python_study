num = int(input("4자리 정수 입력:"))
digit_sum = (num // 1000) + (num % 1000 // 100) + (num % 100 // 10) + (num % 10 // 1)
print("각 자릿수의 합:", digit_sum)
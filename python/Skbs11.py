shape = input("하나의 문자를 입력하세요(R/T/C): ")
if shape == 'R' or shape == 'r':
    print("Rectangle")
elif shape == 'T' or shape == 't':
    print("Triangle")
elif shape == 'C' or shape == 'c':
    print("Circle")
else :
    print("Unknown")
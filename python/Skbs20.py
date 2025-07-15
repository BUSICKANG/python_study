import random
import time

# 단어 목록 (확장 가능)
words = [
    "사과", "바나나", "포도", "수박", "멜론", "호랑이",
    "코끼리", "선생님", "학생", "연필", "지우개", "컴퓨터", "키보드", "마우스",
    "책상", "의자"
]

score = 0
lives = 3
speed = 2   # 단어 입력 시간 제한 (초)

print("한글 타자 시계 게임을 시작합니다!")
print("제한 시간 내에 단어를 정확히 입력하세요!")
print("기회는 3번! 시작합니다...\n")

time.sleep(2)

while lives > 0:
    target = random.choice(words)
    print(f"제시어: {target}")

    start = time.time()
    user_input = input("입력: ").strip()
    end = time.time()

    elapsed = end - start

    if elapsed > speed:
        print(f"시간 초과! ({elapsed:.1f}초 걸림)")
        lives -= 1
    elif user_input != target:
        print("오타! 정확히 입력해야 해요.")
        lives -= 1
    else:
        print("성공!")
        score += 1
    
    print(f"남은 목숨: {lives}, 점수: {score}, 제한시간: {speed:.1f}초\n")
    time.sleep(1)

print("\n게임 종료!")
print(f"최종 점수: {score}")
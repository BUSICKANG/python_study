import time
import random


proverb_list = [
    ["바람 앞의", "촛불도 끝까지 빛을 낸다."],
    ["작은 나뭇잎도", "바람을 만나면 춤춘다."],
    ["우물 안 개구리도", "하늘을 우러러 본다."],
    ["굽은 길이", "더 멀리 데려간다."],
    ["땀 한 방울이", "강을 만든다."],
    ["구름은 가도", "하늘은 남는다."],
    ["작은 불씨가", "큰 숲을 살린다."],
    ["나무는 뿌리로", "말하고 꽃으로 대답한다."],
    ["물이 고이면 썩고,", "흐르면 맑다."],
    ["빛은 벽을 만나도", "끝까지 간다."]
]

score = 0
total_questions = 5  # 총 문제 수

for i in range(total_questions): 
    front, back = random.choice(proverb_list)
    print(f"문제 {i+1}: {front}")


    # 첫 번째 입력
    user_answer = input("뒷부분을 입력하세요: ").strip()
    
    # 공백 무시하고 비교
    if user_answer.replace(" ", "") == back.replace(" ", ""):
        print("✅ 정답입니다!\n")
        score += 1
    else:
        # 틀렸을 경우 힌트 제공 (정답의 앞 3~5글자)
        hint_length = min(5, len(back))  # 5글자 이하로 제한
        hint = back[:hint_length] + "..."
        print(f"❌ 틀렸습니다! 힌트: \"{hint}\"")
        
        # 두 번째 기회
        user_second = input("힌트를 보고 다시 한 번 더 입력하세요: ").strip()
        if user_second.replace(" ", "") == back.replace(" ", ""):
            print("✅ 정답입니다! (두 번째 시도)\n")
            score += 1
        else:
            print(f"❌ 아쉽습니다! 정답은: \"{back}\"\n")

# 최종 점수 출력
print(f"\n게임종료!!! 당신의 총 최종 점수: {total_questions}게임 중 {score}점 입니다.")
import time
import random

list=["나는 사과를 좋아합니다.",
    "나는 배를 좋아합니다.",
    "나는 바나나를 좋아합니다.",
    "나는 감을 좋아합니다.",
    "나는 참외를 좋아합니다.",
    "나는 딸기를 좋아합니다.",
    "나는 대추를 좋아합니다.",
    "나는 밤을 좋아합니다.",
    "나는 메론을 좋아합니다."]

def pick_random_list():
    return random.choice(list)


target = pick_random_list()
print(pick_random_list())

input("준비되면 Ent를 누르세요")

start_time = time.time()
trial = 0
while True:
        
    typed = input("\n따라 쓰세요:")

    end_time = time.time()
    elapsed = end_time - start_time

    correct=0

    for i in range(min(len(target), len(typed))):
        if target[i] == typed[i]:
            correct += 1

    total = max(len(target), len(typed))

    accuracy = correct / total * 100
    speed = len(typed) / elapsed * 60

   if accuracy == 100:
    print("완료했어요.")
        break
    else:
        print("다시 시도해보세요.")
        trial += 1

print("\n결과")
print(f"걸린 시간")

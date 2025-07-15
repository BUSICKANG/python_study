import pygame
import random

# 초기화
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Typing Game!")
FONT = pygame.font.SysFont("malgun gothic", 48)
INPUT_FONT = pygame.font.SysFont("malgun gothic", 36)
TIMER = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER, 2000)
clock = pygame.time.Clock()

# 단어 리스트
# To Do List:
# 영어 단어들로만 구성된 List 생성
WORDS = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
    "iceberg", "jackfruit", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya",
    "quince", "raspberry", "strawberry", "tangerine", "ugli", "vanilla", "watermelon",
    "xigua", "yam", "zucchini", "apricot", "blueberry", "coconut", "dragonfruit",
    "eggplant", "feijoa", "guava", "hazelnut", "indigo", "jalapeno", "kumquat",
    "lime", "mulberry", "nutmeg", "olive", "peach", "quinoa", "radish", "spinach",
    "tomato", "upland", "vine", "wasabi", "xanthan", "yogurt", "zebra", "almond",
    "basil", "cinnamon", "dill", "espresso", "fennel", "garlic", "horseradish",
    "ivy", "jasmine", "kale", "lavender", "mint", "nutria", "oregano", "parsley",
    "quartz", "rosemary", "sage", "thyme", "umber", "violet", "walnut", "xylophone",
    "yellowtail", "zeppelin", "anchor", "bridge", "castle", "dolphin", "eagle",
    "forest", "galaxy", "harbor", "island", "jungle", "kingdom", "lagoon", "mountain",
    "nebula", "ocean", "prairie", "quarry", "river", "summit", "temple"
]
    
# 게임 상태 변수
user_input = ""
score = 0
lives = 3
falling_words = []

def get_random_word():
    return random.choice(WORDS)
    

def add_falling_word():
    """떨어지는 단어를 추가"""
    word = get_random_word()
    x = random.randint(50, 700)
    y = 0  # 화면 상단에서 시작
    speed = random.randint(2, 4)
    falling_words.append({"word": word, "x": x, "y": y, "speed": speed})

def update_words():
    """떨어지는 단어들의 위치 업데이트"""
    for word in falling_words:
        word["y"] += word["speed"]

def check_input():
    """사용자 입력과 떨어지는 단어 비교"""
    global score, user_input
    for word in falling_words:
        if word["word"] == user_input:
            falling_words.remove(word)
            score += 10
            user_input = ""
            return True
    return False

def check_missed():
    """화면 아래로 넘어간 단어 처리"""
    global lives
    missed_words = [word for word in falling_words if word["y"] > 600]
    for word in missed_words:
        falling_words.remove(word)
        lives -= 1
    

def draw_words():
    for word in falling_words:
        text = FONT.render(word["word"], True, (255, 255, 255))
        screen.blit(text, (word["x"], word["y"]))

def draw_ui():
    draw_words()
    input_text = INPUT_FONT.render(f"입력: {user_input}", True, (0, 255, 0))
    score_text = INPUT_FONT.render(f"점수: {score}", True, (255, 255, 0))
    lives_text = INPUT_FONT.render(f"목숨: {lives}", True, (255, 100, 100))
    screen.blit(input_text, (20, 550))
    screen.blit(score_text, (650, 20))
    screen.blit(lives_text, (650, 60))

# 메인 루프
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == TIMER:
            add_falling_word()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            elif event.key == pygame.K_RETURN:
                check_input()
            else:
                user_input += event.unicode

    update_words()
    check_missed()
    draw_ui()

    if lives <= 0:
        game_over_text = FONT.render("Game Over", True, (255, 0, 0))
        screen.blit(game_over_text, (300, 250))
        pygame.display.update()
        pygame.time.wait(3000)
        running = False

    pygame.display.update()
    clock.tick(30)

pygame.quit()
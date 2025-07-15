import pygame

# 초기화
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PYGAME!")
clock = pygame.time.Clock()


#FONT = pygame.font.Sysfont("Malgun Gothic", 48) #글자체
#FONT = pygame.font.Sysfont("Malgun Gothic", 48) #글자체
#FONT = pygame.font.Sysfont("Malgun Gothic", 48) #글자체
FONT = pygame.font.SysFont("Malgun Gothic", 48) #글자체
text = FONT.render("Intel", True, (255, 255, 255))

x = 330
y = 0

img = pygame.image.load("gobu.jpg")
img = pygame.transform.scale(img,  (300, 300))

while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
            elif event.key == pygame.K_LEFT:
                x -= 10
            elif event.key == pygame.K_RIGHT:
                x += 10
            elif event.key == pygame.K_UP:
                y -= 10
            elif event.key == pygame.K_DOWN:
                y += 10

    #y += 1
    #if y > 600:
    
     #   y = 0
        
    screen.blit(text, (300, 5))
    pygame.display.update()
    screen.blit(img, (x, y)) #그림어떤 위치
  
    pygame.display.update()

    clock.tick(25)

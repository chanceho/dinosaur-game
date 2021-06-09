import pygame
pygame.init()

screen = pygame.display.set_mode((600,300))

pygame.display.set_caption('Dinosaur')

WHITE = (255,255,255)
RED = (255,0,0)

background_x,background_y = 0, 0
dinosaur_x, dinosaur_y = 0, 230
tree_x, tree_y = 550, 230
x_velocity, y_velocity = 5, 7

score = 0

font = pygame.font.SysFont('san', 20)
font1 = pygame.font.SysFont('san', 40)

background = pygame.image.load('background.jpg')
dinosaur = pygame.image.load('dinosaur.png')
tree = pygame.image.load('tree.png')
sound1 = pygame.mixer.Sound('tick.wav')
sound2 = pygame.mixer.Sound('te.wav')
clock = pygame.time.Clock()

jump = False
pausing = False
running = True

while running:
    clock.tick(60)
    screen.fill(WHITE)
    
    background1_rect = screen.blit(background, (background_x, background_y))
    background2_rect = screen.blit(background, (background_x+600, background_y))
    dinosaur_rect = screen.blit(dinosaur, (dinosaur_x, dinosaur_y))
    score_txt = font.render('Score: '+ str(score), True, RED)
    screen.blit(score_txt,(5,5))
    background_x -= x_velocity
    if background_x+600 < 0:
        background_x = 0
    tree_x -= x_velocity
    if tree_x <= -20:
        tree_x = 550
        score += 1
    if 80 <= dinosaur_y <= 230:
        if jump == True:
            dinosaur_y -= y_velocity
    else:
        jump = False
    if dinosaur_y < 230:
        if jump == False:
            dinosaur_y += y_velocity

    dinosaur_rect = screen.blit(dinosaur, (dinosaur_x, dinosaur_y))
    tree_rect = screen.blit(tree, (tree_x, tree_y))

    if dinosaur_rect.colliderect(tree_rect):
        pygame.mixer.Sound.play(sound2)
        pausing = True
        gameover_txt = font1.render("Game Over", True, RED)
        screen.blit(gameover_txt,(200,150))
        x_velocity, y_velocity = 0, 0
        pygame.mixer.pause()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                if dinosaur_y == 230:
                    pygame.mixer.Sound.play(sound1)
                    jump = True
                if pausing:
                    background_x, background_y = 0, 0
                    dinosaur_x, dinosaur_y = 0, 230
                    tree_x, tree_y = 550, 230
                    x_velocity, y_velocity = 5, 7
                    score = 0
                    pausing = False

    pygame.display.flip()
pygame.quit()
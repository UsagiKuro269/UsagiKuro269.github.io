import pygame
import sys
import random
#some important thing to fill in
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("Arial", 30)
font1 = pygame.font.SysFont("Forte", 40)

#settings
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREY = (137, 137, 137)
RED = (255, 0, 0)
SEABLUE = (0, 140, 191)

running = True
pygame.mixer.music.load("music1.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

status = "menu"
head_x, head_y = 400.0, 300.0
trail = [(400.0, 300.0)]
velocity = 0.05
spacing = 15
score = 0
snake_length = 1
fruit_x = random.randint(50, WIDTH-10)
fruit_y = random.randint(50, HEIGHT-110)
#main menu
while running:
#currently in main menu
    if status == "menu":
     screen.fill(WHITE)
     pygame.draw.rect(screen, BLACK, (0,0,250,800))

     text_game = font1.render("Placeholder", True, WHITE)#whatever text is this
     rect_game = text_game.get_rect(center=(125,50))#adjusting position of the text
     screen.blit(text_game, rect_game)#make it appears in the game

     text_new_game = font.render("New Game", True, WHITE)
     rect_new_game = text_new_game.get_rect(center=(125,200))
     screen.blit(text_new_game, rect_new_game)

     text_load_game = font.render("Load Game", True, GREY)
     rect_load_game = text_load_game.get_rect(center=(125,300))
     screen.blit(text_load_game, rect_load_game)

     text_settings = font.render("Settings", True, WHITE)
     rect_settings = text_settings.get_rect(center=(125,400))
     screen.blit(text_settings, rect_settings)

     text_exit = font.render("Exit", True, WHITE)
     rect_exit = text_exit.get_rect(center=(125,500))
     pygame.draw.rect(screen, RED, rect_exit)
     screen.blit(text_exit, rect_exit)

     text_ver = font.render("Ver: 1.0.0", True, BLACK)
     rect_ver = text_ver.get_rect(center=(725,575))
     screen.blit(text_ver, rect_ver)
    
    elif status == "playing":
     screen.fill(BLACK)
     pygame.draw.rect(screen, SEABLUE, (0,0,800,100))

     text_score = font.render(f"Score: {score}", True, WHITE)
     rect_score = text_score.get_rect(center=(400,50))
     screen.blit(text_score, rect_score)

     trail.insert(0, (head_x, head_y))

      #collision detection with fruit
     head_rect = font.render("o", True, WHITE).get_rect(center=(head_x, head_y))
     fruit_rect = font.render("b", True, RED).get_rect(center=(fruit_x, fruit_y))

     if head_rect.colliderect(fruit_rect):
            score += 1
            snake_length += 1
            fruit_x = random.randint(50, WIDTH-50)
            fruit_y = random.randint(50, HEIGHT-50)

   
   snake = []
     dist = 0
    for i in range(len(trail) - 1):
            if len(snake) >= snake_length:
                break
            x1, y1 = trail[i]
            x2, y2 = trail[i + 1]
            segment_dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            dist += segment_dist
            if dist >= spacing:
                snake.append((x1, y1))
                dist = 0

       
    for segment in snake:
            text_segment = font.render("o", True, WHITE)
            rect_segment = text_segment.get_rect(center=(segment[0], segment[1]))
            screen.blit(text_segment, rect_segment)

    text_fruit = font.render("o", True, RED)
    rect_fruit = text_fruit.get_rect(center=(fruit_x,fruit_y))
    screen.blit(text_fruit, rect_fruit)

    text_back = font.render("X", True, RED)
    rect_back = text_back.get_rect(center=(50,50))
    screen.blit(text_back, rect_back)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Exiting Game")
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if status == "menu":
               if event.type == pygame.MOUSEBUTTONDOWN:
                  mouse_pos = event.pos
                  if rect_new_game.collidepoint(event.pos):
                     status = "playing"
                  elif rect_load_game.collidepoint(event.pos):
                     status = "playing"
                  elif rect_settings.collidepoint(event.pos):
                     status = "settings"
                  elif rect_exit.collidepoint(event.pos):
                     running = False
            elif status == "playing":
                  if rect_back.collidepoint(event.pos):
                     status = "menu"

    pygame.display.flip()
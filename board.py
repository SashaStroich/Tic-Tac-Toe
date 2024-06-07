import pygame
import sys

pygame.init()

size = (340, 340)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Христики-Нолики")
width = height = 100
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
margin = 10
mas = [[0]*3 for _ in range(3)]
turn = 0  

font = pygame.font.Font(None, 36)

def check_win():
    
    for row in mas:
        if row[0] == row[1] == row[2] != 0:
            return True, row[0]

    
    for col in range(3):
        if mas[0][col] == mas[1][col] == mas[2][col] != 0:
            return True, mas[0][col]

    
    if mas[0][0] == mas[1][1] == mas[2][2] != 0:
        return True, mas[0][0]
    if mas[0][2] == mas[1][1] == mas[2][0] != 0:
        return True, mas[0][2]

    return False, None

def reset_game():
    global mas, turn
    mas = [[0]*3 for _ in range(3)]
    turn = 0

reset_game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                reset_game()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if turn == 0:
                x_mouse, y_mouse = pygame.mouse.get_pos()
                column = x_mouse//(margin+width)
                row = y_mouse//(margin+height)
                if mas[row][column] == 0:
                    mas[row][column] = 'X'
                    turn = 1
            else:
                x_mouse, y_mouse = pygame.mouse.get_pos()
                column = x_mouse//(margin+width)
                row = y_mouse//(margin+height)
                if mas[row][column] == 0:
                    mas[row][column] = 'O'
                    turn = 0

    screen.fill(white)
    
    
    for row in range(3):
        for col in range(3):
            x = col*width+(col+1)*margin
            y = row * height + (row + 1) * margin
            pygame.draw.rect(screen, black, (x,y,width,height), 3)
            if mas[row][col] == 'X':
                pygame.draw.line(screen, red, (x+10, y+10), (x+width-10, y+height-10), 2)
                pygame.draw.line(screen, red, (x+width-10, y+10), (x+10, y+height-10), 2)
            elif mas[row][col] == 'O':
                pygame.draw.circle(screen, red, (x+width//2, y+height//2), width//2 - 10, 2)

    
    win, winner = check_win()
    if win:
        text = font.render(f"Гравець {winner} Виграв!  Натисніть пробіл щоб розпочати знову.", True, black)
        text_rect = text.get_rect(center=(size[0] // 2, size[1] // 2))
        screen.blit(text, text_rect)
    elif all(all(cell != 0 for cell in row) for row in mas):
        text = font.render("Нічия! Натисніть пробіл щоб зіграти знову.", True, black)
        text_rect = text.get_rect(center=(size[0] // 2, size[1] // 2))
        screen.blit(text, text_rect)
    else:
        text = font.render("Хрестики-Нолики", True, black)
        text_rect = text.get_rect(center=(size[0] // 2, size[1] // 2))
        screen.blit(text, text_rect)

    pygame.display.update()





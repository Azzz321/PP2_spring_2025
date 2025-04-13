import pygame
import math

white = (255, 255, 255)
eraser = (0, 0, 0)
green = (34, 139, 34)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
orange = (255, 165, 0)
purple = (128, 0, 128)

#drawing tips
def draw_tips(screen, font):
    tips = [
        "Controls:",
        "R - Red", "G - Green", "B - Blue", "Y - Yellow", "O - Orange", "P - Purple", "W - White",
        "X - Rectangle", "C - Circle", "S - Square", "T - Right Triangle", "A - Equilateral Triangle", "D - Rhombus",
        "Backspace - Eraser"
    ]
    y_offset = 5
    for tip in tips:
        text_surface = font.render(tip, True, white)
        screen.blit(text_surface, (5, y_offset))
        y_offset += 20

def main():
    #initializing and screen
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Paint")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 16)
    
    radius = 2
    mode = white
    last_pos = None

    #main loop
    while True:
        draw_tips(screen, font)  
        #determining if any letter key is pressed 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    mode = red
                elif event.key == pygame.K_g:
                    mode = green
                elif event.key == pygame.K_b:
                    mode = blue
                elif event.key == pygame.K_y:
                    mode = yellow
                elif event.key == pygame.K_w:
                    mode = white
                elif event.key == pygame.K_o:
                    mode = orange
                elif event.key == pygame.K_p:
                    mode = purple
                elif event.key == pygame.K_x:    
                    drawRectangle(screen, pygame.mouse.get_pos(), 200, 100, mode)
                elif event.key == pygame.K_c:
                    drawCircle(screen, pygame.mouse.get_pos(), mode)
                elif event.key == pygame.K_s:
                    drawSquare(screen, pygame.mouse.get_pos(), 200, mode)
                elif event.key == pygame.K_t:
                    drawRightTriangle(screen, pygame.mouse.get_pos(), 200, 100, mode)
                elif event.key == pygame.K_a:
                    drawEquilateralTriangle(screen, pygame.mouse.get_pos(), 200, mode)
                elif event.key == pygame.K_d:
                    drawRhombus(screen, pygame.mouse.get_pos(), 100, 150, mode)
                if event.key == pygame.K_BACKSPACE:
                    radius = 20
                    mode = eraser
                else:
                    radius = 2
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                last_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEMOTION and event.buttons[0]:
                #draw a line from the last point to the current point 
                if last_pos is not None:
                    start_pos = last_pos
                    end_pos = pygame.mouse.get_pos()
                    drawLineBetween(screen, start_pos, end_pos, radius, mode)
                    last_pos = end_pos
        
        pygame.display.flip()
        clock.tick(60)
#drawing a line
def drawLineBetween(screen, start, end, width, color_mode):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    for i in range(iterations):
        progress = 1.0 * i / iterations
        x = int((1 - progress) * start[0] + progress * end[0])
        y = int((1 - progress) * start[1] + progress * end[1])
        pygame.draw.circle(screen, color_mode, (x, y), width)
#drawing the figures
def drawRectangle(screen, mouse_pos, w, h, color):
    pygame.draw.rect(screen, color, (*mouse_pos, w, h), 4)

def drawCircle(screen, mouse_pos, color):
    pygame.draw.circle(screen, color, mouse_pos, 100, 5)

def drawSquare(screen, mouse_pos, side_length, color):
    pygame.draw.rect(screen, color, (*mouse_pos, side_length, side_length), 4)

def drawRightTriangle(screen, mouse_pos, width, height, color):
    points = [mouse_pos, (mouse_pos[0] + width, mouse_pos[1]), (mouse_pos[0], mouse_pos[1] + height)]
    pygame.draw.polygon(screen, color, points, 4)

def drawEquilateralTriangle(screen, mouse_pos, side_length, color):
    height = side_length * math.sqrt(3) / 2
    points = [mouse_pos, (mouse_pos[0] + side_length, mouse_pos[1]), (mouse_pos[0] + side_length / 2, mouse_pos[1] + height)]
    pygame.draw.polygon(screen, color, points, 4)

def drawRhombus(screen, mouse_pos, width, height, color):
    points = [
        (mouse_pos[0], mouse_pos[1] + height / 2),
        (mouse_pos[0] + width / 2, mouse_pos[1]),
        (mouse_pos[0] + width, mouse_pos[1] + height / 2),
        (mouse_pos[0] + width / 2, mouse_pos[1] + height)
    ]
    pygame.draw.polygon(screen, color, points, 4)

main()

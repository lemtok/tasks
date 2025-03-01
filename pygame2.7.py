import pygame

pygame.init()
size = 500, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Прямоугольники с Ctrl+Z")
clock = pygame.time.Clock()
rect_list = []
FPS = 60

if __name__ == '__main__':
    draw_flag = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    draw_flag = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    draw_flag = True
                    rect_list.append([*event.pos, *event.pos])
            if event.type == pygame.KEYDOWN:
                mods = pygame.key.get_mods()
                if event.key == pygame.K_z and (mods & pygame.KMOD_CTRL) and rect_list:
                    rect_list.pop(-1)

        screen.fill((0, 0, 0))

        if draw_flag:
            pos = pygame.mouse.get_pos()
            rect_list[-1] = [rect_list[-1][0], rect_list[-1][1], *pos]
        for x1, y1, x2, y2 in rect_list:
            if x2 - x1 < 0:
                width = min(x2 - x1, -10)
            else:
                width = max(x2 - x1, 10)
            if y2 - y1 < 0:
                height = min(y2 - y1, -10)
            else:
                height = max(y2 - y1, 10)
            
            pygame.draw.rect(screen, pygame.Color('white'), pygame.Rect(x1, y1, width, height), 5, 5)

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
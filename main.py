from random import seed
from random import randint
import pygame

with open("word_search.txt", "r") as f:
    word_grid = [line.split() for line in f]

with open("key.txt") as k:
    keywords = k.read().split(" ")

new_grid = [x[:] for x in word_grid]
solved = []


def check(x, y, xdir, ydir, key):
    # key is the word that is being found not the list of keywords
    try:
        final = [[key[0], x, y]]
        ogx = x
        ogy = y
        ax = x
        ay = y
        for a in range(1, len(key)):
            # print(word_grid[x+xdir][y+ydir])
            if word_grid[x + xdir][y + ydir] == key[a]:
                x += xdir
                y += ydir
                final.append([])
                final[a].append(key[a])
                final[a].append(x)
                final[a].append(y)
            else:
                break

        if len(final) == len(key):
            print(final)
            solved.append(final)

    except IndexError:
        return;


for k in range(len(keywords)):
    print('looking for ', keywords[k])
    for i in range(len(word_grid)):

        for j in range(len(word_grid[i])):

            if keywords[k][0] == word_grid[i][j]:

                try:

                    if keywords[k][1] == word_grid[i + 1][j]:
                        # print(keywords[k][0],keywords[k][1],i,j)
                        check(i, j, 1, 0, keywords[k])

                except IndexError:
                    pass

                try:

                    if keywords[k][1] == word_grid[i - 1][j]:
                        # print(keywords[k][0],keywords[k][1],i,j)
                        check(i, j, -1, 0, keywords[k])

                except IndexError:
                    pass

                try:

                    if keywords[k][1] == word_grid[i][j + 1]:
                        # print(keywords[k][0],keywords[k][1],i,j)
                        check(i, j, 0, 1, keywords[k])

                except IndexError:
                    pass

                try:

                    if keywords[k][1] == word_grid[i][j - 1]:
                        # print(keywords[k][0],keywords[k][1],i,j)
                        check(i, j, 0, -1, keywords[k])

                except IndexError:
                    pass

                try:

                    if keywords[k][1] == word_grid[i + 1][j + 1]:
                        # print(keywords[k][0],keywords[k][1],i,j)
                        check(i, j, 1, 1, keywords[k])

                except IndexError:
                    pass

                try:

                    if keywords[k][1] == word_grid[i + 1][j - 1]:
                        # print(keywords[k][0],keywords[k][1],i,j)
                        check(i, j, 1, -1, keywords[k])

                except IndexError:
                    pass

                try:

                    if keywords[k][1] == word_grid[i - 1][j - 1]:
                        # print(keywords[k][0],keywords[k][1],i,j)
                        check(i, j, -1, -1, keywords[k])

                except IndexError:
                    pass

                try:

                    if keywords[k][1] == word_grid[i - 1][j + 1]:
                        # print(keywords[k][0],keywords[k][1],i,j)
                        check(i, j, -1, 1, keywords[k])

                except IndexError:
                    pass


###Pygame Part###

pygame.init()

clock = pygame.time.Clock()

display_width = 600
display_height = 600
y_len = len(word_grid)
x_len = len(word_grid[0])
one = (84, 232, 123)
two = (232, 84, 84)
three = (84, 106, 232)
four = (232, 153, 84)
five = (84, 225, 232)
six = (230, 84, 232)

gameDisplay = pygame.display.set_mode((display_width, display_height))

def message_display(text, size, color, x, y):
    textDetails = pygame.font.Font('freesansbold.ttf', size)
    TextSurf, TextRect = text_objects(text, textDetails, color)
    TextRect.center = (int(x), int(y))
    gameDisplay.blit(TextSurf, TextRect)

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

stopped = False

while not stopped:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stopped = True

    gameDisplay.fill((255, 255, 255))
    #pygame.draw.rect(gameDisplay, (0, 0, 0), (int(display_width / 20), int(display_height / 6), int(display_width - display_width / 10), int(display_height - display_height / 5)))
    #pygame.draw.rect(gameDisplay, (255, 255, 255), (int(display_width / 15), int(display_height / 5.6), int(display_width - display_width / 7.7), int(display_height - display_height / 4.5)))
    message_display('Word Search Solver', 45, (0, 0, 0), display_width / 2, display_height / 12)
    for i in range(len(word_grid)):
        for j in range(len(word_grid[i])):
            message_display(word_grid[i][j], 10, (0, 0, 0), int((display_width / 25) + ((j+1) * display_width/x_len/1.14)), int((display_height / 7) + ((i+1) * display_height/y_len/1.27)))

    for i in range(len(solved)):
        x1 = solved[i][0][1]
        y1 = solved[i][0][2]
        x2 = solved[i][-1][1]
        y2 = solved[i][-1][2]
        colorNum = i % 6
        color = None
        if colorNum == 0:
            color = one
        elif colorNum == 1:
            color = two
        elif colorNum == 2:
            color = three
        elif colorNum == 3:
            color = four
        elif colorNum == 4:
            color = five
        elif colorNum == 5:
            color = six
        pygame.draw.line(gameDisplay, color, (int((display_width / 25) + ((y1+1) * display_width/x_len/1.14)), int((display_height / 7) + ((x1+1) * display_height/y_len/1.27))), (int((display_width / 25) + ((y2+1) * display_width/x_len/1.14)), int((display_height / 7) + ((x2+1) * display_height/y_len/1.27))), 3)

    pygame.display.update()
    clock.tick(60)

print(solved)
pygame.quit()
quit()
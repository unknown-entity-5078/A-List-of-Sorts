# Declaring Variables
heightList = []
listLength = 10
numOfSelections = 0
numOfSwaps = 0
swap = False
size = (1000, 700)

# coordinate for drawing
xList, y, w = [], 0, size[0]/listLength

def bubblesort(speed, length):
    import pygame
    from random import randint

    global heightList, xList, w, listLength, numOfSelections, numOfSwaps, swap, size

    # Reset variables
    heightList = []
    xList = []
    numOfSelections = 0
    numOfSwaps = 0
    swap = False

    # Change accordance to length and speed input
    listLength = length
    w = size[0]/listLength
    
    # Initializing the window
    pygame.init()
    window = pygame.display.set_mode((size))
    pygame.display.set_caption("Bubble-Sort Visualization")
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)

    # Creating all the random numbers
    for i in range(listLength):
        heightList.append(randint(0, 400))
        xList.append(w*i)

    # Displaying bars on the window


    def draw():
        global xList, y, heightList
        window.fill(black)
        for i in range(listLength):
            pygame.draw.rect(
                window, white, (xList[i], 400-heightList[i], w, heightList[i]), 0)


    def buffer():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


    def update_draw(speed):
        pygame.display.update()
        pygame.time.Clock().tick(int(5*speed))


    # Algorithm
    for i in range(listLength-1, 0, -1):
        for j in range(i):
            draw()
            update_draw(speed)

            if swap:
                pygame.draw.rect(
                    window, green, (xList[j], 400-heightList[j], w, heightList[j]), 0)
                swap = False
            else:
                pygame.draw.rect(
                    window, red, (xList[j], 400-heightList[j], w, heightList[j]), 0)

            update_draw(speed)

            if heightList[j] > heightList[j+1]:
                heightList[j], heightList[j+1] = heightList[j+1], heightList[j]
                swap = True

                numOfSelections += 1
                numOfSwaps += 1

            numOfSelections += 1

            buffer()

    # Sort ended

    # Print sorted list to console
    print(heightList)
    print("Selections: {}\nSwaps: {}".format(numOfSelections, numOfSwaps))

    # Ending animation
    # green going up
    for i in range(listLength):
        pygame.draw.rect(
            window, green, (xList[i], 400-heightList[i], w, heightList[i]), 0)
        update_draw(speed)

        buffer()
    # green going down
    for i in range(listLength-1, -1, -1):
        pygame.draw.rect(
            window, white, (xList[i], 400-heightList[i], w, heightList[i]), 0)
        update_draw(speed)

        buffer()

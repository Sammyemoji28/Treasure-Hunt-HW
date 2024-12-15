
import pygame
import random
import time
import sys

pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Treasure Hunt HW")

WIDTH = 600
HEIGHT = 600

WHITE = (255,255,255)
BLACK = (0,0,0)
PURPLE = (147,112,219)
BLUE = (173,216,230)
PINK = (255,209,220)

gridSize = 30
cellSize = WIDTH//gridSize
obstacleNum = 40
score = 0
gameover = False

treasurePos = []
obstaclePos = []
playerPos = [gridSize//2, gridSize//2]

font = pygame.font.SysFont("arial", 25)

FPS = 30
clock = pygame.time.Clock()

def drawGrids():
    for x in range(0, WIDTH, cellSize):
        pygame.draw.line(screen, WHITE, (x,0), (x,HEIGHT))
    for y in range(0, HEIGHT,cellSize):
        pygame.draw.line(screen, WHITE, (0,y), (WIDTH, y))

def restartGame():
    global playerPos, treasurePos, obstaclePos, score
    playerPos = [gridSize//2, gridSize//2]
    treasurePos = [[random.randint(0, gridSize - 1), random.randint(0, gridSize - 1)] for i in range(3)]
    obstaclePos = []
    while len(obstaclePos) < obstacleNum:
        pos = [random.randint(0, gridSize - 1), random.randint(0, gridSize - 1)]
        if pos != playerPos and pos not in treasurePos and pos not in obstaclePos:
            obstaclePos.append(pos)

def createPlayer():
    pygame.draw.rect(screen, PURPLE, (playerPos[0] * cellSize, playerPos[1] * cellSize, cellSize, cellSize))

def createTreasure():
    for pos in treasurePos:
        pygame.draw.rect(screen, BLUE, (pos[0] * cellSize, pos[1] * cellSize, cellSize, cellSize))

def createObstacles():
    for pos in obstaclePos:
        pygame.draw.rect(screen, PINK, (pos[0] * cellSize, pos[1] * cellSize, cellSize, cellSize))

def checkCollision():
    for pos in treasurePos:
        if pos == playerPos:
            treasurePos.remove(pos)
            return True
    return False

restartGame()

while True:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and playerPos[0] > 0:
        playerPos[0] -= 1
    if keys[pygame.K_RIGHT] and playerPos[0] < gridSize - 1:
        playerPos[0] += 1
    if keys[pygame.K_UP] and playerPos[1] > 0:
        playerPos[1] -= 1
    if keys[pygame.K_DOWN] and playerPos[1] < gridSize - 1:
        playerPos[1] += 1

    if checkCollision():
        score += 1
        if len(treasurePos) == 0:
            restartGame()
    if playerPos in obstaclePos:
        gameover = True
        score = 0
        restartGame()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    drawGrids()
    createPlayer()
    createTreasure()
    createObstacles()
    text = font.render(f"Score : {str(score)}", False, PURPLE)
    screen.blit(text, (30,30))
    clock.tick(FPS)
    pygame.display.flip()

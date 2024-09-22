import random
import pygame
from calcVelocidades import calculoVelocidades
import numpy

# Particula 1
x1, vx1 = random.uniform(30,720), random.uniform(-1000,1000)
y1, vy1 = random.uniform(650,700), random.uniform(-50,50)
r1 = 25
m1 = 1

# Particula 2
x2, vx2 = random.uniform(30,720), random.uniform(-1000,1000)
y2, vy2 = random.uniform(650,700), random.uniform(-50,50)
r2 = 25
m2 = 2

# Parâmetros da simulação
space_size = 750
ay = 2500
rate = 500
dt = 1/1000
t1 , t2 = 0, 0

pygame.init()

clock = pygame.time.Clock()

# Set up the drawing window
screen = pygame.display.set_mode([space_size, space_size])

vy0_1 = vy1
vy0_2 = vy2

# Run until the user asks to quit
running = True
while running:

    px_total = m1 * vx1 + m2 * vx2
    py_total = m1 * vy1 + m2 * vy2

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with black
    screen.fill((0, 0, 0))

    pygame.draw.line(screen, (255, 255, 255), (0, space_size/2), (space_size, space_size/2), 1)

    pygame.draw.line(screen, (255, 255, 255), (space_size/2, 0), (space_size/2, space_size), 1)

    pygame.draw.line(screen, (255, 0, 0), (375, 375), (375 + px_total, 375), 3)

    pygame.draw.line(screen, (0, 0, 255), (375, 375), (375, 375 - py_total), 3)

    pygame.draw.line(screen, (0, 255, 0), (340, 375), (340, 375 - 0.00005*((750 - y1)*ay*m1 + (750 - y2)*ay*m2 + 0.5*m1*(vy1*vy1 + vx1*vx1)+ 0.5*m2*(vy2*vy2 + vx2*vx2))), 3)

    pygame.draw.line(screen, (255, 0, 255), (300, 375), (300, 375 - ( (750 - y1)*ay*m1*0.00005 + 0.00005 * 0.5 * m1 * (vy1 * vy1 + vx1 * vx1) ) ), 3)

    pygame.draw.line(screen, (125, 255, 125), (300, 375), (300, 375 - ( (750 - y1)*ay*m1*0.00005 ) ), 3)

    pygame.draw.line(screen, (0, 255, 255), (260, 375), (260, 375 - ( (750 - y2)*ay*m2*0.00005 + 0.00005 * 0.5 * m2 * (vy2 * vy2 + vx2 * vx2) ) ), 3)

    pygame.draw.line(screen, (255, 125, 125), (260, 375), (260, 375 - ( (750 - y2)*ay*m2*0.00005 ) ), 3)

    pygame.draw.circle(screen, (255, 255, 255), (x1, y1), r1)

    pygame.draw.circle(screen, (255, 0, 0), (x2, y2), r2)

    if x1 > space_size - r1 or x1 < r1:
        vx1 = -vx1

    if y1 > space_size - r1 or y1 < r1:
        vy1 = -vy1
        vy0_1 = vy1
        t1 = 0

    if x2 > space_size - r2 or x2 < r2:
        vx2 = -vx2

    if y2 > space_size - r2 or y2 < r2:
        vy2 = -vy2
        vy0_2 = vy2
        t2 = 0

    if (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)<(r1+r2)*(r1+r2):
        vx1, vy1, vx2, vy2 = calculoVelocidades(m1,x1,y1,vx1,vy1,m2,x2,y2,vx2,vy2)
        vy0_1 = vy1
        vy0_2 = vy2
        t1 = 0
        t2 = 0

    x1 = x1 + vx1 * dt

    k1y_1 = vy0_1 + ay * t1
    k2y_1 = vy0_1 + ay * (t1 + (dt/2))
    k3y_1 = vy0_1 + ay * (t1 + (dt/2))
    k4y_1 = vy0_1 + ay * (t1 + dt)

    y1 = y1 + (1/6)*(k1y_1+2*k2y_1+2*k3y_1+k4y_1)*dt

    vy1 = (vy1 + ay * dt)

    x2 = x2 + vx2 * dt

    k1y_2 = vy0_2 + ay * t2
    k2y_2 = vy0_2 + ay * (t2 + (dt / 2))
    k3y_2 = vy0_2 + ay * (t2 + (dt / 2))
    k4y_2 = vy0_2 + ay * (t2 + dt)

    y2 = y2 + (1 / 6) * (k1y_2 + 2 * k2y_2 + 2 * k3y_2 + k4y_2) * dt

    vy2 = (vy2 + ay * dt)

    t1 = t1 + dt
    t2 = t2 + dt

    clock.tick(rate)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
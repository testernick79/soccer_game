import pygame, sys
import general
import randon
from pygame.locals import *
from creature import *
from field import *
import ai

def monsterTest(rootNode1_acc, rootNode2_acc, showing=False, time_length=None, playing=False, online=False):
    balls = 1
    players = 2
    skulls = 0

    balls = list()
    players = list()
    skulls = list()

    if online:
        socket,
        isClient = tcp_connect(ip_address)

    if not playing:
        rootNode1_accX = rootNode1_acc[0]
        rootNode1_accY = rootNode1_acc[1]
        rootNode2_accX = rootNode2_acc[0]
        rootNode2_accY = rootNode2_acc[1]

    if showing:
        pygame.display.set_caption('Soccer Game')
        general.surface = pygame.display.get_surface()
        field = Field();
        goal1 = field.getGoal1()
        goal2 = field.getGoal2()

    for i in xrange(0, balls):
        balls.append(Ball(surface=general.surface, redius=6, showing=showing))

    for i in xrange(0, players):
        players.append( Player(general.surface, (20,20), players=i, showing) )

    for i in xrange(0, skulls):
        skulls.append( MonsterBodyComputer( surface=general.surface ) )

    ai_state = ai.State(players[0], players[1], balls[0])
    my_ai = ai.Ai(players[1], goal1, goal2)

    if showing:
        clock = pygame.time.clock()

    count = 0

    while counter<time_length or time_length is None:
        "MAIN LOOP"
        moveCamera(balls[0])
        stoppingX_event = False
        stoppingY_event = False
        new_key = False
        mouse_pos = pygame.mouse.get_pos()
        goal_size = goal1.image.get_size()

    if online:
        ball = balls[0]
        player1 = players[0]
        player2 = players[1]
        terminals0 = Terminals( counter, ball.pos, ball.vel, player1.pos, player1.vel, 1, [0, 0], [0, 0], 1)
        terminals1 = Terminals(counter, ball.pos, ball.vel, [width - player2.pos[0], height - player2.pos[1]], [- player2.vel[1]], 1, [0, 0], [0, 0], 1)

    if showing: clock.tick(120)

    count += 1
    if showing:
    "Background"
        if showing: field.blitBackground(general.surface)
    "Keyboard event"
    input = pygame.event.get()
    for event in input:
        whatkey = keyboard(event)
        if whatkey.isKEYDOWN():
            if whatkey.isESCAPE():
                sys.exit(0)
            elif whatkey.isEQUALS():
                general.global_zoom *= 1.1
            elif whatkey.isMINUS():
                general.global_zoom /= 1.1
            elif whatkey.isLEFT():
                players[0].fireLEFT()
            elif whatkey.isRIGHT():
                players[0].fireRIGHT()
            elif whatkey.isUP():
                players[0].fireUP()
            elif whatkey.isDOWN():
                players[0].fireDOWN()
            elif whatkey.isPERIOD():
                balls[0].getSHOT(players[0])
            elif whatkey.isSLASH():
                balls[0].getSHOT(players[0], 0.46)

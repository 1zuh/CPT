import random
CIV = 0  # constantly increasing variable

# global variables related to player(s) movement/position
pos_y = 395
pos_y_2 = 155
g_speed = 0  # gravity speed
g_speed_2 = 0

# global variables related to obstacle generation
obs_pos_x = []  # obstacle position x
obs_count = 0
random_addition = 0
obs = 0


def setup():
    size(640, 480)
    frameRatetik(60)
    tests()
    test_collision()


def tests():
    assert score(4) == 1, "Should return 1"
    assert score(1020) == 255, "Should return 255"
    print ("unexceptional functions have been tested and deemed acceptable")


def test_collision():
    global obs
    if obs == 40 and pos_y == 365:
        assert collision() == 1, "Should return 1"
    if obs == 500 and pos_y == 375:
        assert collision() == 0, "Should return 0"
    if obs == 104 and pos_y == 395:
        assert collision() == 1, "Should return 1"
    if obs == 500 and pos_y == 395:
        assert collision() == 0, "Should return 0"
    print ("collision() function has been tested and deemed acceptable")


def draw():
    global CIV
    background(255, 255, 255)
    rect(0, 470, 640, 1)
    rect(0, 230, 640, 1)
    player()
    player2()
    score(CIV)
    updateObstacles(score(CIV))
    try:
        if collision() == 1 or collision() == 2:
            fill(0)
            textSize(20)
            text("""Collision detected. Game over.
    Press 'R' once to restart.""", width/4, height/3)
            noLoop()  # without this players can jump out of the obstacle to continue playing
        else:
            CIV += 1
    except:
        print("somehow, an error has occurred. try restarting.")
        noLoop()


def score(value):
    another_synonym_for_score = value/4
    fill(0)
    textSize(13)
    text("score:{}".format(another_synonym_for_score), 10, 10)
    noFill()
    return another_synonym_for_score


def player():
    global pos_y, g_speed
    pos_y += g_speed
    if pos_y <= 394:
        g_speed += 0.5  # gravity
    if pos_y >= 395:
        g_speed = 0
    noFill()
    rect(40, pos_y, 64, 64)  # player model


def player2():
    global pos_y_2, g_speed_2
    pos_y_2 += g_speed_2
    if pos_y_2 <= 154:
        g_speed_2 += 0.5
    if pos_y_2 >= 155:
        g_speed_2 = 0
    rect(40, pos_y_2, 64, 64)


def keyPressed():
    global g_speed, g_speed_2, CIV
    if keyCode == 32:  # keyCode 32 is spacebar
        if pos_y == 395:
            g_speed = -12
    if keyCode == 38:  # keyCode 38 is up arrow
        if pos_y_2 == 155:
            g_speed_2 = -12
    if collision() == 1 or collision() == 2:
        if key == 'r':
            loop()  # noLoop() bricks the game unless this is here
            CIV = 0
            for obs_removal in obs_pos_x:
                obs_pos_x.remove(obs_removal)


def updateObstacles(score):
    global obs_pos_x, obs_count, obs, difficulty
    obs_count += 1
    difficulty = -5
    for i in range(0, 20):
        if score >= i * 250:
            difficulty -= 1
    obs_pos_x = [pos + difficulty for pos in obs_pos_x]
    if obs_count > 50 + random_addition:  # 50 is the minimum distance between obstacles
        addObstacle()
    for obs in obs_pos_x:
        rect(obs, 430, 60, 40)
        rect(obs, 190, 60, 40)


def addObstacle():
    global obs_count, random_addition, difficulty
    obs_count = 0
    distance = 70
    for i in range(0, 20, 4):
        if difficulty >= -5 - i:
            distance -= 5
    random_addition = random.randint(0, distance)
    obs_pos_x.append(640)


def collision():
    global obs_pos_x, pos_y, pos_y_2
    for obs in obs_pos_x:
        if (obs >= 40 and obs <= 104) or (obs + 60 >= 40 and obs + 60 <= 104):
            if pos_y >= 395 - 40 + 10:  # 10 to be a bit more forgiving
                print("Collision detected for Player 1. Game over.")
                return 1
            elif pos_y_2 >= 155 - 40 + 10:
                print ("Collision detected for Player 2. Game over.")
                return 2
            else:
                return 0

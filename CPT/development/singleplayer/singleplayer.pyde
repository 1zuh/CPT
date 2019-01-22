import random
CIV = 0  # constantly increasing variable
# global variables related to player movement
pos_y = 340
g_speed = 0  # gravity speed

# global variables related to random obstacle generation
obs_pos_x = []  # obstacle position x
obs_count = 0
random_addition = 0
obs = 0


def setup():
    size(640, 480)
    frameRate(60)
    #test functions
    tests()
    test_collision()


def tests():
    assert score(4) == 1, "Should return 1"
    assert score(1020) == 255, "Should return 255"
    print ("unexceptional functions have been tested and deemed acceptable")


def test_collision():
    global obs
    if obs == 40 and pos_y == 310:
        assert collision() == 1, "Should return True"
    if obs == 500 and pos_y == 320:
        assert collision() == 0, "Should return False"
    if obs == 104 and pos_y == 340:
        assert collision() == 1, "Should return True"
    if obs == 500 and pos_y == 340:
        assert collision() == 0, "Should return False"
    print ("collision() function has been tested and deemed acceptable")


def draw():
    global CIV
    background('#f5f5f2')
    stroke('#b0b0b0')
    rect(0, 415, 640, 1)
    player()
    score(CIV)
    updateObstacles(score(CIV))
    try:
        if collision() == 1:
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
    fill('#b0b0b0')
    textSize(13)
    text("score:{}".format(another_synonym_for_score), 10, 10)
    noFill()
    return another_synonym_for_score


def player():
    global pos_y, g_speed
    pos_y += g_speed
    if pos_y <= 339:
        g_speed += 0.5  # gravity
    if pos_y >= 340:
        g_speed = 0
    noFill()
    rect(40, pos_y, 64, 64)  # player model


def keyPressed():
    global g_speed, CIV
    if keyCode == 32:  # keyCode 32 is spacebar
        if pos_y == 340:
            g_speed = -12
    if collision() == 1:
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
        # rect(obs_pos_x, 375, 20, 40) # small cactus
        rect(obs, 375, 60, 40)  # small cactus crowd
        # rect(obs_pos_x, 355, 30, 60) # large cactus


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
    global obs_pos_x, pos_y
    for obs in obs_pos_x:
        if (obs >= 40 and obs <= 104) or (obs + 60 >= 40 and obs + 60 <= 104):
            if pos_y >= 340 - 40 + 10:  # 10 to be a bit more forgiving
                print("Collision detected. Game over.")
                return 1
            else:
                return 0

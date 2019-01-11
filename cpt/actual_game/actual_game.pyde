import time
player_y = 340
y_speed = 0
def setup():
    size (640, 480)
    frameRate (60)
    
def draw():
    player()
    rect(0, 415, 640, 1)
    score()
    obstacles()
    collision()
    
def score():
    global synonym_for_score
    synonym_for_score = frameCount/2
    fill (0)
    text("score:{}".format(synonym_for_score), 10, 10)
    noFill()
    
def player():
    global player_y, y_speed
    player_y += y_speed
    if player_y <= 339:
        y_speed += 0.5
    if player_y >= 340:
        y_speed = 0
    background (255, 255, 255)
    rect(40, player_y, 64, 64)
    
def keyPressed():
    global y_speed
    if player_y == 340:
        y_speed = -12
    
def obstacles():
    framecount = frameCount
    global x1, x2, synonym_for_score
    difficulty = -5
    for i in range(1, 20):
        if synonym_for_score >= i * 100:
            difficulty -= 0.25
    x1 = ((framecount % 160) * difficulty) + 600
    rect(x1, 375, 20, 40)
    
def collision():
    global x1, x2, player_y
    if x1 >= 40 and x1 <= 104:
        if player_y >= 310:
            noLoop()
            time.sleep(0.5)
            print("Collision detected. Game over.")

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

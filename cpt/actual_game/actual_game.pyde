
player_y = 340
y_speed = 0
def setup():
    size (640, 480)
    frameRate (60)
    
def draw():
    player()
    ground()
    obstacles()
    score()
    collision()

def ground():
    rect(0, 415, 640, 1)
    
def score():
    fill (0)
    text("score:{}".format(frameCount/2), 10, 10)
    noFill()
    
def player():
    global player_y, y_speed
    player_y += y_speed
    if player_y <= 190:
        y_speed *= -1
    if player_y >= 339:
        y_speed = 7
    if player_y == 340:
        y_speed = 0
    background (255, 255, 255)
    rect(40, player_y, 64, 64)
def keyPressed():
    global y_speed
    y_speed = -12
    
def obstacles():
    framecount = (frameCount * 5) * -1
    global x1
    x1 = framecount + 600
    rect(x1, 385, 20, 30)
def collision():
    global x1, player_y
    if x1 >= 40 and x1 <= 60:
        if player_y >= 340:
            print("Collision detected. Game over.")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

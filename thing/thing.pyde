def setup():
    size (640, 480)
    
def draw():
    title_screen()
    
def title_screen():
    background (255, 255, 255)
    w = 115
    h = 60
    rect(165, 150, 290, 90)
    rect(125, 250, w, h)
    rect(375, 250, w, h)
    fill (0)
    textSize(20)
    text("another generic sidescroller", 180, 200)
    textSize(15)
    text("singleplayer", 140, 280)
    text("multiplayer", 390, 280)
    noFill()
    w = 290
    h = 90

    if mousePressed:
        if mouseX >= 165 and mouseX <= 165 +290 and mouseY >= 150 and mouseY <= 150 + 90:
            print("The mouse is pressed and over the button.")
            background(0)

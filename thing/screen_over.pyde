def setup():
    size(640, 480)
    
def draw():
    gameover_screen()
    
def gameover_screen():
    background(255)
    img = loadImage("game over.jpg")
    image(img, (width - 569)/2, 70)
    fill(0)
    textSize(23)
    text("how unfortunate", 235, 300)

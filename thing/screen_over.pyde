def setup():
    size(640, 480)
    
def draw():
    background(255)
    img = loadImage("game over.jpg")
    img2 = loadImage("how unfortunate.png")
    image(img, (width - 569)/2, 70)
    image(img2, (width - 200)/2, 270)
    '''
    is really small so your choice on whether or not to choose image above or text
    text("how unfortunate", 275, 270)
    '''
    

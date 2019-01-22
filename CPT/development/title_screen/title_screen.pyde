def setup():
    size(640, 480)
    global dinosaur
    dinosaur = loadImage("dinosaur.png")


def draw():
    title_screen()


def title_screen():
    background(255, 255, 255)
    # titlecard
    image(dinosaur, 50, 30, 100, 100)
    fill(0)
    textSize(27)
    text("""another
generic
sidescroller""", 160, 40)
    rect(40, 150, 520, 1)

    # singleplayer
    noFill()
    rect(30, 190, 540, 36)
    fill(0)
    textSize(15)
    text("singleplayer", 60, 211)

    # multiplayer
    noFill()
    rect(30, 250, 540, 36)
    fill(0)
    textSize(15)
    text("multiplayer", 60, 271)

    # lol
    noFill()
    rect(30, 310, 440, 36)
    fill(0)
    textSize(15)
    text("lol", 60, 331)

    # mousepressed:
    if mousePressed:
        if mouseX >= 30 and mouseX <= 30 + 540:
            if mouseY >= 190 and mouseY <= 190 + 36:
                print("The mouse is pressed and over the singleplayer button.")
                background(0, 255, 0)
            if mouseY >= 250 and mouseY <= 250 + 36:
                print("The mouse is pressed and over the multiplayer button.")
                background(255, 0, 0)
            if mouseY >= 310 and mouseY <= 480 + 36:
                print("lol")
                background(0, 0, 255)

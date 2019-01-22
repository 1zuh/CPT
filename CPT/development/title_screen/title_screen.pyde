def setup():
    size(640, 480)
    global dinosaur1, dinosaur2, gallo
    dinosaur1 = loadImage("dinorun0000.png")
    dinosaur2 = loadImage("dinorun0001.png")
    gallo = loadImage("11080017.jpeg")


def draw():
    title_screen()


def title_screen():
    background(255, 255, 255)
    # titlecard
    fill(0)
    textSize(27)
    text("""another
generic
sidescroller""", 160, 40)
    rect(40, 150, 520, 1)
    image(dinosaur1, 50, 30, 96, 112)
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
                noStroke()
                fill(255, 255, 255)
                rect(50, 30, 96, 112)
                stroke(0)
                if frameCount % 6 != 0:
                    image(dinosaur1, 50, 30, 96, 112)
                elif frameCount % 6 == 0:
                    image(dinosaur2, 50, 30, 96, 112)
            elif mouseY >= 250 and mouseY <= 250 + 36:
                print("The mouse is pressed and over the multiplayer button.")
                noStroke()
                fill(255, 255, 255)
                rect(50, 30, 96, 112)
                stroke(0)
                if frameCount % 6 != 0:
                    image(dinosaur2, 50, 30, 96, 112)
                elif frameCount % 6 == 0:
                    image(dinosaur1, 50, 30, 96, 112)
            elif mouseY >= 310 and mouseY <= 480 + 36:
                print("lol")
                image(gallo, 0, 0, 640, 480)

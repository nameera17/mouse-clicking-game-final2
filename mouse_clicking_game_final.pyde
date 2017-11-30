p1_pos_x = 0
p1_pos_y = 0
p2_pos_x = 0
p2_pos_y = 0
ball_size = 60
p1_score = 0
p2_score = 0
winner = None

def setup():
    global p1_pos_x
    global p1_pos_y
    global p2_pos_x
    global p2_pos_y
           
    size(800, 400)
    p1_pos_x = random(0, width/2)
    p1_pos_y = random(0, height)
    
    p2_pos_x = random(width/2, width)
    p2_pos_y = random(0, height)


def draw():
    global p1_pos_x
    global p1_pos_y
    global p1_score
    global p2_score
    global winner
    
    background(0)
    textAlign(LEFT)
    # Player 1 board
    fill(106, 204, 138)
    rect(0, 0, width/2, height)
    
    # Player 1 ball
    noStroke()
    fill(50, 75, 54)
    ellipse(p1_pos_x, p1_pos_y, ball_size, ball_size)
    
    # Player 1 Score
    fill(50, 75, 54)
    textSize(30)
    text("Score: " + str(p1_score), 30, 50)
    
    # Player 2 board 
    fill(50, 75, 54)
    rect(width/2, 0, width, height)
    
    # Player 2 ball
    noStroke()
    fill(137, 206, 138)
    ellipse(p2_pos_x, p2_pos_y, ball_size, ball_size)
    
    # Player 2 Score
    fill(137, 206, 138)
    textSize(30)
    text("Score: " + str(p2_score), width/2 + 30, 50)

    if winner:
        textSize(90)
        textAlign(CENTER)
        fill(255)
        text(winner + " WINS!", width/2, height/2)

def mousePressed():
    global p1_pos_x
    global p1_pos_y
    global p2_pos_x
    global p2_pos_y
    global p1_score
    global p2_score
    global ball_size
    global winner

    
    # P 1
    radius = ball_size / 2.0
    distance_x = abs(mouseX - p1_pos_x)
    distance_y = abs(mouseY - p1_pos_y)
    hypotenuse = sqrt(distance_x ** 2 + distance_y ** 2)
    if hypotenuse <= radius:
        p1_pos_x = random(0, width/2)
        p1_pos_y = random(0, height)
        p1_score += 1
        
    # P 2
    radius = ball_size / 2.0
    distance_x = abs(mouseX - p2_pos_x)
    distance_y = abs(mouseY - p2_pos_y)
    hypotenuse = sqrt(distance_x ** 2 + distance_y ** 2)
    if hypotenuse <= radius:
        p2_pos_x = random(width/2, width)
        p2_pos_y = random(0, height)
        p2_score += 1
    
    if winner == None:
        if p1_score == 10:
            winner = "PLAYER 1"
        elif p2_score == 10:
            winner = "PLAYER 2"
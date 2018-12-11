# The shape of the numbers for the dice
dice = { 1: [[None, None, None], [None, "", None], [None, None, None]],
        2: [["", None, None], [None, None, None], [None, None, ""]],
        3: [["", None, None], [None, "", None], [None, None, ""]],
        4: [["", None, ""], [None, None, None], ["", None, ""]],
        5: [["", None, ""], [None, "", None], ["", None, ""]],
        6: [["", None, ""], ["", None, ""], ["", None, ""]]}

def setup():
    # Variable initialization
    global dice_no, score, count, debug
    dice_no = None
    score = 0
    count = 0
    debug = True
    size(220, 155)

    
def draw():
    global dice_no, score, count
    # Clear the previous draws on the screen
    clear()
    fill(255)
    rect(0, 0, width, height)
    
    basex = 35
    if debug:
        basey = 60
    else:
        basey = 30
        
    # Fill the whole field with color x
    fill(232, 227, 218)
    # Draw a rect, this will be the dice
    rect(basex-30, basey-30, 120, 120, 12, 12, 12, 12)
    if dice_no != None:
        for y in range(len(dice[dice_no])):
            for x in range(len(dice[dice_no][y])):
                if dice[dice_no][y][x] != None:
                    # Draw the eye's of the dice, in the desired color
                    fill(0)
                    ellipse(basex + (x * 30), basey + (y * 30), 20, 20)
    if debug:
        text("score: " + str(score) + " - Count: " + str(count) + " - Dice_No: " + str(dice_no), 0, 20)
    
def mousePressed():
    global dice_no, score, count
    if mouseButton == LEFT: 
        if count % 2 == 0:
            score = 0
            count = 0
        # Get a random value for the dice
        dice_no = int(random(1,7))
        score += dice_no
        count += 1

# The shape of the numbers for the dice
dice = { 1: [[None, None, None], [None, "", None], [None, None, None]],
        2: [["", None, None], [None, None, None], [None, None, ""]],
        3: [["", None, None], [None, "", None], [None, None, ""]],
        4: [["", None, ""], [None, None, None], ["", None, ""]],
        5: [["", None, ""], [None, "", None], ["", None, ""]],
        6: [["", None, ""], ["", None, ""], ["", None, ""]]}

dice_cnt = 2

def setup():
    # Variable initialization
    global dice_no, score, count, debug
    dice_no = []
    score = 0
    count = 0
    debug = True
    size(130 * dice_cnt, 155)

    
def draw():
    global dice_no, score, count
    # Clear the previous draws on the screen
    clear()
    fill(255)
    rect(0, 0, width, height)
    
    print(dice_no)
    
    basex = 35
    if debug:
        basey = 60
    else:
        basey = 30
        
    for i in range(len(dice_no)):
        bx = (basex+i*130)
        # Fill the whole field with color x
        fill(232, 227, 218)
        # Draw a rect, this will be the dice
        rect(bx-30, basey-30, 120, 120, 12, 12, 12, 12)
        if dice_no != []:
            for y in range(len(dice[dice_no[i]])):
                for x in range(len(dice[dice_no[i]][y])):
                    if dice[dice_no[i]][y][x] != None:
                        # Draw the eye's of the dice, in the desired color
                        fill(0)
                        ellipse(bx + (x * 30), basey + (y * 30), 20, 20)
    if debug:
        text("score: " + str(score) + " - Count: " + str(count) + " - Dice_No: " + str(dice_no), 0, 20)
    
def mousePressed():
    global dice_no, score, count
    if mouseButton == LEFT: 
        score = 0
        count = 0
        # Get a random value for the dice
        dice_no = [int(random(1,7)) for x in range(dice_cnt)]
        score = sum(dice_no)

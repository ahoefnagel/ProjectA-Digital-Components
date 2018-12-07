dice = { 1: [[None, None, None], [None, "", None], [None, None, None]],
        2: [["", None, None], [None, None, None], [None, None, ""]],
        3: [["", None, None], [None, "", None], [None, None, ""]],
        4: [["", None, ""], [None, None, None], ["", None, ""]],
        5: [["", None, ""], [None, "", None], ["", None, ""]],
        6: [["", None, ""], ["", None, ""], ["", None, ""]]}
dice_no = None
score = 0
count = 0
debug = True

def setup():
    size(220, 150)
    
def draw():
    global dice_no, score, count
    clear()
    basex = 30
    if debug:
        basey = 60
    else:
        basey = 30
        
    fill(120, 134, 240)
    rect(basex-30, basey-30, 120, 120)
    if dice_no != None:
        for y in range(len(dice[dice_no])):
            for x in range(len(dice[dice_no][y])):
                if dice[dice_no][y][x] != None:
                    fill(220)
                    ellipse(basex + (x * 30), basey + (y * 30), 20, 20)
    if debug:
        text("score: " + str(score) + " - Count: " + str(count) + " - Dice_No: " + str(dice_no), 0, 20)
    
def mousePressed():
    global dice_no, score, count
    if mouseButton == LEFT: 
        if count % 2 == 0:
            score = 0
            count = 0
        dice_no = int(random(1,7))
        score += dice_no
        count += 1

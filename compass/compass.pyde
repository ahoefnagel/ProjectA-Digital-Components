'''
    Created By: Albert Hoefnagel
    Copyright - 2018
'''
deg = 0
speed = 0
is_slowing = False
rotation_speed = 0
rotation = 0
nesw = [{ "min": 45, "max": 135, "location": "East"}, { "min": 135, "max": 225, "location": "South"}, 
           { "min": 225, "max": 315, "location": "West"}, { "min": 315, "max": 45, "location": "North"}]
# Images
compass = None
arrow = None

def setup():
    global compass, arrow
    size(840, 620, P3D)
    compass = loadImage("windroos.jpg")
    arrow = loadImage("arrow2.png")

def draw():
    global compass, arrow, rotation_speed, rotate_counter, is_slowing, rotation, nesw
    background(255)
    fill(0)
    
    print(rotation_speed)
    
    if is_slowing:
        rotation_speed -= 0.03
    else:
        rotation_speed += deg

    if rotation_speed >= 20:
        is_slowing = True
        
    if rotation_speed < 0:
        rotation_speed = 0
        rot = (rotation - 90) % 360
        textSize(32)
        for comp in nesw:
            if rot > comp['min'] and rot < comp['max']:
                print('The location is: ', comp['location'])
                text('The location is: ' + comp['location'], width/4, 32)
                break
            elif (comp['location'] == 'North' and rot > comp['min']) or (comp['location'] == 'North' and rot < comp['max']):
                print()
                text('The location is: ' + comp['location'], width/4, 32)
                break

    rotation += rotation_speed
    pushMatrix()
    image(compass, width/2 - compass.width/2, height/2 - compass.height/2)
    translate(width/2, height/2)
    rotateZ(radians(rotation))
    image(arrow, -arrow.width/2, -arrow.height/2)
    popMatrix()

    rect(0, 0, 80, 20)
    fill(255)
    text('SPIN!', 30, 15)
    
def mousePressed():
    global deg, is_slowing, rotation
    if mouseButton == LEFT and mouseX > 0 and mouseX < 80 and mouseY > 0 and mouseY < 20:
        is_slowing = False
        rotation = 0
        rand = int(random(1, 4))
        rand2 = int(random(1, 90))
        rand_usage = rand * 90 + rand2
        print(rand_usage)
        deg = (rand_usage / 1000.0)

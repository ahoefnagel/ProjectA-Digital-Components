deg = 0
speed = 0
is_slowing = False
rotation_speed = 0
rotation = 0
# The four locations that the wheel can point at, with their degree
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
    # Check if the arrow is slowing down, if so, decrease the rotation 
    if is_slowing:
        rotation_speed -= 0.05
    else:
        rotation_speed += deg

    if rotation_speed >= 20:
        is_slowing = True
        
    if rotation_speed < 0:
        rotation_speed = 0
        rot = (rotation - 90) % 360
        textSize(32)
        # Check at which side the compass has landed and display it on to the screen
        for comp in nesw:
            if rot > comp['min'] and rot < comp['max']:
                text('The location is: ' + comp['location'], width/2, 24)
                break
            elif (comp['location'] == 'North' and rot > comp['min']) or (comp['location'] == 'North' and rot < comp['max']):
                text('The location is: ' + comp['location'], width/2, 24)
                break

    rotation += rotation_speed
    # Push, pop keep transforms seperated from the rest of the draw function
    pushMatrix()
    # Draw the arrow and the compass
    image(compass, width/2 - compass.width/2, height/2 - compass.height/2)
    translate(width/2, height/2)
    rotateZ(radians(rotation))
    image(arrow, -arrow.width/2, -arrow.height/2)
    popMatrix()
    
    # Draw the 'SPIN!' button
    pushMatrix()
    rect(0, 0, 80, 20)
    textAlign(CENTER, CENTER)
    fill(255)
    strokeWeight(4)
    textSize(16)
    text('SPIN!', 0, 0, 80, 20)
    popMatrix()
    
# Check if the mouse is pressed
def mousePressed():
    global deg, is_slowing, rotation
    if mouseButton == LEFT and mouseX > 0 and mouseX < 80 and mouseY > 0 and mouseY < 20:
        is_slowing = False
        rotation = 0
        rand = int(random(1, 4))
        rand2 = int(random(1, 90))
        rand_usage = rand * 90 + rand2
        # Set the degree at which the arrow should point, and devide it through 1000
        deg = (rand_usage / 1000.0)

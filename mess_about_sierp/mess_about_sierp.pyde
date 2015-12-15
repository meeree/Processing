def setup():
    size(900, 900)
    stroke(255)
    
total = 1
def draw():
    global total
    background(0)
    mouse = [float(mouseX-width/2), -float(mouseY-height/2)]
    translate(width/2, height/2)
    scale(1, -1)
    if mouse[0] == 0.0:
        angle = PI/2
    else:
        angle = atan(mouse[1]/mouse[0])
    if mouse[0] < 0:
        angle += PI
    manager([0, 0], angle, total, 10)
    if total < 5:
        total += 1

        
def manager(point, angle, total, push=20, count=0):
    if count < total:
        for changer in [0, PI/2, PI]:
            distance = [point[0] + push*cos(angle+changer), point[1] + push*sin(angle+changer)]
            line(point[0], point[1], distance[0], distance[1])
            manager([point[0] + distance[0], point[1] + distance[1]], angle, total, push, count+1)

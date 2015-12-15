def setup():
    size(1100, 900)
    fill(255)
    stroke(255)
    strokeWeight(0.25)
    background(5)
    
count = 0
def draw():
    global points, count
    if len(points) > 1:
        generate(points)
    points.append([random(10, width-10), random(10, height-10), 1])
    stroke(len(points) % 256, 0, 0)
    count += 1
    
points = []

def weight(point, weight):
    return [p*weight for p in point]

def bezier(points, t):
    final_points = []
    if len(points) == 1:
        final_point = points[0]
        return weight(final_point, 1.0/(final_point[-1]))
                  
    for p in range(len(points)-1):
        new_point = []
        for cood in range(len(points[p])):
            new_point.append((1-t)*points[p][cood] + t*points[p+1][cood])
        final_points.append(new_point)
    
    return bezier(final_points, t)

def generate(points):
    t = 0.0
    pinit = bezier(points, t)
    while t < 1.0:
        t += 0.005
        pnew = bezier(points, t)
        line(pinit[0], pinit[1], pnew[0], pnew[1])
        pinit = pnew
    
def mousePressed():
    global points
    if mouseButton == RIGHT:
        pos = -1
        for p in points:
            pos += 1
            if ((mouseX-p[0])/(p[-1]*5))**2 + ((mouseY-p[1])/(p[-1]*5))**2 <= 1:
                points[pos] = weight(p[:-1], (p[-1]+2)/p[-1])
                points[pos].append(p[-1]+2)
    if mouseButton == LEFT:
        ellipse(mouseX, mouseY, 5, 5)
        points.append([mouseX, mouseY, 1])  

def keyPressed():
    global points
    if key == ENTER:
        generate(points)
    if key == BACKSPACE:
        points = []
    if key == TAB:
        saveFrame('bezier-##.png')

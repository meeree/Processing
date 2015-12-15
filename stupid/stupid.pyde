def setup():
    size(600, 600)
    frameRate(1000)
    
def interp(point1, point2):
    return (point2[1]-point1[1])/(point2[0]-point1[0])

def bezier(points, t):
    final_points = []
    
    if len(points) == 0:
        return
       
    for p in range(len(points)-1):
        new_point = []
        for cood in range(len(points[p])):
            new_point.append((1-t)*points[p][cood] + t*points[p+1][cood])
        final_points.append(new_point)
    
    strokeWeight(len(points))
    for p in range(len(points)-1):
        line(points[p][0], points[p][1], points[p+1][0], points[p+1][1])
            
    return bezier(final_points, t)


points = []
k = 10

def draw():
    global points, k
    translate(width/2, height/2)
    scale(1, -1)
    background(255)
    
    for p in points:
        ellipse(p[0], p[1], 5, 5)
    
    t = 0
    total = []
    
    while t <= 1.0:
        bezier(points, t) 
        
        t += 0.1
    x = mouseX-width/2
    y = height/2-mouseY
    points = [[-x, y], [-x, -y], [x, -y], [x, y]]
    
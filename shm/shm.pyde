def setup():
    size(600, 600)
    noFill()

A = 100.0
t = 0.0
dt = 0.1
k = 2.0
m = 10.0
u = 1

def draw():
    global A, t, dt, k, m, u
    
    background(255)
    translate(width/2, height/2)
    scale(1, -1)

    w = sqrt(k/m)
           
    theta = w*t
              
    x = A*cos(theta)
    vx = -w*A*sin(theta)
    ax = - w**2*A*cos(theta)    
    
    
    rect(x, 0, -20, 20)
    
    t += dt
    
    
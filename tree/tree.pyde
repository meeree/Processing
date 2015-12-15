def setup():
    size(1400, 700)
   
def tree(trunk, angle, trunkscalar, end_):
    global a
    if trunk < end_:
        return
    line(0, 0, 0, trunk)
    translate(0, trunk)
    pushMatrix()
#     rotate(angle)
#     tree(trunk*trunkscalar, angle, trunkscalar, end_)
    popMatrix()
    rotate(-angle)
    tree(trunk*trunkscalar, angle, trunkscalar, end_)
    
def draw():
    global a
    stroke(0)
    background(255)
    translate(width/2, height)
    scale(1, -1)
    tree(100.0*mouseY/height, 2.0*mouseX/width, .9*mouseY/height, 10)


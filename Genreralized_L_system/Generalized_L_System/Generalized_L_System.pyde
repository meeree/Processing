def setup():
    size(900, 700)
    stroke(255)
    background(0)
    strokeWeight(0.25)
    frameRate(1)
        
class fractalMaker():
    def __init__(self, file, name):
        modifiers = {}
        fl = open(file)
        for line_ in fl:
            if name in line_:
                colon = line_.find(':')
                period = line_.find('.')
                modifiers[line_[period+1:colon]] = line_[colon+2:-1]
        self.constants = list(modifiers['constants'])
        counter = -1
        for i in self.constants:
            counter += 1
            if i == ',':
                self.constants.pop(counter)
        self.angle = eval(modifiers['angle'])
        self.variables = list(modifiers['variables'])
        counter = -1
        for i in self.variables:
            counter += 1 
            if i == ',':
                self.variables.pop(counter)
        self.axiom = list(modifiers['start'])
        counter = -1
        self.rules = {}
        endpoint = 0
        print(modifiers)
        for i in list(modifiers['rules']):
            counter += 1
            if i == '>':
                arrow = counter
            if i == ',' or i == '.':
                self.rules[modifiers['rules'][endpoint:arrow-1]] = modifiers['rules'][arrow+1:counter]
                endpoint = counter+1
        for i in self.constants:
            self.rules[i] = i
        self.order = int(modifiers['order'])
        #Defined parameters are constants, beginning, rules, variables, and angle
        self.pos = 0
        self.Cangle = 0

    def generate(self):
        ls_ = []
        for i in self.axiom:
            for x in self.rules:
                if i == x:
                    for k in self.rules[x]:
                        ls_.append(k)
        return ls_
    
    def fractal(self, order, size_=10):
        for i in self.axiom:
            for x in self.variables:
                if i == x:
                    line(0, 0, size_, 0)
                    self.pos = self.pos + size_/cos(self.Cangle)
                    translate(size_, 0)
            if i == '+':
                rotate(self.angle)
                self.Cangle = self.Cangle + self.angle
            if i == '-':
                self.Cangle = self.Cangle - self.angle
                rotate(-self.angle)
        print(self.order, order)
        if self.order >= order:
            self.axiom = self.generate()

Runner = fractalMaker('/home/jhazelden/runner', 'KochKoc')

order = 0
counter = 0

def draw():
    global order, counter
    counter += 1
    if counter % 3 == 0:
        stroke(255, 0, 0)
    elif counter % 3 == 1:
        stroke(0, 255, 0)
    elif counter % 3 == 2:
        stroke(0, 0, 255)
    translate(width/2, height/2)
    scale(0.1, -0.1)
    Runner.fractal(order)
    order += 1


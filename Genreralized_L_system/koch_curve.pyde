def setup():
    size(800, 700)
    strokeWeight(0.25)
    frameRate(1)

class fractalMaker():
    def __init__(self, file):
        modifiers = {}
        fl = open(file)
        for line_ in fl:
            colon = line_.find(':')
            modifiers[line_[:colon]] = line_[colon+2:-1]
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
        for i in list(modifiers['rules']):
            counter += 1
            if i == '>':
                arrow = counter
            if i == ',' or i == '.':
                self.rules[modifiers['rules'][endpoint:arrow-1]] = modifiers['rules'][arrow+1:counter]
                endpoint = counter+1
        for i in self.constants:
            self.rules[i] = i
        #Defined parameters are constants, beginning, rules, variables, and angle

    def generate(self):
        ls_ = []
        for i in self.axiom:
            for x in self.rules:
                if i == x:
                    for k in self.rules[x]:
                        ls_.append(k)
        return ls_
    
    def fractal(self, size_=10):
        print(self.axiom)
        for i in self.axiom:
            for x in self.variables:
                if i == x:
                    line(0, 0, size_, 0)
                    translate(size_, 0)
            if i == '+':
                rotate(self.angle)
            if i == '-':
                rotate(-self.angle)
        self.axiom = self.generate()

koch = fractalMaker('/home/jhazelden/runner')

def draw():
    translate(0, height)
    scale(0.1, -0.1)
    koch.fractal()

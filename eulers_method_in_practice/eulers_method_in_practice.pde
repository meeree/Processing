float scaleBy = 1;
boolean parametersChanged = true;
float velocity = 840;
float mass = 2300;
float angle = PI/9;

void setAngle(float angle_in_degrees_) {
  parametersChanged = true;
  angle = angle_in_degrees_*PI/180;
}

void setMass(float mass_) {
  parametersChanged = true;
  mass = mass_;
}

void setVelocity(float velocity_) {
  parametersChanged = true;
  velocity = velocity_;
}

interface JavaScript {
  void showValues(float mass);
}

void bindJavascript(JavaScript js) {
  javascript = js;
}

JavaScript javascript;


void setup() {
  size(640, 480);
}

void draw() {
  if (javascript!=null && parametersChanged) {
    background(255);
    javascript.showValues(mass);
    translate(0, 480);
    scale(scaleBy, -scaleBy);
    Approximate running = new Approximate(.01, 0, 0, 0, 100) ;
    running.run();
    parametersChanged = false;
  }
}


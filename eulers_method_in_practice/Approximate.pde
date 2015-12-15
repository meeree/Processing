class Approximate {
  float dt, x, y, t, limit, initial;

  Approximate(float dt_, float x_init, float y_init, float t_init, float t_final) {
    dt = dt_;
    x = x_init;
    y = y_init;
    t = t_init;
    limit = t_final;
    initial = t_init;
  }

  void run() {
    float constant = 0.01;
    float fg = -9.81*mass;
    float vx = cos(angle)*velocity;
    float vy = sin(angle)*velocity;
    noFill();
    beginShape();
    stroke(0);
    while (t < limit) {
     vertex(x/75, y/75);
      float fa = constant*velocity*velocity;
      float fx = -fa*vx  /velocity;
      float fy = (-fa*vy/velocity)+fg;
      float ax = fx/mass;
      float ay = fy/mass;
      vx = vx + dt*ax;
      vy = vy + dt*ay;
      t = t + dt;
      x = x + dt*vx;
      y = y + dt*vy;
      velocity = sqrt(vx*vx + vy*vy);
    }
    endShape();
  }
}



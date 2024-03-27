#include <ServoSmooth.h>

// переменные для сервоприводов первого манипулятора
ServoSmooth servo1;
ServoSmooth servo2;
ServoSmooth servo3;
ServoSmooth servo4;
ServoSmooth servo5;
ServoSmooth servo6;

int s1_angle = 0;
int s2_angle = 0;
int s3_angle = 0;
int s4_angle = 0;
int s5_angle = 0;
int s6_angle = 0;

int mass[50] = {};

String serial_input;

void setup() {
  // инициализация последовательнго порта для связи с Raspberry Pi
  Serial.begin(9600);

  // назначение пинов платы для сервоприводов первого манипулятора 
  servo1.attach(2, 500, 2400, 87); //основание
  servo1.smoothStart();
  servo1.setSpeed(20);
  servo1.setAccel(0.08);

  //поворачиваются против часовой от нуля градусов, по часовой к 180 (этикетка на меня)
  servo2.attach(3, 500, 2400, 98); //1 плечо (5 - опущен параллельно, 90 - вртикально)
  servo2.smoothStart();
  servo2.setSpeed(50);
  servo2.setAccel(0.08);

  servo3.attach(4, 500, 2400, 175); //2 плечо (175 - прижат, уменьшение)
  servo3.smoothStart();
  servo3.setSpeed(50);
  servo3.setAccel(0.2);

  servo4.attach(5, 500, 2400, 178); //3 плечо (178 - прижат, уменьшение)
  servo4.smoothStart();
  servo4.setSpeed(60);
  servo4.setAccel(0.1);

  servo5.attach(6, 500, 2400, 90); //захват (90 - закрыт полностью, 20 - открыт, уменьшение - открытие)
  servo5.smoothStart();
  servo5.setSpeed(40);
  servo5.setAccel(0.08);
}

void loop() {
  if (Serial.available() > 0) {
    serial_input = Serial.readStringUntil('\n');
  }

  //serial_input = "home_position";
  //serial_input = "open_claw";
  //serial_input = "close_claw";
  //serial_input = "position_down_right";
  //serial_input = "position_down_left";
  //serial_input = "position_top_right";
  //serial_input = "position_top_left";

  if(serial_input == "home_position") {
    home_position();
  }

  if(serial_input == "open_claw") {
    open_claw();
  }

  if(serial_input == "close_claw") {
    close_claw();
  }

  if(serial_input == "position_down_right") {
    position_down_right();
  }

  if(serial_input == "position_top_right") {
    position_top_right();
  }

  if(serial_input == "position_down_left") {
    position_down_left();
  }

  if(serial_input == "position_top_left") {
    position_top_left();
  }
  

}


void home_position() {
  servo1.tick();
  servo1.setTargetDeg(87);

  servo2.tick();
  servo2.setTargetDeg(98);
  //servo2.write(98);

  servo3.tick();
  servo3.setTargetDeg(175);

  servo4.tick();
  servo4.setTargetDeg(178);
}


void open_claw() {
  servo5.tick();
  servo5.setTargetDeg(20);
}


void close_claw() {
  servo5.tick();
  servo5.setTargetDeg(64);
}


void position_down_right() {
  servo1.tick();
  servo1.setTargetDeg(55);

  servo2.tick();
  servo2.setTargetDeg(32);
  //servo2.write(40);

  servo3.tick();
  servo3.setTargetDeg(120);

  servo4.tick();
  servo4.setTargetDeg(150);
}


void position_down_left() {
  servo1.tick();
  servo1.setTargetDeg(87);

  servo2.tick();
  servo2.setTargetDeg(30);
  //servo2.write(40);

  servo3.tick();
  servo3.setTargetDeg(140);

  servo4.tick();
  servo4.setTargetDeg(165);
}


void position_top_right() {
  servo1.tick();
  servo1.setTargetDeg(68);

  servo2.tick();
  servo2.setTargetDeg(33);
  //servo2.write(39);

  servo3.tick();
  servo3.setTargetDeg(60);

  servo4.tick();
  servo4.setTargetDeg(95);
}


void position_top_left() {
  servo1.tick();
  servo1.setTargetDeg(87);
  
  servo2.tick();
  servo2.setTargetDeg(33);
  //servo2.write(39);

  servo3.tick();
  servo3.setTargetDeg(60);

  servo4.tick();
  servo4.setTargetDeg(95);
}




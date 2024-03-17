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
  servo1.attach(2, 500, 2400, 70); //основание
  servo1.smoothStart();
  servo1.setSpeed(40);
  servo1.setAccel(0.08);
  servo1.setMaxAngle(120);

  //поворачиваются против часовой от нуля градусов, по часовой к 180 (этикетка на меня)
  servo2.attach(3, 500, 2400, 95); //1 плечо
  servo2.smoothStart();
  servo2.setSpeed(40);
  servo2.setAccel(0.08);

  servo3.attach(4, 500, 2400, 170); //2 плечо
  servo3.smoothStart();
  servo3.setSpeed(40);
  servo3.setAccel(0.08);

  servo4.attach(5, 500, 2400, 178); //3 плечо
  servo4.smoothStart();
  servo4.setSpeed(40);
  servo4.setAccel(0.08);

  servo5.attach(6, 500, 2400, 90); //захват
  servo5.smoothStart();
  servo5.setSpeed(40);
  servo5.setAccel(0.08);
}

void loop() {
  if (Serial.available() > 0) {
    serial_input = Serial.readStringUntil('\n');
  }
  
  if(serial_input == "position_1") {
    position_1();
  }

  if(serial_input == "position_2") {
    position_2();
  }
}

void position_1() {
  //servo1.tick();
  //servo1.setTargetDeg(50);
  servo2.tick();
  servo2.setTargetDeg(20);
  servo3.tick();
  servo3.setTargetDeg(85);
  servo4.tick();
  servo4.setTargetDeg(120);
  servo5.tick();
  servo5.setTargetDeg(30);
}

void position_2() {
  //servo1.tick();
  //servo1.setTargetDeg(50);
  servo2.tick();
  servo2.setTargetDeg(80);
  servo3.tick();
  servo3.setTargetDeg(150);
  servo4.tick();
  servo4.setTargetDeg(120);
  servo5.tick();
  servo5.setTargetDeg(30);
}

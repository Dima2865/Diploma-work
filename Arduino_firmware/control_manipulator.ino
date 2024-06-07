#include <ServoSmooth.h>

// Переменные для сервоприводов манипулятора
ServoSmooth servo1;
ServoSmooth servo2;
ServoSmooth servo3;
ServoSmooth servo4;
ServoSmooth servo5;
ServoSmooth servo6;

// Переменная, хранящая данные из последовательного порта
String serial_input;

// Функция для инициализации последовательного порта, 
// установки параметров управления сервоприводами и задания им начального положения
void setup() {
  // Инициализация последовательнго порта
  Serial.begin(9600);

  // Назначение пинов платы для каждого сервопривода манипулятора
  // Установка настроек управления сервоприводами
  // (установка плавного старта, скорости поворота и ускорения)
  servo1.attach(2, 500, 2400, 87); // основание
  servo1.smoothStart();
  servo1.setSpeed(30);
  servo1.setAccel(0.1);

  //поворачиваются против часовой от нуля градусов, по часовой к 180 (этикетка на меня)
  // 1 плечо (5 - опущен параллельно, 90 - вертикально)
  servo2.attach(3, 500, 2400, 98);
  servo2.smoothStart();
  servo2.setSpeed(50);
  servo2.setAccel(0.1);

  // 2 плечо (175 - прижат, уменьшение)
  servo3.attach(4, 500, 2400, 175);
  servo3.smoothStart();
  servo3.setSpeed(60);
  servo3.setAccel(0.2);

  // 3 плечо (178 - прижат, уменьшение)
  servo4.attach(5, 500, 2400, 178);
  servo4.smoothStart();
  servo4.setSpeed(35);
  servo4.setAccel(0.3);

  // захват (90 - закрыт полностью, 20 - открыт, уменьшение - открытие)
  servo5.attach(6, 500, 2400, 20);
  servo5.smoothStart();
  servo5.setSpeed(80);
  servo5.setAccel(0.2);
}

// Основной loop цикл
void loop() {
  // Если чтение из последовательного порта возможно, то считываем данные
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
  //serial_input = "position_end2";
  //serial_input = "position_end_2_mid";
  //serial_input = "position_end_3_top";

  // Если поступила команда home_position, то запускается одноименная функция
  if(serial_input == "home_position") {
    home_position();
  }

  // Если поступила команда open_claw, то запускается одноименная функция
  if(serial_input == "open_claw") {
    open_claw();
  }

  // Если поступила команда close_claw, то запускается одноименная функция
  if(serial_input == "close_claw") {
    close_claw();
  }

  // Если поступила команда position_down_right, то запускается одноименная функция
  if(serial_input == "position_down_right") {
    position_down_right();
  }

  // Если поступила команда position_top_right, то запускается одноименная функция
  if(serial_input == "position_top_right") {
    position_top_right();
  }

  // Если поступила команда position_down_left, то запускается одноименная функция
  if(serial_input == "position_down_left") {
    position_down_left();
  }

  // Если поступила команда position_top_left, то запускается одноименная функция
  if(serial_input == "position_top_left") {
    position_top_left();
  }
  
  // Если поступила команда position_end, то запускается одноименная функция
  if(serial_input == "position_end") {
    position_end();
  }
  
  // Если поступила команда position_end1, то запускается одноименная функция
  if(serial_input == "position_end1") {
    position_end1();
  }
  
  // Если поступила команда position_end2, то запускается одноименная функция
  if(serial_input == "position_end2") {
    position_end2();
  }
  
  // Если поступила команда position_end3, то запускается одноименная функция
  if(serial_input == "position_end3") {
    position_end3();
  }

  // Если поступила команда position_end_2_mid, то запускается одноименная функция
  if(serial_input == "position_end_2_mid") {
    position_end_2_mid();
  }

  // Если поступила команда position_end_3_top, то запускается одноименная функция
  if(serial_input == "position_end_3_top") {
    position_end_3_top();
  }

  // Если поступила команда up, то запускается одноименная функция
  if(serial_input == "up") {
    up();
  }
}


// Функция для движения в "домашнюю" позицию
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


// Функция для подъема манипулятора
void up() {
  servo2.tick();
  servo2.setTargetDeg(98);
  //servo2.write(98);

  servo3.tick();
  servo3.setTargetDeg(175);

  servo4.tick();
  servo4.setTargetDeg(178);
}


// Функция для движения в зону выгрузки для алгоритма 1 (или нижнее положение для выгрузки объекта для алгоритма 3)
void position_end() {
  servo1.tick();
  servo1.setTargetDeg(150);

  servo2.tick();
  servo2.setTargetDeg(33);
  //servo2.write(40);

  servo3.tick();
  servo3.setTargetDeg(110);

  servo4.tick();
  servo4.setTargetDeg(140);
}


// Функция для движения в среднее положение для выгрузки объекта (для алгоритма 3)
void position_end_2_mid() {
  servo1.tick();
  servo1.setTargetDeg(150);

  servo2.tick();
  servo2.setTargetDeg(63);
  //servo2.write(40);

  servo3.tick();
  servo3.setTargetDeg(128);

  servo4.tick();
  servo4.setTargetDeg(132);
}


// Функция для движения в верхнее положение для выгрузки объекта (для алгоритма 3)
void position_end_3_top() {
  servo1.tick();
  servo1.setTargetDeg(150);

  servo2.tick();
  servo2.setTargetDeg(90);
  //servo2.write(40);

  servo3.tick();
  servo3.setTargetDeg(135);

  servo4.tick();
  servo4.setTargetDeg(115);
}


// Функция для движения в первое положение для выгрузки объекта (для алгоритма 2)
void position_end1() {
  servo1.tick();
  servo1.setTargetDeg(126);

  servo2.tick();
  servo2.setTargetDeg(37);
  //servo2.write(40);

  servo3.tick();
  servo3.setTargetDeg(90);

  servo4.tick();
  servo4.setTargetDeg(120);
}


// Функция для движения во второе положение для выгрузки объекта (для алгоритма 2)
void position_end2() {
  servo1.tick();
  servo1.setTargetDeg(145);

  servo2.tick();
  servo2.setTargetDeg(37);
  //servo2.write(40);

  servo3.tick();
  servo3.setTargetDeg(100);

  servo4.tick();
  servo4.setTargetDeg(130);
}


// Функция для движения в третье положение для выгрузки объекта (для алгоритма 2)
void position_end3() {
  servo1.tick();
  servo1.setTargetDeg(165);

  servo2.tick();
  servo2.setTargetDeg(37);
  //servo2.write(40);

  servo3.tick();
  servo3.setTargetDeg(100);

  servo4.tick();
  servo4.setTargetDeg(130);
}


// Функция открытия захвата
void open_claw() {
  servo5.tick();
  servo5.setTargetDeg(20);
}


// Функция закрытия захвата
void close_claw() {
  servo5.tick();
  servo5.setTargetDeg(70);
}


// Функция для движения в зеленую зону для захвата объекта
void position_down_right() {
  servo1.tick();
  servo1.setTargetDeg(77);

  servo2.tick();
  servo2.setTargetDeg(32);
  //servo2.write(40);

  servo3.tick();
  servo3.setTargetDeg(135);

  servo4.tick();
  servo4.setTargetDeg(160);
}


// Функция для движения в желтую зону для захвата объекта
void position_down_left() {
  servo1.tick();
  servo1.setTargetDeg(112);

  servo2.tick();
  servo2.setTargetDeg(30);
  //servo2.write(40);

  servo3.tick();
  servo3.setTargetDeg(130);

  servo4.tick();
  servo4.setTargetDeg(160);
}


// Функция для движения в синюю зону для захвата объекта
void position_top_right() {
  servo1.tick();
  servo1.setTargetDeg(80);

  servo2.tick();
  servo2.setTargetDeg(38);
  //servo2.write(39);

  servo3.tick();
  servo3.setTargetDeg(70);

  servo4.tick();
  servo4.setTargetDeg(100);
}


// Функция для движения в красную зону для захвата объекта
void position_top_left() {
  servo1.tick();
  servo1.setTargetDeg(103);
  
  servo2.tick();
  servo2.setTargetDeg(35);
  //servo2.write(39);

  servo3.tick();
  servo3.setTargetDeg(60);

  servo4.tick();
  servo4.setTargetDeg(95);
}

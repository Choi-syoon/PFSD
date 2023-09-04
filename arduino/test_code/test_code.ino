#include <Servo.h>

Servo servo1;

int Dir1Pin_A = 3;      // 제어신호 1핀
int Dir2Pin_A = 4;      // 제어신호 2핀
int SpeedPin_A = 8;    // PWM제어를 위한 핀
int pwm_speed = 0;

void setup() 
{ 
  digitalWrite(Dir1Pin_A, LOW);          //모터가 역방향으로 회전 
  digitalWrite(Dir2Pin_A, HIGH);
  pinMode(pwm_speed, OUTPUT);
  Serial.begin(9600);
  while (! Serial);
  Serial.println("Speed 0 to 255");
} 
 
 
void loop() 
{ 
  if (Serial.available())
  {
    int speed = Serial.parseInt();
    if (speed >= 0 && speed <= 255)
    {
      analogWrite(SpeedPin_A, speed);
      delay(10000);
    }
  }
} 

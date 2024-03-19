// #include <Streaming.h>


String pressedButtons = "";
// int buttonState = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(2, INPUT_PULLUP);
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(2) != LOW){
    pressedButtons += "w";
    // Serial.println("W");
    // delay(100);
  }
  if (digitalRead(3) != LOW){
    pressedButtons += "s";
  }
  Serial.println(pressedButtons);
  pressedButtons = "";
  // delay(100);
}

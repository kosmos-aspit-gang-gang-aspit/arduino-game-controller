daString pressedButtons = "";
String lastPressedButtons = "";
void setup() {
  pinMode(2, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(2) != LOW){
    pressedButtons += "w";
  }
  if (digitalRead(3) != LOW){
    pressedButtons += "s";
  }
  if (digitalRead(4) != LOW){
    pressedButtons += "d";
  }
  if (digitalRead(5) != LOW){
    pressedButtons += "a";
  }
  Serial.println(pressedButtons);
  lastPressedButtons = pressedButtons;
  pressedButtons = "";
}

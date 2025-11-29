#include "Notes.h"
#include "sounds01.h"
#include "durations01.h"

int buzzer = 8;

void setup() {}
void loop() {
  for (int i = 0; i < sizeof(melody)/sizeof(int); i++) {
    int duration = 2000 / noteDurations[i];
    tone(buzzer, melody[i], duration);
    delay(duration * 1.1);
  }

  delay(2000);
}

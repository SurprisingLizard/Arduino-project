/*  
  此為arduino播放音樂程式
  引用 Notes.h, sounds 及 durations 檔案
  以迴圈讀取音高及音長 使用內建函式 tone() 播放
*/
#include "Notes.h"
#include "sounds01.h"

int buzzer = 8; // 接腳
int durations = 120; // 節拍數

void setup() {}
void loop() {
  for (int i = 0; i < sizeof(melody)/sizeof(int); i++) {
    int duration = 240000 / durations / noteDurations[i];
    tone(buzzer, melody[i], duration);
    delay(duration * 1.1);
  }

  delay(5000);
}

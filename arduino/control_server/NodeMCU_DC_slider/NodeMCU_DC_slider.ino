#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

// WiFi 정보
const char* ssid = "TEST_SSID";
const char* password = "test1234";

ESP8266WebServer server(80); // 서버 포트 80으로 설정

void setup() {
  Serial.begin(115200);
  delay(10);

  digitalWrite(D1, HIGH);
  digitalWrite(D2, LOW);
  pinMode(D7, OUTPUT); // D1핀을 출력으로 설정

  // WiFi 연결
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");  
 
   // HTTP 요청 처리
   server.on("/", handleRoot);

   server.begin();
   Serial.println("HTTP server started");
}

void loop() {
   server.handleClient();
}

void handleRoot() {
 String html = "<html>\
<head>\
<script>\
window.onload = function(){\
var slider = document.getElementById('motorSpeed');\
slider.oninput = function(){\
var request = new XMLHttpRequest();\
request.open('GET', 'setSpeed?speed=' + this.value, true);\
request.send();\
}\
}\
</script>\
</head>\
<body>\
<h2>DC Motor Speed Control</h2>\
<p>Slide to control the speed of the motor:</p>\
<input type='range' min='0' max='1023' id='motorSpeed'>\
</body></html>";
 
server.send(200, "text/html", html);

if (server.hasArg("speed")) {
String speedStr=server.arg("speed");
int speed=speedStr.toInt();
analogWrite(D1,speed); 
}
}

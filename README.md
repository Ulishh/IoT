# TC1004B - Implementacion del internet de las cosas.

En este repositorio se encuentra la solución del reto para la matera de implementación de internet de las cosas (TC1004B).
El reto consiste en el prototipado de un alcoholimetro digital con el fin la creación de transpariencia en el protocolo 
de multado en vias públicas.

Los integrantes del equipo son:
Eleazar Olivas Gaspar | A01731405@tec.mx
Ulises Hernadez Hernadez | A01735823@tec.mx

Profesores de la materia:
Emmanuel Torres Rios | etorresr@tec.mx
Alba Adriana Romero Garcia | aromerog@tec.mx

Requerimientos de hardware:
 - Esp32        Wroom driver de Wi-fi.
 - DHT11        sensor de humedad y temperatura.
 - Mq135        Sensor de calidad de aire.
 - Mq3          sensor de alcohol.
 - ARD365       sensor de nivel de agua.
 - INND-TS53RCB display de 7 segmentos.
 - Resistencia  365 ohm
 - Jumpers
 - Protoboard 

Requerimientos de software:
 - Arduino IDE
 - DHT.h                    libreria adafruit 
 - esp_wpa2.h               libreria Esp32 driver
 - WiFi.h                   libreria para funciones de wi-fi
 - Firebase_ESP_Client.h    libreria para conección base de datos firebase
 - addons/TokenHelper.h     libreria para generacion de token de firebase
 - Arduino.h                libreria para funciones de soporte de arduino IDE
 - addons/RTDBHelper.h      libreria para funciones de comunicación de firebase

🧠 Miniproyecto 2: Machine Vision – Contador de Dedos con Python y Arduino🎯

Desarrollar un sistema de visión por computadora que, al detectar entre 0 y 5 dedos levantados, envíe dicho número a Arduino, donde un circuito electrónico simulará una suma acumulativa o display de conteo.

LINK VIDEO: https://drive.google.com/file/d/1bLqorv6xtMLSosCP_lxt-f1FkTkLg7WU/view?usp=sharing

Descripción del proyecto

Se utilizará Python con MediaPipe para el seguimiento de la mano y conteo de dedos.
Se usará OpenCV para visualizar el video en tiempo real.
Cada vez que el número de dedos cambie, se enviará dicho número al Arduino vía puerto serial (USB).
En el Arduino, se controlará un sumador o display (pueden ser LEDs, display de 7 segmentos o LCD).

Se utilizaron 2 codigos Python:

Controlador:
Este código sirve para controlar 5 LEDs que están conectados a un Arduino. Primero, se indica que el Arduino está conectado en el puerto 'COM4' (ese puerto puede cambiar dependiendo de tu computadora). Luego, se preparan los pines digitales 8, 9, 10, 11 y 12 como salidas para los LEDs. Después, se define una función llamada led(dedosArriba), que recibe una lista que representa los dedos levantados (por ejemplo [1,0,0,0,0] si solo levantas el pulgar). Dependiendo de cuántos dedos estén levantados, el programa enciende cierta cantidad de LEDs: si no levantas ninguno, todos los LEDs se apagan; si levantas un dedo, se enciende el primer LED; si levantas dos dedos, se encienden el primero y el segundo LED, y así sucesivamente hasta que si levantas los cinco dedos, los cinco LEDs se encienden. 

Contador_dedos:
Este código en Python abre la cámara web y utiliza el módulo HandDetector de la librería cvzone para detectar una mano en tiempo real con alta precisión. Cada imagen capturada se voltea horizontalmente para que el movimiento sea más intuitivo para el usuario. Cuando se detecta una mano, el programa analiza cuáles dedos están levantados y genera una lista indicando su estado (1 para dedo levantado, 0 para dedo abajo). Basado en esta detección, el código muestra en pantalla el conteo de dedos levantados usando OpenCV y envía esa información a un módulo externo llamado Controlador, que probablemente actúa sobre hardware como LEDs u otros dispositivos. El proceso se repite continuamente en un bucle hasta que el usuario presiona la tecla "q", momento en el cual el programa cierra la cámara y todas las ventanas de visualización para finalizar correctamente.

Adicional del lado de Arduino se necesita configurar un codigo correspondiente a Firmdata que es el encargado de poder enteder las instrucciones de parte de Python, se configuro el StandardFirmdata.

Saludos cordiales.
Carlos Rolando Caal Arana




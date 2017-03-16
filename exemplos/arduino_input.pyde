"""
arduino_input

Demonstra a leitura dos pinos digitais e analógicos de um Arduino
rodando o firmware StandardFirmata.

Para usar:
* No IDE Arduino, faça o upload do exemplo StandardFirmata
  (Examples > Firmata > StandardFirmata) para o sua placa Arduino.
* Execute este sketch e veja a lista de portas seriais na áre de mensagens.
. Note the index of the port corresponding to your
  Arduino board (the numbering starts at 0).  (Unless your Arduino board
  happens to be at index 0 in the list, the sketch probably won't work.
  Stop it and proceed with the instructions.)
* Modifique the "arduino = Arduino(...)" line below, changing the number
  in Arduino.list()[0] to the number corresponding to the serial port of
  your Arduino board.  Alternatively, you can replace Arduino.list()[0]
  with the name of the serial port, in double quotes, e.g. "COM5" on Windows
  or "/dev/tty.usbmodem621" on Mac.
* Execute este sketch. Os quadrados mostram os valores das entradas digitais
  (Pinos com HIGH preenchidos, os com LOW não). Os círculos mostram os valores
  das entradas analógica (quanto maior o círculo, maior a leitura do pino
  analógico de entrada correspondentr). The pins are laid out as if the Arduino
  were held with the logo upright (i.e. pin 13 is at the upper left). Note
  that the readings from unconnected pins will fluctuate randomly. 
  
Para mais informações: http:#playground.arduino.cc/Interfacing/Processing
"""

add_library('serial')  # substitui import processing.serial.*;
add_library('arduino')  # substitui import cc.arduino.*;

off = color(4, 79, 111)
on = color(84, 145, 158)

def setup():
    global arduino
    size(470, 280)

    # Portas seriais disponíveis
    println(Arduino.list())

    # Modifique a linha abaixo, mudando o "0" para o índice da porta serial
    # correspondente a sua placa Arduino (conforme mostrado na lista
    # gerade pelo cógido acima).
    arduino = Arduino(this, Arduino.list()[0], 57600)

    # Como alternativa, use o nome da porta serial correspondente ao seu
    # Arduino (com apspas-duplas), como na seguinte linha:
    # arduino = Arduino(this, "/dev/tty.usbmodem621", 57600)

    # Ajusta os pinos digitais do Arduino como entradas (inputs).
    for i in range(14):  # for pins 0 to 13
        arduino.pinMode(i, Arduino.INPUT)

def draw():
    background(off)
    stroke(on)

    # Desenha uma caixa com preenchimento para cada pino digital que esteja HIGH (5 volts).
    for i in range(14):  # from 0 to 13
        if arduino.digitalRead(i) == Arduino.HIGH:
            fill(on)
        else:
            fill(off)
        rect(420 - i * 30, 30, 20, 20)

    # Desenha um círculo cujo tamanho corresponde ao valor do input analógico.
    noFill()
    for i in range(6):  # for analog pins from A0 to A5
        ellipse(280 + i * 30, 240, arduino.analogRead(i) / 16,
                arduino.analogRead(i) / 16)

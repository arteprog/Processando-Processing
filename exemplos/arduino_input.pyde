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
* Modify the "arduino = Arduino(...)" line below, changing the number
  in Arduino.list()[0] to the number corresponding to the serial port of
  your Arduino board.  Alternatively, you can replace Arduino.list()[0]
  with the name of the serial port, in double quotes, e.g. "COM5" on Windows
  or "/dev/tty.usbmodem621" on Mac.
* Run this sketch. The squares show the values of the digital inputs (HIGH
  pins are filled, LOW pins are not). The circles show the values of the
  analog inputs (the bigger the circle, the higher the reading on the
  corresponding analog input pin). The pins are laid out as if the Arduino
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

    # Modify this line, by changing the "0" to the index of the serial
    # port corresponding to your Arduino board (as it appears in the list
    # printed by the line above).
    arduino = Arduino(this, Arduino.list()[0], 57600)

    # Alternatively, use the name of the serial port corresponding to your
    # Arduino (in double-quotes), as in the following line.
    # arduino = Arduino(this, "/dev/tty.usbmodem621", 57600)

    # Set the Arduino digital pins as inputs.
    for i in range(14):  # for pins 0 to 13
        arduino.pinMode(i, Arduino.INPUT)

def draw():
    background(off)
    stroke(on)

    # Draw a filled box for each digital pin that's HIGH (5 volts).
    for i in range(14):  # from 0 to 13
        if arduino.digitalRead(i) == Arduino.HIGH:
            fill(on)
        else:
            fill(off)
        rect(420 - i * 30, 30, 20, 20)

    # Draw a circle whose size corresponds to the value of an analog input.
    noFill()
    for i in range(6):  # for analog pins from A0 to A5
        ellipse(280 + i * 30, 240, arduino.analogRead(i) / 16,
                arduino.analogRead(i) / 16)

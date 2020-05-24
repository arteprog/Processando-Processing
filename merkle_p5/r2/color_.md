
#### Nome
### color()

#### Exemplos
<img border="0" height="100" src="media/color_.gif" width="100"/>
```pde
color c1 = color(102, 102, 0); 
fill(c1); 
noStroke(); 
rect(30, 20, 55, 55); 

```

#### Descrição

	
Creates colors for storing in variables of the**color** datatype. The parameters are interpreted as RGB or HSB values depending on the current**colorMode()**. The default mode is RGB values from 0 to 255 and therefore, the function call**color(255, 204, 0)** will return a bright yellow color. The**color()** function packs the information input through its parameters into a 32 bit number in the following order AAAAAAAARRRRRRRRGGGGGGGGBBBBBBBB where R is the red/hue value, G is green/saturation, and B is blue/brightness.

#### Sintaxe
```pde
color(gray)
color(gray, alpha)
color(value1, value2, value3)
color(value1, value2, value3, alpha)
color(hex)

```
Parâmetros
gray
int or float: number specifying value between white and black
alpha
int or float: relative to current color range
value1
int or float: red or hue values relative to the current color range
value2
int or float: green or saturation values relative to the current color range
value3
int or float: blue or brightness values relative to the current color range
hex
int: color value in hexadecimal notation (i.e. #FFCC00 or 0xFFCC00)

#### Retorno

	
color

#### Utilização

	
Web & Applicações

#### Relacionado

[color](color)
[colorMode()](colorMode_)

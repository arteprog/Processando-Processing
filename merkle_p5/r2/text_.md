
#### Nome
### text()

#### Exemplos
<img border="0" height="100" src="media/text_.gif" width="100"/>
```pde
PFont font; 
// The font must be located in the sketch's 
// "data" directory to load successfully 
font = loadFont("FFScala-32.vlw"); 
textFont(font, 32); 
text("word", 15, 30); 
fill(0, 102, 153); 
text("word", 15, 60); 
fill(0, 102, 153, 51); 
text("word", 15, 90);  

```
<img border="0" height="100" src="media/text_X.gif" width="100"/>
```pde
size(100, 100, P3D); 
PFont font; 
font = loadFont("FFScala-32.vlw"); 
textFont(font, 32); 
text("word", 15, 60, -30); 
fill(0, 102, 153); 
text("word", 15, 60); 

```
<img border="0" height="100" src="media/text_3.gif" width="100"/>
```pde
PFont font; 
font = loadFont("FFScala-Bold-12.vlw"); 
textFont(font, 12); 
String s = "The quick brown fox jumped over the lazy dog."; 
text(s, 15, 20, 70, 70); 

```

#### Descrição

	
Draws text to the screen. Displays the information specified in the**data** or**stringdata** parameters on the screen in the position specified by the**x** and**y** parameters and the optional**z** parameter. A font must be set with the**textFont()** function before**text()** may be called. The**width** and**height** parameters define a rectangular area to display within and may only be used with string data. The text displays in relation to the**textAlign()** function, which gives the option to draw to the left, right, and center of the coordinates. Use the**textMode()** function with the**SCREEN** parameter to display text in 2D at the surface of the window. Change the color of the text with the**fill()** function.

#### Sintaxe
```pde
text(data, x, y)
text(data, x, y, z)
text(stringdata, x, y, width, height)
text(stringdata, x, y, width, height, z)

```
Parâmetros
data
String, char, int, or float: the alphanumeric symbols to be displayed
x
int or float: coordenada-x of text
y
int or float: coordenada-y of text
z
int or float: coordenada-z of text
stringdata
String: letters to be displayed
width
int or float: width of text box
height
int or float: height of text box

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado

[textAlign()](textAlign_)
[textMode()](textMode_)
[loadFont() ](loadFont_)
[PFont ](PFont)
[textFont() ](textFont_)

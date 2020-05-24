<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### createFont()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
```pde
PFont myFont; 
 
void setup() { 
  size(200, 200); 
  // Uncomment the following two lines to see the available fonts 
  //String[] fontList = PFont.list(); 
  //println(fontList); 
  myFont = createFont("FFScala", 32); 
  textFont(myFont); 
  text("!@#$%", 10, 50); 
} 
 

```

#### Descrição

	
Dynamically converts a font to the format used by Processing from either a font name that's installed on the computer, or from a .ttf or .otf inside the data folder of the sketch. Use the**PFont.list()** method to first determine the names for the fonts recognized by the computer. If you're going to be sharing the program with other people or posting it on the web, it's important to include a .ttf or .otf version of your font the the data directory of the sketch because other people might not have the font installed on their computer.Use the**PFont.list()** method to first determine the names for the fonts recognized by the computer. The**size** parameter states the font size you want to generate. The**charset** parameter is an array of chars which specifies the characters to generate and the**smooth** parameter specifies if the font should be antialiased or not. Processing displays fonts using the .vlw font format, which uses images for each letter, rather than defining them through vector data.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
createFont(<font color="#996600">name</font>, <font color="#996600">size</font>)
createFont(<font color="#996600">name</font>, <font color="#996600">size</font>, <font color="#996600">charset</font>)
createFont(<font color="#996600">name</font>, <font color="#996600">size</font>, <font color="#996600">smooth</font>)
createFont(<font color="#996600">name</font>, <font color="#996600">size</font>, <font color="#996600">charset</font>, <font color="#996600">smooth</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
name
String: name of the font to load
size
float: point size of the font
charset
char[]: array containing characters to be generated
smooth
boolean: true for an antialiased font, false for aliased
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
PFont
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado

[PFont ](PFont)

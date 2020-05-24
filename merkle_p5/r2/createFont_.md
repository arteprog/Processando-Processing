
#### Nome
### createFont()

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

#### Sintaxe
```pde
createFont(name, size)
createFont(name, size, charset)
createFont(name, size, smooth)
createFont(name, size, charset, smooth)

```
Parâmetros
name
String: name of the font to load
size
float: point size of the font
charset
char[]: array containing characters to be generated
smooth
boolean: true for an antialiased font, false for aliased

#### Retorno

	
PFont

#### Utilização

	
Web & Applicações

#### Relacionado

[PFont ](PFont)

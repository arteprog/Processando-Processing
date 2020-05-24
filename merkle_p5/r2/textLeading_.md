
#### Nome
### textLeading()

#### Exemplos
<img border="0" height="100" src="media/textLeading_.gif" width="100"/>
```pde
PFont font; 
// The font must be located in the sketch's 
// "data" directory to load successfully 
font = loadFont("EurekaMonoCond-Bold-14.vlw"); 
// Text to display. The "\n" is a "new line" character 
String lines = "LIN1\nLIN2\nLIN3"; 
textFont(font, 14); 
textLeading(10); 
text(lines, 5, 25); 
fill(126);  // Set value to gray 
textLeading(20); 
text(lines, 36, 25); 
fill(0);    // Set value to black 
textLeading(30); 
text(lines, 68, 25); 

```

#### Descrição

	
Sets the spacing between lines of text in units of pixels. This setting will be used in all subsequent calls to the **text()** function.

#### Sintaxe
```pde
textLeading(dist)

```
Parâmetros
dist
int or float: the size in pixels for spacing between lines



#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado

[loadFont() ](loadFont_
)
[PFont ](PFont
)
[text()](text_
)
[textFont() ](textFont_
)

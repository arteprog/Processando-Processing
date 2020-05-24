
#### Nome
### PFont

#### Exemplos
<img border="0" height="100" src="media/PFont.gif" width="100"/>
```pde
PFont font; 
// The font must be located in the sketch's 
// "data" directory to load successfully 
font = loadFont("FFScala-32.vlw"); 
textFont(font, 32); 
text("word", 15, 50); 

```

#### Descrição

	
PFont is the font class for Processing. The**loadFont()** function constructs a new font and**textFont()** makes a font active. The**list()** method creates a list of the fonts installed on the computer, which is useful information to use with the<c>createFont()</c> function for dynamically converting fonts into a format to use with Processing.
Métodos
[list()](PFont_list_)
Gets a list of the fonts installed on the system.
Construtores

```pde
PFont()
PFont(input)

```
Parâmetros
input
InputStream

#### Utilização

	
Web & Applicações

#### Relacionado

[loadFont() ](loadFont_)
[textFont() ](textFont_)
[text() ](text_)

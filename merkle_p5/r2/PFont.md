<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### PFont
<img height="25" src="../images/1pix.gif" width="1"/>

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
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição

	
PFont is the font class for Processing. The**loadFont()** function constructs a new font and**textFont()** makes a font active. The**list()** method creates a list of the fonts installed on the computer, which is useful information to use with the<c>createFont()</c> function for dynamically converting fonts into a format to use with Processing.
<img height="25" src="../images/1pix.gif" width="1"/>
Métodos
[list()](PFont_list_)
Gets a list of the fonts installed on the system.
<img height="25" src="../images/1pix.gif" width="1"/>
<img height="25" src="../images/1pix.gif" width="1"/>
Construtores

```pde
PFont()
PFont(<font color="#996600">input</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
input
InputStream
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado

[loadFont() ](loadFont_)
[textFont() ](textFont_)
[text() ](text_)

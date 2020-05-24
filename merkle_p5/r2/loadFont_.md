<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### loadFont()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/loadFont_.gif" width="100"/>
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

	
Loads a font into a variable of type**PFont**. To load correctly, fonts must be located in the data directory of the current sketch.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
loadFont(<font color="#996600">fontname</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
fontname
string: name of the font to load
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
PFont
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado

[PFont ](PFont)
[textFont() ](textFont_)
[text() ](text_)

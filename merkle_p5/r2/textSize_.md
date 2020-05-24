<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### textSize()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/textSize_.gif" width="100"/>
```pde
PFont font; 
// The font must be located in the sketch's 
// "data" directory to load successfully 
font = loadFont("FFScala-32.vlw"); 
textFont(font, 32); 
text("word", 15, 50); 
textSize(14); 
text("word", 15, 70); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição

	
Sets the current font size. This size will be used in all subsequent calls to the**text()** function. Font size is measured in units of pixels.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
textSize(<font color="#996600">size</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
size
int or float: the size of the letters in units of pixels
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado

[loadFont() ](loadFont_)
[PFont ](PFont)
[text()](text_)
[textFont() ](textFont_)

<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### textAlign()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/textAlign_.gif" width="100"/>
```pde
PFont font; 
// The font must be located in the current sketch's 
// "data" directory to load successfully 
font = loadFont("EurekaMonoCond-Bold-20.vlw"); 
textFont(font, 20); 
textAlign(RIGHT); 
text("word", 50, 30); 
textAlign(CENTER); 
text("word", 50, 50); 
textAlign(LEFT); 
text("word", 50, 70); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição

	
Sets the current alignment for drawing text. The parameters LEFT, CENTER, and RIGHT set the display characteristics of the letters in relation to the values for the**x** and**y** parameters of the**text()** function.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
textAlign(<font color="#996600">MODE</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
MODE
Either LEFT, CENTER, or RIGHT
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
[text() ](text_)

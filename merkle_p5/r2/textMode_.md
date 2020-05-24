<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### textMode()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/textMode_.gif" width="100"/>
```pde
PFont metaBold; 
// The font "Meta-Bold.vlw.gz" must be located in the 
// current sketch's "data" directory to load successfully 
metaBold = loadFont("Meta-Bold.vlw.gz"); 
String lines = "screen"; 
textFont(metaBold); 
textMode(SCREEN); 
text(lines, 3, 70); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição

	
Sets the way text draws to the screen. In the default configuration, it's possible to rotate, scale, and place letters in three dimensional space. Changing to SCREEN mode draws letters directly to the front of the windows and increases the rendering quality of the letters. The letters draw at the actual size of the font (in pixels) and therefore calls to**textSize()** will not affect the size of the letters. To create a font at the size you desire, use the "Create font..." option in the Tools menu.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
textMode(<font color="#996600">MODE</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
MODE
either MODEL or SCREEN
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

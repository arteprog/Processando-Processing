<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### textWidth()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/textWidth_.gif" width="100"/>
```pde
PFont font; 
font = loadFont("FFScala-32.vlw"); 
textFont(font, 32); 
 
char c = 'T'; 
float cw = textWidth(c); 
text(c, 0, 40); 
line(cw, 0, cw, 50); 
 
String s = "Tokyo"; 
float sw = textWidth(s); 
text(s, 0, 85); 
line(sw, 50, sw, 100); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição

	
Calculates and returns the width of any character or text string.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
textWidth(<font color="#996600">data</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
data
char or String
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Float
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado

[loadFont() ](loadFont_)
[PFont ](PFont)
[text()](text_)
[textFont() ](textFont_)

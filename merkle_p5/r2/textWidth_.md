
#### Nome
### textWidth()

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

#### Descrição

	
Calculates and returns the width of any character or text string.

#### Sintaxe
```pde
textWidth(data)

```
Parâmetros
data
char or String



#### Retorno

	
Float

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


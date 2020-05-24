
#### Nome
### textAlign()

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

#### Descrição

	
Sets the current alignment for drawing text. The parameters LEFT, CENTER, and RIGHT set the display characteristics of the letters in relation to the values for the **x** and **y** parameters of the **text()** function.

#### Sintaxe
```pde
textAlign(MODE)

```
Parâmetros
MODE
Either LEFT, CENTER, or RIGHT



#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado

[loadFont() ](loadFont_
)
[PFont ](PFont
)
[text() ](text_
)


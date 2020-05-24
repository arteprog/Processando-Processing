<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### loop()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
void setup() { 
  size(200, 200); 
  noLoop(); 
} 
 
float x = 0; 
 
void draw() { 
  background(204); 
  x = x + .1; 
  if (x > width) { 
    x = 0; 
  } 
  line(x, 0, x, height); 
} 
 
void mousePressed() { 
  loop(); 
} 
 
void mouseReleased() { 
  noLoop(); 
} 

```

#### Descrição
determina que Processing irá execurar o código em**draw()** continuamente.  Caso**noLoop()** seja chamada, o código em**draw()** parará de executar.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
loop()
redraw()
draw()

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[noLoop()](noLoop_)

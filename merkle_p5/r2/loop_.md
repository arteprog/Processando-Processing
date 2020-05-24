
#### Nome
### loop()

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
determina que Processing irá execurar o código em `draw()` continuamente.  Caso `noLoop()` seja chamada, o código em `draw()` parará de executar.

#### Sintaxe
```pde
loop()
redraw()
draw()

```

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[noLoop()](noLoop_
)


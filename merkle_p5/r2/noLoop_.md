
#### Nome
### noLoop()

#### Exemplos

```pde
void setup() { 
  size(200, 200); 
  noLoop(); 
} 
 
void draw() { 
  line(10, 10, 190, 190); 
} 

```
<hr align="left" noshade="noshade" size="1" width="150"/>

```pde
void setup() { 
  size(200, 200); 
} 
 
float x = 0.0; 
 
void draw() { 
  background(204); 
  x = x + 0.1; 
  if (x > width) { 
    x = 0; 
  } 
  line(x, 0, x, height); 
} 
 
void mousePressed() { 
  noLoop(); 
} 
 
void mouseReleased() { 
  loop(); 
} 

```

#### Descrição
Para o Processind de continuamente executar o código em**draw()**.  Caso**loop() **seja chamada,  o código em**draw() **é executado continuamente.

#### Sintaxe
```pde
noLoop()
redraw()
draw()

```

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[loop()](loop_)

<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### noLoop()
<img height="25" src="../images/1pix.gif" width="1"/>

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
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
noLoop()
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
[loop()](loop_)

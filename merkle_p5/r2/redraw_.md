
#### Nome
### redraw()

#### Exemplos

```pde
float x = 0; 
 
void setup() { 
  size(200, 200); 
  noLoop(); 
} 
 
void draw() { 
  background(204); 
  line(x, 0, x, height); 
} 
 
void mousePressed() { 
  x += 1; 
  redraw(); 
} 

```



#### Descrição
Executa o código incluso em `draw() ` uma
vez. Esta função permite ao programa atualizar a janela
de visualização apenas quando necessário, por
exemplo, quando um evento registrado por `mousPressed() `ou `keyPressed()` ocorrer. Na estruturação de um programa, apenas faz sentido chamar redraw() em evento tais como `mousPressed().  `Chamá-la em `draw()` não tem efeito, pois esta é executada continuamente de qualquer modo.

#### Sintaxe
```pde
redraw()

```

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[noLoop()](noLoop_
)
[loop()](loop_
)


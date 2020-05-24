
#### Nome
### mouseMoved()

#### Exemplos

```pde
// Mova o mouse através da imagem para
// mudar seu valor
 
int value = 0; 
 
void draw() { 
  fill(value); 
  rect(25, 25, 50, 50); 
} 
 
void mouseMoved() 
{ 
  value = value + 5; 
  if (value > 255) { 
    value = 0; 
  } 
} 

```



#### Descrição
A função `mouseMoved() `é chamada cada vez que o mouse move e que um botão não é pressionado.

#### Sintaxe
```pde
mouseMoved()

```

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[mouseX](mouseX
)
[mouseY](mouseY
)
[mousePressed](mousePressed
)
[mousePressed()](mousePressed_
)
[mouseReleased()](mouseReleased_
)
[mouseDragged()](mouseDragged_
)


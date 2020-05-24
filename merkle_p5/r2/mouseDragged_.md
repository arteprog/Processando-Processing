
#### Nome
### mouseDragged()

#### Exemplos

```pde
// Arraste (pressione e mantenha pressionado) seu mouse através
// da imagem para mudar o valor do retângulo
 
int value = 0; 
 
void draw() { 
  fill(value); 
  rect(25, 25, 50, 50); 
} 
 
void mouseDragged() 
{ 
  value = value + 5; 
  if (value > 255) { 
    value = 0; 
  } 
} 

```



#### Descrição
Chamada cada vez que o mouse move e que um botão do mouse é pressionando.

#### Sintaxe
```pde
mouseDragged

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
[mouseMoved()](mouseMoved_
)


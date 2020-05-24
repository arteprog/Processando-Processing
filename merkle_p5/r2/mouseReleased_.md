
#### Nome
### mouseReleased()

#### Exemplos

```pde
// Clique na imagem para mudar
// o valor do retângulo
 
int value = 0; 
 
void draw() { 
  fill(value); 
  rect(25, 25, 50, 50); 
} 
 
void mouseReleased() 
{ 
  if(value == 0) { 
    value = 255; 
  } else { 
    value = 0; 
  } 
} 

```



#### Descrição

	
TA função **mouseReleased()** é chamada cada vez que um botão do mouse é solto.

#### Sintaxe
```pde
mouseReleased()

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
[mouseMoved()](mouseMoved_
)
[mouseDragged()](mouseDragged_
)


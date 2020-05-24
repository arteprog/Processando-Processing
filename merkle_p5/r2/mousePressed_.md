
#### Nome
### mousePressed()

#### Exemplos

```pde
// Clique na imagem para mudar
// o valor do retângulo
 
int value = 0; 
 
void draw() { 
  fill(value); 
  rect(25, 25, 50, 50); 
} 
 
void mousePressed() 
{ 
  if(value == 0) { 
    value = 255; 
  } else { 
    value = 0; 
  } 
} 

```

#### Descrição
A função**mousePressed()** é chamada cada vez que um botão do mouse é pressionada. A variável**mousButton **é utilizada para se determinar qual botão está pressionado.

#### Sintaxe
```pde
mousePressed()

```

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[mouseX](mouseX)[mouseY](mouseY)[mouseButton](mouseButton)[mousePressed](mousePressed)[mouseReleased()](mouseReleased_)[mouseMoved()](mouseMoved_)[mouseDragged()](mouseDragged_)

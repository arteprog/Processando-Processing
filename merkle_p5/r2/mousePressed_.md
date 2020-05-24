<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### mousePressed()
<img height="25" src="../images/1pix.gif" width="1"/>

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
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
mousePressed()

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[mouseX](mouseX)[mouseY](mouseY)[mouseButton](mouseButton)[mousePressed](mousePressed)[mouseReleased()](mouseReleased_)[mouseMoved()](mouseMoved_)[mouseDragged()](mouseDragged_)

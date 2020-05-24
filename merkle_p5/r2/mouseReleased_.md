<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### mouseReleased()
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

	
TA função**mouseReleased()** é chamada cada vez que um botão do mouse é solto.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
mouseReleased()

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[mouseX](mouseX)[mouseY](mouseY)[mousePressed](mousePressed)[mousePressed()](mousePressed_)[mouseMoved()](mouseMoved_)[mouseDragged()](mouseDragged_)

<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### mouseDragged()
<img height="25" src="../images/1pix.gif" width="1"/>

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
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
mouseDragged

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[mouseX](mouseX)[mouseY](mouseY)[mousePressed](mousePressed)[mousePressed()](mousePressed_)[mouseReleased()](mouseReleased_)[mouseMoved()](mouseMoved_)

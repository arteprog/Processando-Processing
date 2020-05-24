<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### mouseMoved()
<img height="25" src="../images/1pix.gif" width="1"/>

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
A função**mouseMoved() **é chamada cada vez que o mouse move e que um botão não é pressionado.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
mouseMoved()

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[mouseX](mouseX)[mouseY](mouseY)[mousePressed](mousePressed)[mousePressed()](mousePressed_)[mouseReleased()](mouseReleased_)[mouseDragged()](mouseDragged_)

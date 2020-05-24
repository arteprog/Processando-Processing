<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### key
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
// Clique na janela para lhe dar foco e 
// pressiona a tecla 'B'
 
void draw() { 
  if(keyPressed) { 
    if (key == 'b' || key == 'B') { 
      fill(0); 
    } 
  } else { 
    fill(255); 
  } 
  rect(25, 25, 50, 50); 
} 

```

#### Descrição
A variável de sistema**key**
sempre contém o valor da tecla pressionada mais recentemente no
teclado. Para se detetar as teclas de direcionamento, é
atribuído à variável**keyCode** um dos valores entre  UP, DOWN, LEFT, ou RIGHT.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
key

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[keyPressed ](keyPressed)[keyCode](keyCode)[keyPressed() ](keyPressed_)[keyReleased() ](keyReleased_)

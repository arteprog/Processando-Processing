<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### keyCode
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
color fillVal = color(126); 
 
void draw() { 
  fill(fillVal); 
  rect(25, 25, 50, 50); 
} 
 
void keyPressed() { 
  if(key == CODED) { 
    if (keyCode == UP) { 
      fillVal = 255; 
    } else if (keyCode == DOWN) { 
      fillVal = 0; 
    } 
  } else { 
    fillVal = 126; 
  } 
} 

```

#### Descrição
A variável de sistema**keyCode**
é utilizada para se detetar teclas especiais como as techas UP,
DOWN, LEFT, or RIGHT  (n.t. para cime, para  baixo, para a
esquerda e para a direita, respectivamente) do teclado. Outras
constantes de teclas especiais  são ALT, CONTROL, SHIFT,
BACKSPACE, TAB, ENTER, RETURN, ESC, e DELETE. Antes de testar qual
código de tecla foi pressionado, é necessário
testar e ver ser a tecla foi mesmo codificada. Isto pode ser feito com
o comando condicional "if(key == CODED) {}", como ilustrado no exemplo
acima.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
keyCode

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[key](key)[keyPressed ](keyPressed)[keyPressed() ](keyPressed_)[keyReleased() ](keyReleased_)

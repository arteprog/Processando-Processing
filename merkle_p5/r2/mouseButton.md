
#### Nome
### mouseButton

#### Exemplos

```pde
// Clique sobre a imagem e pressione os botões
// esquerdo e direito do mousse para mudar 
// o valor do retângulo
void draw() { 
  if (mousePressed && (mouseButton == LEFT)) { 
    fill(0); 
  } else if (mousePressed && (mouseButton == RIGHT)) { 
    fill(255); 
  } else { 
    fill(126); 
  } 
  rect(25, 25, 50, 50); 
} 

```



```pde
// Clique sobre a imagem e pressione os botões
// esquerdo e direito do mousse para mudar 
// o valor do retângulo
void draw() { 
  rect(25, 25, 50, 50); 
} 
 
void mousePressed() { 
  if (mouseButton == LEFT) { 
    fill(0); 
  } else if (mouseButton == RIGHT) { 
    fill(255); 
  } else { 
    fill(126); 
  } 
} 

```



#### Descrição
Processing rastreia automaticamente se o
botão do mouse é pressionando, assim como qual
botão é pressionando. O valor da variável de
sistema **mouseButton** pode ser um entre **LEFT**, **RIGHT**, ou **CENTER**, dependendo de qual botão foi pressionado.

#### Utilização

	
Web & Applicações

#### Relacionado
[mouseX](mouseX
)
[mouseY](mouseY
)
[mousePressed()](mousePressed_
)
[mouseReleased()](mouseReleased_
)
[mouseMoved()](mouseMoved_
)
[mouseDragged()](mouseDragged_
)


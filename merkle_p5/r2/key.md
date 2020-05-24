
#### Nome
### key

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
A variável de sistema `key`
sempre contém o valor da tecla pressionada mais recentemente no
teclado. Para se detetar as teclas de direcionamento, é
atribuído à variável `keyCode` um dos valores entre  UP, DOWN, LEFT, ou RIGHT.

#### Sintaxe
```pde
key

```

#### Utilização

	
Web & Applicações

#### Relacionado
[keyPressed ](keyPressed
)
[keyCode](keyCode
)
[keyPressed() ](keyPressed_
)
[keyReleased() ](keyReleased_
)


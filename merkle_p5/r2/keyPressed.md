
#### Nome
### keyPressed

#### Exemplos

```pde
// Clique na imagem para lhe dar foco
// e pressione qualquer tecla
 
// Nota: o retângulo neste exemplo pode
// piscar quando o sistema operacional 
// registrar um aperto de tecla longo como
// uma repetição de apertos de tecla
 
void draw() { 
  if (keyPressed == true) { 
    fill(0); 
  } else { 
    fill(255); 
  } 
  rect(25, 25, 50, 50); 
} 

```



#### Descrição


A variável booleana **keyPressed** é  verdadeira (<span style="font-style: italic;"> `true` )</span> se uma tecla está pressionada e falsa (<span style="font-weight: bold;"> *false* )</span> se uma tecla não está pressionada.

#### Sintaxe
```pde
keyPressed

```

#### Utilização

	
Web & Applicações

#### Relacionado
[key ](key
)
[keyCode](keyCode
)
[keyPressed() ](keyPressed_
)
[keyReleased() ](keyReleased_
)


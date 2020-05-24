
#### Nome
### keyReleased()

#### Exemplos

```pde
// Clique na imagem para lhe dar foco
// e pressione qualquer tecla
 
int value = 0; 
 
void draw() { 
  fill(value); 
  rect(25, 25, 50, 50); 
} 
 
void keyReleased() 
{ 
  if(value == 0) { 
    value = 255; 
  } else { 
    value = 0; 
  } 
} 

```



#### Descrição


	A função `keyReleased() ` é
chamada cada vez que uma tecla é pressionada. Como regra geral,
nada deve ser desenhado no escopo do bloco de `keyReleased().`

#### Sintaxe
```pde
void keyReleased() { 
  comandos
}
            
```

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[keyPressed ](keyPressed
)
[key ](key
)
[keyCode](keyCode
)
[keyPressed() ](keyPressed_
)


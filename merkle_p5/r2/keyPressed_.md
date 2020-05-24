<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### keyPressed()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
// Clique na imagem para lhe dar foco
// e pressione qualquer tecla
 
int value = 0; 
 
void draw() { 
  fill(value); 
  rect(25, 25, 50, 50); 
} 
 
void keyPressed() 
{ 
  if(value == 0) { 
    value = 255; 
  } else { 
    value = 0; 
  } 
} 

```

#### Descrição
A função**keyPressed() ** é
chamada cada vez que uma tecla é pressionada. Como regra geral,
nada deve ser desenhado no escopo do bloco de**keyPressed().**
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
void keyPressed() { 
  <font color="#996600">comandos</font>
}
            
```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[keyPressed ](keyPressed)[key ](key)[keyCode](keyCode)[keyReleased() ](keyReleased_)

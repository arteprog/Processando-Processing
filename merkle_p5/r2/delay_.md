<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### delay()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
int pos = 0; 
void draw() { 
  background(204); 
  pos++; 
  line(pos, 20, pos, 80); 
  if(pos > width) { 
    pos = 0; 
  } 
  delay(250);  // Atrasa um programa por 250 milisegundos
} 

```

#### Descrição
Força um programa a parar de executar por um
tempo especificado. Tempos de atraso são especificados em
milésimos de segundo. A chamada de função**delay(3000) **atrasará
a execução do progrma por três segundos. A
função causa uma parada no programa assim que é
chamada, exceto na primeira vez em que estiver
executando função** draw()**,** **quando parará o programa apenas após o laço ter sido completado.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
delay(<font color="#996600">milisegundos</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
milisegundos
int: espesificado como milisegundo (há 1000 ms em 1 segundo)
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

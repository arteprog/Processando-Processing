<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### minute()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
void draw() { 
  background(204); 
  int s = second();  // Values from 0 - 59 
  int m = minute();  // Values from 0 - 59 
  int h = hour();    // Values from 0 - 23 
  line(s, 0, s, 33); 
  line(m, 33, m, 66); 
  line(h, 66, h, 100); 
} 

```

#### Descrição
Processing se comunica com o relógio de seu computador. A função**minute()** retorna o minuto corrente como um valor entre 0 e 59.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
minute()

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
int
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[millis() ](millis_)[second()](second_)[minute()](minute_)[hour()](hour_)[day()](day_)[month()](month_)[year()](year_)

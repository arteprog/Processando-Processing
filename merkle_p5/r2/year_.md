
#### Nome
### year()

#### Exemplos

```pde
void setup() { 
  PFont metaBold; 
  metaBold = loadFont("fonts/Meta-Bold.vlw.gz"); 
  setFont(metaBold, 44); 
  noLoop(); 
} 
 
void draw() { 
  int d = day();    // Values from 1 - 31 
  int m = month();  // Values from 1 - 12 
  int y = year();   // 2003, 2004, 2005, etc. 
  String s = String.valueOf(d); 
  text(s, 10, 28); 
  s = String.valueOf(m); 
  text(s, 10, 56); 
  s = String.valueOf(y); 
  text(s, 10, 84); 
} 
 

```

#### Descrição
Processing se comunica com o relógio de seu computador. A função**year()** retorna o ano corrente como um valor inteiro (2003, 2004, 2005, etc).

#### Sintaxe
```pde
year()

```

#### Retorno

	
int

#### Utilização

	
Web & Applicações

#### Relacionado
[millis() ](millis_)[second()](second_)[minute()](minute_)[hour()](hour_)[day()](day_)[month()](month_)[year()](year_)

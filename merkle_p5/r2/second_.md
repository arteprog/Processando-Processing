
#### Nome
### second()

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
Processing se comunica com o relógio de seu computador. A função `second()` retorna segundo corrente  como um valor entre 0 e 59.

#### Sintaxe
```pde
second

```

#### Retorno

	
int

#### Utilização

	
Web & Applicações

#### Relacionado
[millis() ](millis_
)
[second()](second_
)
[minute()](minute_
)
[hour()](hour_
)
[day()](day_
)
[month()](month_
)
[year()](year_
)


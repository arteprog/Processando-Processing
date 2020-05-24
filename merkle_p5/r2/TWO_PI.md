
#### Nome
### TWO_PI (6.28318...)

#### Exemplos
<img border="0" height="100" src="media/TWO_PI.gif" width="100"/>

```pde
float f = 0.0; 
beginShape(POLYGON); 
while(f < TWO_PI) { 
  vertex(width/2 + cos(f)*40, height/2 + sin(f)*40); 
  f += PI/12.0; 
} 
endShape(); 

```

#### Descrição
TWO_PI é uma constante matemática de valor constante igual à
6.28318530717958647693. É o dobro da razão entre a circunferência de
um círculo e seu diâmetro. É útil em combinações com as funções
trigonométricas**sin()** e**cos()**.

#### Sintaxe
```pde
TWO_PI

```

#### Utilização

	
Web & Applicações

#### Relacionado
[PI](PI)[HALF_PI](HALF_PI)


#### Nome
### HALF_PI (1.57079...)

#### Exemplos
<img border="0" height="100" src="media/HALF_PI.gif" width="100"/>

```pde
float f = 0.0; 
beginShape(POLYGON); 
while(f < HALF_PI) { 
  vertex(width/2 + cos(f)*40, height/2 + sin(f)*40); 
  f += PI/12.0; 
} 
endShape(); 

```

#### Descrição
HALF_PI é uma constante matemática de
valor constante igual à 1.57079632679489661923. É a
metade da razão entre a circunferência de um
círculo e seu diâmetro. É útil em
combinações com as funções
trigonométricas**sin()** e**cos()**.

#### Sintaxe
```pde
HALF_PI

```

#### Utilização

	
Web & Applicações

#### Relacionado
[PI](PI)[TWO_PI](TWO_PI)

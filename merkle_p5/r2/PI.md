
#### Nome
### PI (3.14159...)

#### Exemplos
<img border="0" height="100" src="media/PI.gif" width="100"/>

```pde
float f = 0.0; 
beginShape(POLYGON); 
while(f < PI) { 
  vertex(width/2 + cos(f)*40, height/2 + sin(f)*40); 
  f += PI/12.0; 
} 
endShape(); 

```

#### Descrição
PI é uma constante matemática de valor constante igual à
3.14159265358979323846. É a razão entre a circunferência de
um círculo e seu diâmetro. É útil em combinações com as funções
trigonométricas**sin()** e**cos()**.

#### Sintaxe
```pde
PI

```

#### Utilização

	
Web & Applicações

#### Relacionado
[TWO_PI](TWO_PI)[HALF_PI](HALF_PI)

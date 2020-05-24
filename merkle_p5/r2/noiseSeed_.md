
#### Nome
### noiseSeed()

#### Exemplos

```pde
float xoff = 0.0; 
 
void setup() { 
  noiseSeed(0); 
  stroke(0, 10); 
} 
 
void draw() 
{ 
  xoff = xoff + .01; 
  float n = noise(xoff) * width; 
  line(n, 0, n, height); 
} 

```



#### Descrição
Atribui um valor de semente para `noise()`. Como padrão, `noise()` produz resultados diferentes cada vez que é chamada.  Atribua ao parâmetro `valor `uma constante para se obter os mesmos números pseudo-randômicos cada vez que o software for executado.

#### Sintaxe
```pde
noiseSeed(valor)

```
Parâmetros
valor
int: semente para se calcular os números



#### Retorno

	
float

#### Utilização

	
Web & Applicações

#### Relacionado
[noise()](noise_
)
[noiseDetail()](noiseDetail_
)
[random()](random_
)
[randomSeed()](randomSeed_
)


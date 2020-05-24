<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### noiseSeed()
<img height="25" src="../images/1pix.gif" width="1"/>

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
Atribui um valor de semente para**noise()**. Como padrão,**noise()** produz resultados diferentes cada vez que é chamada.  Atribua ao parâmetro**valor **uma constante para se obter os mesmos números pseudo-randômicos cada vez que o software for executado.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
noiseSeed(<font color="#996600">valor</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
valor
int: semente para se calcular os números
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
float
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[noise()](noise_)[noiseDetail()](noiseDetail_)[random()](random_)[randomSeed()](randomSeed_)

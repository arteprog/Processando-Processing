
#### Nome
### noise()

#### Exemplos

```pde
float xoff = 0.0; 
void draw() 
{ 
  background(204); 
  xoff = xoff + .01; 
  float n = noise(xoff) * width; 
  line(n, 0, n, height); 
} 

```
<hr align="left" noshade="noshade" size="1" width="150"/>

```pde
float noiseScale=0.02; 
void draw() { 
  background(0); 
  for(int x=0; x<width; x++) { 
    float noiseVal = noise((mouseX+x)*noiseScale, 
                            mouseY*noiseScale); 
    stroke(noiseVal*255); 
    line(x, mouseY+noiseVal*80, x, height); 
  } 
} 

```

#### Descrição
Retorna um valor de ruído de Perlim em
coordenadas específicas. O ruído de Perin é um
gerador de seqüências randômicas que produz uma
sucessão ordenada de modo mais natural de números, se
comparada a função padrão**random()**.
 Ela foi inventada por Ken Perlin nos anos de 1980, e tem sido
utilizada desde então em aplicações
gráficas para produzir texturas, movimento natural, formas,
terrenos, etc.
Sua principal diferença da função**random()**
reside no fato de que o ruído de perlin é definido cem um
espaço n-dimensional, onde cada pare de coordenadas corresponde
a um valor fixo-semi-randômico (fixo no temp de vida de um
programa). O valor resultante sempre será entre 0.0 e 1.0.
Processing pode computar ruído de Perlin 1D, 2D e 3D, dependendo
do número de coordenadas dados. O valor do ruído pode ser
animado ao se movimentar pelo espaço de ruído como
demonstrado no exemplo acima. A segunda e a terceira dimensão
também podem ser interpretadas como tempo.
O rído real pode ser estruturado de modo similara a um sinal de
áudio, em respeito ao uso que a função faz de
freqüências. De modo similara ao conceito de
harmônicas em física, o ruído de Perlin é
calculado sobre várias oitavas, as quais são somadas para
se obter o reultado final.
Uma outra forma de se ajustar a qualidade da seqüência
resultante  é a escala das coordenadas de entrada. Como a
função trabalha em um espaço infinito, o
valor das coordenadas não importa como tal, mas distância
entre coordenadas sucessicas (por exemplo, na utilização
de**noise()** em um laço).
omo regra geral, quanto menor a diferença entre coordenadas,
mais suave será a seqüência de ruído de Perlin
resultante. Passos entre 0.0003 e 0.003 funcionam melhor para a maioria
das aplicações, mas pode ser diferente dependendo do uso.

#### Sintaxe
```pde
noise(x)
noise(x, y)
noise(x, y, z)

```
Parâmetros
x
float: coordenada x no espaço de ruído de Perlin
y
float: coordenada y no espaço de ruído de Perlin
z
float: coordenada z no espaço de ruído de Perlin

#### Retorno

	
float

#### Utilização

	
Web & Applicações

#### Relacionado
[noiseDetail()](noiseDetail_)[random()](random_)

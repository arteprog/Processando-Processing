
#### Nome
### random()

#### Exemplos

```pde
for(int i=0; i<100; i++) { 
 float r = random(50); 
 stroke(r*5); 
 line(50, i, 50+r, i); 
} 

```
<hr align="left" noshade="noshade" size="1" width="150"/>

```pde
for(int i=0; i<100; i++) { 
 float r = random(-50, 50); 
 stroke(abs(r*5)); 
 line(50, i, 50+r, i); 
} 

```

#### Descrição
Gera números pseudo-randômicos. Cada vez que a função**random()**
é chamada, ela retorna um valor não esperado em
determinado intervalo. Se um valor é passado a
função, ela irá retornar um**float** entre zero e o valor deste parâmetro. A chamada de função**random(5)**
retorna valores entre 0.0 e 5.0. Se dois parâmetros são
passados, ela irá retornar um float com valor entre estes
parâmetros. A chamada de função**random(-5.0, 10.2)** 
retornará valores entre -5.0 e 10.2. Para se converter um
número randômico de ponto flutuante para inteiro, use a
função**int()**.<span style="font-weight: bold;"></span><span style="font-weight: bold;"></span>

#### Sintaxe
```pde
random(valor1);
random(valor1, valor2);

```
Parâmetros
valor1
int
ou float
valor2
int
ou float

#### Retorno
 float

#### Utilização
 Web &
Applicações

#### Relacionado
[noise()](noise_)[randomSeed()](randomSeed_)

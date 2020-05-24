
#### Nome
### randomSeed()

#### Exemplos

```pde
randomSeed(0); 
for(int i=0; i<100; i++) { 
  float r = random(0, 255); 
  stroke(r); 
  line(i, 0, i, 100); 
} 
 

```

#### Descrição
Atribui um valor de semente para**random()**. Como padrão,**random()** produz resultados diferentes cada vez que é chamada. Atribua ao parâmetro**valor **uma constante para se obter os mesmos números pseudo-randômicos cada vez que o software for executado.

#### Sintaxe
```pde
random(valor);

```
Parâmetros
valor
int: valor da semente para se gerar os números

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[random()](random_)[noise()](noise_)[noiseSeed()](noiseSeed_)

<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### randomSeed()
<img height="25" src="../images/1pix.gif" width="1"/>

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
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
random(<font color="#996600">valor</font>);

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
valor
int: valor da semente para se gerar os números
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[random()](random_)[noise()](noise_)[noiseSeed()](noiseSeed_)

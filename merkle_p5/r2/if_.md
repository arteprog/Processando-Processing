
#### Nome
### if()

#### Exemplos
<img border="0" height="100" src="media/if_.gif" width="100"/>

```pde
for(int i=5; i<height; i+=5) { 
  stroke(255);  // Atribui a cor ao branco
  if(i < 35) {  // Quando "i" form menor que "35"... 
    stroke(0);  //... atribui a cor ao preto
  } 
  line(30, i, 80, i); 
} 

```

#### Descrição
Permite ao programa decidir entre a execução de um código a executar.  Caso a `expressão `seja avaliada como verdadeira, os comandos contidos no bloco serão executados. Caso a `expressão `seja avaliada como falsa, os comandos contidos no bloco não serão executados.

#### Sintaxe
```pde
if(expresão) { 
  comandos 
} 

```
Parâmetros
expresão
qualquer expressão que possa ser avaliada como verdadeira ou falsa

comandos
um ou mais comandos a executar



#### Utilização

	
Web & Applicações

#### Relacionado
[else](else
)


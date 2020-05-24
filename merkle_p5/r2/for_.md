
#### Nome
### for()

#### Exemplos
<img border="0" height="100" src="media/for_.gif" width="100"/>

```pde
for(int i=0; i<40; i=i+1) { 
  line(30, i, 80, i); 
} 

```
<img border="0" height="100" src="media/for_2.gif" width="100"/>

```pde
for(int i=0; i<80; i=i+5) { 
  line(30, i, 80, i); 
} 

```
<img border="0" height="100" src="media/for_3.gif" width="100"/>

```pde
for(int i=40; i<80; i=i+5) { 
  line(30, i, 80, i); 
} 

```
<img border="0" height="100" src="media/for_4.gif" width="100"/>

```pde
for(int i=30; i<80; i=i+5) { 
  for(int j=0; j<80; j=j+5) { 
    point(i, j); 
  } 
} 

```

#### Descrição
Controla uma seqüência de repetições. A estrutura `for ` tem três partes: **início**, **teste**, e **coda**. Cada parte deve ser separada por um ponto e vírgula (';'). O laço continua ate que `teste` seja avaliada como `false` *. *Quando a estrutura `for()`é executada, a seguinte seqüência passos ocorre:


1. os comandos em "início" são executados;


2. a expressão "teste" é avaliada verdadeira ou falsa;


3. Caso "teste" seja verdadeira ( *true*), passa-se ao passo 4.   Caso "teste" seja falsa ( *false*), passa-se ao passo 6;


4. Executam-se os comandos contidos no bloco da estrutura em laço;


5. Executam-se os comandos em "coda" e  passa-se ao passo 2;


6.  Sai-se do laço.


#### Sintaxe
```pde
for(início; teste; coda) { 
  comandos
} 
            
```
Parâmetros
início
inclui os comandos execudados uma única vez antes do início do laço


teste
caso "teste"seja avaliado verdadeiro ( **true** ), os comando são executados


comandos

conjunto de comandos executados em cada iteração do laço


coda
inclui comandos executadas ao final de cada iteração do laço





#### Utilização

	
Web & Applicações

#### Relacionado
[while()](while_
)


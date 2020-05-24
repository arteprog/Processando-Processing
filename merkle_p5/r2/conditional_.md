
#### Nome
### ?: (condicional)

#### Exemplos

```pde
int s = 0; 
for(int i=5; i<100; i+=5) { 
  s = (i < 50) ? 0 : 255; 
  stroke(s); 
  line(30, i, 80, i); 
} 

```

#### Descrição
Uma abreviação para se escrever uma estrutura de controle**se() **e**senão **(**if()** e**else**). Se a condição for avaliada como verdadeira (**true**) , a**expressão1 ** é valiada e retornada. Se a condição for avaliada como falsa (**false**) , a**expressão2 ** é valiada e retornada.
A seguinte estrutura conticional :```pde
condição : expressão1 ? expressão2
```
is equivalent to this structure:```pde
if(condição) {
  expressão1 
} else { 
  expressão2 
}
```

#### Sintaxe
```pde
condição ? expressão1 : expressão2
            
```
Parâmetros
condição
qualquer expressão que possa ser avaliada como verdadeira ou falsa
expressão1
qualquer expressão válida
expressão2
qualquer expressão válida

#### Retorno
Variável, dependendo do tipo de dados das expressões

#### Utilização

	
Web & Applicações

#### Relacionado
[if()](if_)[else](else)

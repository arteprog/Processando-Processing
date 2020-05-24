
#### Nome
### return

#### Exemplos

```pde
int val = 30; 
 
void draw() { 
  int t = timestwo(val); 
  println(t); 
} 
 
int timestwo(int dVal) { 
  dVal = dVal * 2; 
  return dVal; 
} 

```
<hr align="left" noshade="noshade" size="1" width="150"/>

```pde
int[] vals = {10, 20, 30}; 
  
void draw() { 
  int[] t = timestwo(vals); 
  println(t); 
  noLoop(); 
} 
 
int[] timestwo(int[] dVals) { 
  for(int i=0; i<dVals.length; i++) { 
    dVals[i] = dVals[i] * 2; 
  } 
  return dVals; 
} 

```
<hr align="left" noshade="noshade" size="1" width="150"/>

```pde
void draw() { 
  background(204); 
  line(0, 0, width, height); 
  if(mousePressed) { 
    return; 
  } 
  line(0, height, width, 0); 
} 
 

```

#### Descrição
A palavra chave**return**
é utilizada para indicar o tipo de valor a retornar de uma
função. O valor sendo retornado deve ser de tipo igual ao
definido na declaração da função.
Funções declaradas com**void **não podem retornar valores e não podem incluir um valor de retorno. A palavara chace**return ** também
pode ser usada para  sair de uma função, e
consequentemente não permitindo que o program leia e execute os
comandos restantes nela contidos (veja o terceiro exemplo acima).

#### Sintaxe
```pde
tipo funcao {
  comandos
  return valorvalue
}
            
```
Parâmetros
tipo
boolean, byte, char, int, float, String, boolean[], byte[], char[], int[], float[], String[]
funcao
qualquer função que esteja sendo definida
comandos
qualquer comando válido
valor
deve ser do mesmo tipo de dados que o parâmtro "tipo"

#### Utilização

	
Web & Applicações

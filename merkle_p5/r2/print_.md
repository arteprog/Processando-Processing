
#### Nome
### print()

#### Exemplos

```pde
print("begin- "); 
float f = 0.3; 
int i = 1024; 
print("f is " + f + " and i is " + 1024); 
String s = " -end"; 
println(s); 
 
// The above code prints: 
// begin- f is 0.3 and i is 1024 -end 

```
<hr align="left" noshade="noshade" size="1" width="150"/>

```pde
float[] f = { 0.3, 0.4, 0.5 }; 
print(f); 
 
// The above code prints: 
// 0.3 0.4 0.5 

```

#### Descrição
Escreve na área do console do ambiente
Processing. Frequentemente, isto é de ajuda para
se visualizar  os dados que um programa está
produzindo.
A função companheira**println() **trabalha como**print()**,
mas cria um nova linha de texto para cada chamada daquela. Elementos
individuais pode ser separados por aspas ("") e  agregados pelo
operador de adição (+).  Ela também escreve o
conteúdo de um array na área de texto do  console do
ambiete Processing. Isto é de ajuda para se  visualizar
 os dados que um programa está produzindo. Um espaço
é colocado entre cada elemento do array. Esta
função só pode imprimeir arraus 1D, mas pode
testar se o conteúdo de uma array de mais de duas
dimensões é nulo ou não nulo.

#### Sintaxe
```pde
print(data)

```
Parâmetros
data
boolean, byte, char, color, int, float, String, boolean[], byte[], char[], color[], int[], float[], ou String[]

#### Utilização

	
IDE

#### Relacionado
[println()](println_)

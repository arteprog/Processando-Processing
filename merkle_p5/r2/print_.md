<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### print()
<img height="25" src="../images/1pix.gif" width="1"/>

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
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
print(<font color="#996600">data</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
data
boolean, byte, char, color, int, float, String, boolean[], byte[], char[], color[], int[], float[], ou String[]
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
IDE
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[println()](println_)

<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### join()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
<span style="font-family: monospace;">String[]
animals = new String[3]; </span><br style="font-family: monospace;"/>
```<p lang="en-US" style="margin-bottom: 0cm;"><span style="font-family: monospace;">animals[0] = "cat";
                        </span>
<span style="font-family: monospace;">animals[1] = "seal"; </span>
<span style="font-family: monospace;">animals[2] = "bear";
                        </span>
<span style="font-family: monospace;">String joinedAnimals = join(animals, " : ");
                        </span>
<span style="font-family: monospace;">println(joinedAnimals); // Imprime "cat : seal : bear"</span>
</p>
<hr align="left" noshade="noshade" size="1" width="150"/>

```pde
// Juntar um array de ints requer que primeiro
// se converta este para um arrray de strings
int[] numbers = new
int[3]; 
numbers[0] = 8; 
numbers[1] = 67; 
numbers[2] = 5;
String joinedNumbers = join(nf(numbers, 0), ", ");
println(joinedNumbers); // Imprime "8, 67, 5"String men = "Chernenko,Andropov,Brezhnev"; 


```
<<
```pde

```>>
#### Descrição

Combina
um array de Strings em um único String. Para converter arrays
de ints ou floats, é necessários primeiro contertê-los
para strinfs através de nf() ou nfs().<p style="margin-bottom: 0cm;"></p>
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
join(<font color="#996600">stringArray</font>, <font color="#996600">delim</font>)
```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
stringArray
a string a repartir
delim
o caracter a utilizar na delimitação dos dados
Retorna

	
String
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[
](join_)[split()](../split_)[](text_)

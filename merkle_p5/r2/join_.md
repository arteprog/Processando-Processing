
#### Nome
### join()

#### Exemplos

```pde
<span style="font-family: monospace;">String[]
animals = new String[3]; </span><br style="font-family: monospace;"/>
```<p lang="en-US" style="margin-bottom: 0cm;"><span style="font-family: monospace;">animals[0] = "cat";
                        </span><br style="font-family: monospace;"/>
<span style="font-family: monospace;">animals[1] = "seal"; </span><br style="font-family: monospace;"/>
<span style="font-family: monospace;">animals[2] = "bear";
                        </span><br style="font-family: monospace;"/>
<span style="font-family: monospace;">String joinedAnimals = join(animals, " : ");
                        </span><br style="font-family: monospace;"/>
<span style="font-family: monospace;">println(joinedAnimals); // Imprime "cat : seal : bear"</span>

</p>



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

#### Sintaxe
```pde
join(stringArray, delim)
```
Parâmetros
stringArray
a string a repartir


delim
o caracter a utilizar na delimitação dos dados


Retorna

	
String

#### Utilização

	
Web & Applicações

#### Relacionado
[
](join_
)[split()](../split_
)[](text_
)

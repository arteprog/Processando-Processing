
#### Nome
### split()

#### Exemplos

```pde
String men = "Putin Yeltsin Gorbachev"; 
String list[] = split(men); 
// list[0] é agora Putin, list[1] é agora Yeltsin, ... 

```



```pde
String men = "Chernenko,Andropov,Brezhnev"; 
String list[] = split(men, ','); 
// list[0] é agora Chernenko, list[1] é agora Andropov, ... 

```



```pde
String numbers = "8 67 5 309"; 
int list[] = int(split(numbers)); 
// list[0] é agora 8, list[1] é agora 67, ... 

```
<<
```pde

```>>


#### Descrição
<p style="margin-bottom: 0cm;">Uma
função utilitária que separa uma série de
dados incorporados em uma String em um array de Strings. O parâmentro
delim especifica o caracter ou os caracteres que marcam as
fronteiras entre cada elemento.  Se nenhum caracter delim
é especificadao, um caracter em branco é utilizado como
caracter de separação. Caracteres de separação
incluem a tabulação ('\t'), pula linha ('\n' ; n.t.
line feed), enter ( '\r') , pula página ('\f',
n.t. form feed) , e o espaço (' '). Para se converter
uma String em um array de inteiros ou floats, se utilizam as funções
de conversão de tipos int() e float() para se
converter o array de Strings (veja exemplo acima).</p>

#### Sintaxe
```pde
split(str)
split(str, delim)
```
Parâmetros
str
a string a repartir


delim
o caracter a utilizar na separação dos dados


Retorna

	
String[]

#### Utilização

	
Web & Applicações

#### Relacionado
[join()](join_
)[](text_
)

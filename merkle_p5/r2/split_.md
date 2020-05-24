<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### split()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
String men = "Putin Yeltsin Gorbachev"; 
String list[] = split(men); 
// list[0] é agora Putin, list[1] é agora Yeltsin, ... 

```
<hr align="left" noshade="noshade" size="1" width="150"/>

```pde
String men = "Chernenko,Andropov,Brezhnev"; 
String list[] = split(men, ','); 
// list[0] é agora Chernenko, list[1] é agora Andropov, ... 

```
<hr align="left" noshade="noshade" size="1" width="150"/>

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
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
split(<font color="#996600">str</font>)
split(<font color="#996600">str</font>, <font color="#996600">delim</font>)
```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
str
a string a repartir
delim
o caracter a utilizar na separação dos dados
Retorna

	
String[]
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[join()](join_)[](text_)

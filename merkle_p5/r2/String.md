<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### String
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
String str1 = "CCCP"; 
char data[] = {'C', 'C', 'C', 'P'}; 
String str2 = new String(data); 
println(str1);  // Prints "CCCP" to the console 
println(str2);  // Prints "CCCP" to the console 

```

#### Descrição
Uma string é uma seqüência de caracteres. A classe**String**
 inclui métodos para examinar caracteres individuais, para
comparar strings, extrair partes de strings, e para converter strings
inteiras para maiúsculas ou minúsculas. Strings
são sempre definidas entre aspas ("Abc") e caracteres são
sempre definidos entre apostrofos ('A'). Há mais médodos na classe String que aqueles listados
nesta página. Documentação adicional pode ser
localisada em[http://java.sun.com/j2se/1.4.2/docs/api/. ](http://java.sun.com/j2se/1.4.2/docs/api/)
<img height="25" src="../images/1pix.gif" width="1"/>
Métodos
[charAt()](String_charAt_)
Retorna o caracter em um índice especificado
[equals()](String_equals_)
Compara uma string a um objeto especificado
[indexOf()](String_indexOf_)
Retorna o valor do
índice correspondente à primeira ocorrência de um
caracter pertencente à respectiva string
[length()](String_length_)
Retorna o número de caracteres na respectiva string
[substring()](String_substring_)
Retorna uma nova string que é parte da string  dada
[toLowerCase()](String_toLowerCase_)
Converte todos os caracteres da strind para minúsculo
[toUpperCase()](String_toUpperCase_)
Converte todos os caracteres da strind para maiúsculo
<img height="25" src="../images/1pix.gif" width="1"/>
<img height="25" src="../images/1pix.gif" width="1"/>
Construtores
```pde
String(<font color="#996600">data</font>)
String(<font color="#996600">data</font>, <font color="#996600">offset</font>, <font color="#996600">length</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
data
byte[] or char[]: *array* de  bytes a ser decodificado em caracteres ou array de caracteres a ser combinado em uma string
offset
int: índice do primeiro caracter
length
int: número de caracteres
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[char](char)[text()](text_)

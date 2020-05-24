
#### Nome
### String

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
Construtores
```pde
String(data)
String(data, offset, length)

```
Parâmetros
data
byte[] or char[]: *array* de  bytes a ser decodificado em caracteres ou array de caracteres a ser combinado em uma string
offset
int: índice do primeiro caracter
length
int: número de caracteres

#### Utilização

	
Web & Applicações

#### Relacionado
[char](char)[text()](text_)

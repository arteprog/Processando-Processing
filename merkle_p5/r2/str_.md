
#### Nome
### str()

#### Exemplos

```pde
boolean b = false; 
byte y = -28; 
char c = 'R'; 
float f = -32.6; 
int i = 1024; 
 
String sb = str(b); 
String sy = str(y); 
String sc = str(c); 
String sf = str(f); 
String si = str(i); 
 
sb = sb + sy + sc + sf + si + sh; 
 
println(sb);  // Imprime 'false-28R-32.61024' 

```

#### Descrição
Retorna uma representação em  String  de tipos de dados primitivos e*arrays. *Por
exemplo, o inteiro  3 retornará "3", o  float -12.6
retornará a string "-12.6", e o valor booleano*true* retornará a string "true".

#### Sintaxe
```pde
str(dado)

```
Parâmetros
dado
boolean, byte, char, float, int, boolean[], byte[], char[], float[], int[]

#### Retorno

	
String ou String[]

#### Utilização

	
Web & Applicações

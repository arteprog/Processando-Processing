
#### Nome
### byte()

#### Exemplos

```pde
float f = 65.0; 
byte b = byte(f); 
println(f + " : " + b);  // Imprime "65.0 : 65" 
 
char c = 'E'; 
b = byte(c); 
println(c + " : " + b);  // Imprime "E : 69" 
 
f = 130.0; 
b = byte(f); 
println(f + " : " + b);  // Imprime "130.0 : -126" 

```

#### Descrição

Converte um tipo de dados primitivo, string ou*array *na
sua representação em bytes. Um byte é um
número inteiro entre -128 e 127. Conseqüentemente, quando
um número fora deste intervalo é convertido, seu valor
é tranpassado à representação em byre
correspondende, como ilustrado no último exemplo acima.

#### Sintaxe
```pde
byte(valor)

```
Parâmetros
valor
int, float, char, boolean, String, int[], float[], char[], boolean[], String[]

#### Retorno

	
byte

#### Utilização

	
Web & Applicações

#### Relacionado
[byte](byte)[int()](int_)

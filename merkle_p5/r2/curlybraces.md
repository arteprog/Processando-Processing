
#### Nome
### {} (chaves)

#### Exemplos

```pde
int[] a = { 5, 20, 25, 45, 70 }; 
 
void setup() { 
  size(100, 100); 
} 
 
void draw() { 
  for(int i=0; i<a.length; i++) { 
    line(0, a[i], 50, a[i]); 
  } 
} 

```

#### Descrição

	
Define o início e o fim de blocos de funções e blocos de comandos tais como nas estruturas** for()** e**if()**. Chaves também são utilizadas para definir os valores iniciais em declarações de vetores.

#### Sintaxe
```pde
{ comandos }
{ ele0, ..., eleN }

```
Parâmetros
comandos
qualquer seqüência válida de comandos
ele0 ... eleN
lista de elementos separados por vírgulas

#### Utilização

	
Web & Applicações

#### Relacionado
[() (parentheses)](parentheses)

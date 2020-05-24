<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### {} (chaves)
<img height="25" src="../images/1pix.gif" width="1"/>

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
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
{ <font color="#996600">comandos</font> }
{ <font color="#996600">ele0</font>, ..., <font color="#996600">eleN</font> }

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
comandos
qualquer seqüência válida de comandos
ele0 ... eleN
lista de elementos separados por vírgulas
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[() (parentheses)](parentheses)

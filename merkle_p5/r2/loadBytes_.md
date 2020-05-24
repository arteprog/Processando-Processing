
#### Nome
### loadBytes()

#### Exemplos

```pde
// abre um arquivo e lê seu conteúdo binário
byte b[] = loadBytes("something.dat"); 
 
// imprime cada valor, de 0 a 255
for (int i = 0; i < b.length; i++) { 
  // cada décimo número, inicia uma nova linha
  if ((i % 10) == 0) { 
    println(); 
  } 
 
  // Bytes são números entre -128 e 127
  // Isto converte para números entre 0 e 255 
  int a = b[i] & 0xff; 
  print(a + " "); 
} 
// imprime um linha branca ao final
println(); 
 

```

#### Descrição
Lê o conteúdo de um arquivo ou de uma
url e o coloca em um array de bytes. Se um arquivo é
especificado, este deve estar localizado no diretório "data" do
diretório/pasta de rascunho.

#### Sintaxe
```pde
loadBytes(filename);

```
Parâmetros
filename
String: nome do arquivo ou url a carregar

#### Retorno

	
byte[]

#### Utilização

	
Web & Applicações

#### Relacionado
[loadStrings()](loadStrings_)[saveStrings()](saveStrings_)[saveBytes() ](saveBytes_)

<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### loadBytes()
<img height="25" src="../images/1pix.gif" width="1"/>

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
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
loadBytes(<font color="#996600">filename</font>);

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
filename
String: nome do arquivo ou url a carregar
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
byte[]
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[loadStrings()](loadStrings_)[saveStrings()](saveStrings_)[saveBytes() ](saveBytes_)

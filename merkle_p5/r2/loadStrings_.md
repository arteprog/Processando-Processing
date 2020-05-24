
#### Nome
### loadStrings()

#### Exemplos

```pde
String lines[] = loadStrings("list.txt"); 
println("there are " + lines.length + " lines"); 
for (int i=0; i < lines.length; i++) { 
  println(lines[i]); 
} 

```



#### Descrição
Lê o conteúdo de um arquivo ou de uma
url e cria um array String de suas linhas individuais. Se um arquivo
é especificado, este deve estar localizado no
diretório "data" do diretório/pasta de rascunho.

#### Sintaxe
```pde
loadStrings(filename)

```
Parâmetros
filename
String: nome do arquivo ou url a carregar



#### Retorno

	
String[]

#### Utilização

	
Web & Applicações

#### Relacionado
[loadBytes() ](loadBytes_
)
[saveStrings()](saveStrings_
)
[saveBytes()](saveBytes_
)


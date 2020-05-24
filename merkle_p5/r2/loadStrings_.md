<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### loadStrings()
<img height="25" src="../images/1pix.gif" width="1"/>

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
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
loadStrings(<font color="#996600">filename</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
filename
String: nome do arquivo ou url a carregar
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
String[]
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[loadBytes() ](loadBytes_)[saveStrings()](saveStrings_)[saveBytes()](saveBytes_)
